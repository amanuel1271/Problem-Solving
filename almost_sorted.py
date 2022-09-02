#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def decreasing_points(arr):
    indices = []
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            indices.append(i)
    return indices
    
    
    
def can_be_swapped(arr):
    
    size_arr = len(arr)
    indices = decreasing_points(arr)
    indice_size = len(indices)
    
    if not(indice_size in [1,2]):
        return (False,0,0)
        
    if indice_size == 1:
        idx = indices[0]
        if (idx + 2 == size_arr or arr[idx] < arr[idx + 2]) and (idx - 1 < 0 or arr[idx + 1] > arr[idx-1]):
            return (True,idx,idx+1)
    elif indice_size == 2:
        idx1,idx2 = indices[0],indices[1] + 1
        if (idx2 + 1 == size_arr or arr[idx1] < arr[idx2 + 1]) and (idx1 - 1 < 0 or arr[idx2] > arr[idx1-1]):
            return (True,idx1,idx2)
        
    return (False,0,0)
    
    
    
    
def can_be_reversed(arr):
    indices = decreasing_points(arr)
    size_arr = len(arr)
    consecutive = True
    
    for i in range(1,len(indices)):
        if indices[i] != indices[i-1] + 1:
            consecutive = False
            break
    
    if not consecutive:
        return (False,0,0)
        
    idx1,idx2 = indices[0],indices[-1] + 1
    if (idx2 + 1 == size_arr or arr[idx1] < arr[idx2 + 1]) and (idx1 - 1 < 0 or arr[idx2] > arr[idx1-1]):
            return (True,idx1,idx2)
        
    return (False,0,0)

    
def almostSorted(arr):
    # Write your code here]
    
    # has duplicates
    if len(set(arr)) != len(arr):
        print("no")
        return
        
    swap_res,idx1,idx2 = can_be_swapped(arr)
    if swap_res:
        print("yes")
        print("swap {} {}".format(idx1 + 1,idx2 + 1))
        return 
        
    reverse_res,idx1,idx2 = can_be_reversed(arr)
    if reverse_res:
        print("yes")
        print("reverse {} {}".format(idx1 + 1,idx2 + 1))
        return
        
    # can't be sorted with methods
    print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
