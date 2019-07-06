#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio


async def task_fizzbuzz(prefix):
    for x in range(1, 10):
        # await asyncio.sleep(1)
        print(prefix + "{}:".format(str(x)) + fizzbuzz(x))
    return None


def fizzbuzz(i):
    if i == 15:
        return 'FizzBuzz'
    if i % 5 == 0:
        return 'Buzz'
    if i % 3 == 0:
        return 'Fizz'
    return str(i)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # コルーチン10万個生成
    tasks = asyncio.wait([task_fizzbuzz(str(i) + ":") for i in range(1, 100000)])
    loop.run_until_complete(tasks)
    loop.close()



