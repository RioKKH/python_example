#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import time
from multiprocessing import Pool

COUNT = 50000000

def countdown(n):
    while n > 0:
        n -= 1
        
def multi(numofcores):
    pool = Pool(processes=numofcores)
    start = time.time()
    for i in range(numofcores):
        pool.apply_async(countdown, args=(COUNT//numofcores,))
    pool.close()
    pool.join()
    
    print(f'Number of Processes {numofcores} : Took {time.time() - start : .2f} seconds.')


if __name__ == "__main__":
    multi(1)
    multi(2)
    multi(4)

