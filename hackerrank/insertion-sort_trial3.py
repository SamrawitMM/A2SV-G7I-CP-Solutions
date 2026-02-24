#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    element_compared = arr[-1]
    
    placed = False
    for i in range(n-2, -1, -1):
        if arr[i] > element_compared:
            arr[i+1] = arr[i]
            print(*arr)
        elif arr[i] <= element_compared:
            placed = True
            arr[i+1] = element_compared
            print(*arr)
            break
            
    if not placed:
        arr[0] = element_compared
        print(*arr)
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
   
    insertionSort1(n, arr)
