#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
https://qiita.com/icoxfog417/items/07cbf5110ca82629aca0
------------------------------------------------------------
# マルチスレッド
## プロセス中の処理単位。同じプロセス間のスレッドはメモリを共有する
# マルチプロセス
## 固有のメモリ空間を持つ処理単位。マルチコアCPUの場合、各コアに
対してプロセスを割り当てることができる
# ノンブロッキング
## マルチスレッドの弱点を克服する方法として生まれたもの
多数のリクエストをさばく際の手法に違いがある
## ブロッキングが効果的なのは以下の様なケース
### ボトルネックとなるような重たい処理がある
### その処理は大量に発生する
### 処理を完了させる順序は問わない
### 具体的にはURLからのページ取得や、DBからのデータ取得、つまりI/O関連
### CPU bound な問題の場合にはmultiprocessを用いれば良い。

### coroutine
    async関数の返り値はcoroutineになる
### Future
### Task
    Futureのサブクラス。実行を管理する。直接作ることはない、作ってはいけない。
"""

import asyncio
import concurrent.futures
import requests


Seconds = [
    ("first", 5),
    ("second", 0),
    ("third", 3)
]


async def sleeping(order, seconds, hook=None):
    await asyncio.sleep(seconds)
    if hook:
        hook(order)
    return order


async def basic_async():
    # the order of result is nonsequential (not depends on order, even sleeping time)
    for s in Seconds:
        r = await sleeping(*s)
        print("{0} is finished.".format(r))
    return True


async def parallel_by_gather():
    """
    予め並列で実行したい処理の数が決まっている場合、
    それらを並列で一斉に処理させることができる
    """
    # execute by parallel
    def notify(order):
        print(order + " has just finished.")

    cors = [sleeping(s[0], s[1], hook=notify) for s in Seconds]
    # asyncio.gatherは実行される順番は不定も、返す順番は渡した順番どおり
    results = await asyncio.gather(*cors)
    return results


async def parallel_by_wait():
    # execute by parallel
    def notify(order):
        print(order + " has just finished.")

    cors = [sleeping(s[0], s[1], hook=notify) for s in Seconds]
    done, pending = await asyncio.wait(cors)
    return done, pending


async def queue_execution(arg_urls, callback, parallel=2):
    """
    並列処理する長さが予め不定の場合にはQueueが使える。
    """
    # see refs
    # http://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio

    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    for u in arg_urls:
        # queueの中にput_nowait()で処理対象をどんどんいれていく
        queue.put_nowait(u)

    async def fetch(q):
        # queueが殻にならない限りどんどん処理をしていく
        # 今回は1つのqueueで2つのcoroutineを分担している
        while not q.empty():
            u = await q.get()
            # run_in_executorを使うことで、普通の関数をFuture化出来る
            future = loop.run_in_executor(None, requests.get, u)
            future.add_done_callback(callback)
            await future

    tasks = [fetch(queue) for i in range(parallel)]
    return await asyncio.wait(tasks)


async def limited_parallel(limit=3):
    sem = asyncio.Semaphore(limit)

    # 並列で実行するプロセスの下図を制御する場合
    # function want to limit the number of parallel
    async def limited_sleep(num):
        # Semaphoreが空くのを待つ
        with await sem:
            return await sleeping(str(num), num)

    import random
    tasks = [limited_sleep(random.randint(0, 3)) for i in range(9)]
    return await asyncio.wait(tasks)


async def future_callback(callback):
    """
    非同期処理の完了後にコールバック処理をしたい
    """
    futures = []

    for s in Seconds:
        cor = sleeping(*s)
        f = asyncio.ensure_future(cor)
        f.add_done_callback(callback)
        futures.append(f)

    await asyncio.wait(futures)


def get_async_iterator(arg_urls):
    """
    データベースからの逐次読み出しなど、Iteratorでありつつ処理はノンブロッキング
    で流したい場合は、Iteratorを自作することが可能
    """

    class AsyncIterator():

        def __init__(self, urls):
            self.urls = iter(urls)
            self.__loop = None

        async def __aiter__(self):
            self.__loop = asyncio.get_event_loop()
            return self

        async def __anext__(self):
            try:
                u = next(self.urls)
                future = self.__loop.run_in_executor(None, requests.get, u)
                resp = await future
            except StopIteration:
                raise StopAsyncIteration
            return resp


    return AsyncIterator(arg_urls)


def print_num(num):
    print(num)

async def async_by_process():
    executor = concurrent.futures.ProcessPoolExecutor()
    queue = asyncio.Queue()

    for i in range(10):
        queue.put_nowait(i)

    async def proc(q):
        while not q.empty():
            i = await q.get()
            future = loop.run_in_executor(executor, print_num, i)
            await future

    tasks = [proc(queue) for i in range(4)]  #cpu core
    return await asyncio.wait(tasks)


if __name__ == "__main__":
    # ノンブロッキングなthread
    loop = asyncio.get_event_loop()

    print("@basic async ******************************************")
    # asyncな関数を渡す
    # イベントループ内に1つしかcontinueがない場合、async/awaitは
    # 効果を発揮しない
    loop.run_until_complete(basic_async())

    print("@parallel by gather ***********************************")
    # the result of asyncio.gather is mysterious!
    results = loop.run_until_complete(parallel_by_gather())
    for r in results:
        print("asyncio.gather result: {0}".format(r))

    print("@parallel by wait *************************************")
    done, pending = loop.run_until_complete(parallel_by_wait())
    for d in done:
        dr = d.result()
        print("asyncio.wait result: {0}".format(dr))

    print("@queue execution **************************************")
    results = []
    def store_result(f):
        results.append(f.result())
    results.clear()
    loop.run_until_complete(queue_execution([
        "http://www.google.com",
        "http://www.yahoo.com",
        "https://github.com/"
    ], store_result))
    for r in results:
        print("queue execution: {0}".format(r.url))

    print("@limited parallel **************************************")
    done, pending = loop.run_until_complete(limited_parallel())
    for d in done:
        print("limited parallel: {0}".format(d.result()))

    print("@future callback **************************************")
    results.clear()
    loop.run_until_complete(future_callback(store_result))
    for r in results:
        print("future callback: {0}".format(r))

    print("@async iterator ***************************************")
    async def async_fetch(urls):
        ai = get_async_iterator(urls)
        async for resp in ai:
            print(resp.url)

    loop.run_until_complete(async_fetch([
        "http://www.google.com",
        "http://www.yahoo.com",
        "https://github.com/"
    ]))

    print("@async by process *************************************")
    loop.run_until_complete(async_by_process())
