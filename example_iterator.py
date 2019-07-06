#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def iterator_sample():
    l = [1, 2, 3]
    iterator_object = iter(l)
    while True:
        try:
            obj = next(iterator_object)
            print(obj)
        except StopIteration as e:
            break
        except Exception as e:
            print("Error: ", e)
            sys.exit(1)


class MyIterator(object):
    # 特殊メソッド: __xxx___()の形式の特定の名前を持つメソッドのこと
    # イテレータプロトコルを実装する
    # オブジェクトがイテレータとして振る舞うためには、
    # __next__()　と　__iter__()の2つの特殊メソッドが必要になる
    def __init__(self, start, stop):
        self._counter = start
        self._stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        # オブジェクトがnext()で呼ばれたときに、__next__()メソッドが処理の
        # 実体として動作する
        if self._counter > self._stop:
            raise StopIteration()
        ret = self._counter
        self._counter += 1
        return ret

    def next(self):
        # for python2
        return self.__next__()


def MyContainer(object):
    '''
    コンテナオブジェクト
    イテレータプロトコルの中で__iter__()だけを実装したものがイテレータの
    コンテナオブジェクトになる。リストがコンテナオブジェクトになる
    '''

    def __init__(self, start, stop):
        print(self._start, self._stop)
        self._start = start
        self._stop = stop

    def __iter__(self):
        # コンテナクラスの__iter__()ではイテレータオブジェクトを返す
        return MyIterator(start=self._start, stop=self._stop)


if __name__ == '__main__':
    iterator_sample()

    c = MyIterator(start=1, stop=3)
    print(next(c))
    print(next(c))
    print(next(c))
    #print(next(c)) # Error

    container_object = MyContainer(start=1, stop=3)
    #container_object = MyContainer(start=1, stop=3)
    # コンテナオブジェクトからiter()を使ってイテレータオブジェクトをゲット
    d = iter(container_object)


