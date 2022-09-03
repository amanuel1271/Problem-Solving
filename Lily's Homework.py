#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def swap_all(dic,arr,i,index_sorted):
    dic[arr[i]],dic[arr[index_sorted]] = index_sorted,i
    arr[i],arr[index_sorted] = arr[index_sorted],arr[i]
    
    
    
    
    
def swap_cnt(asc_num_to_index,asc_sorted,cmp_asc):
    swap = 0
    
    for i in range(len(cmp_asc)):
        if cmp_asc[i] == asc_sorted[i]:
            continue
        index_sorted = asc_num_to_index[asc_sorted[i]]
        swap_all(asc_num_to_index,cmp_asc,i,index_sorted)
        swap += 1
    return swap
    

def lilysHomework(arr):
    asc_sorted = sorted(arr)
    desc_sorted = asc_sorted[::-1]
    cmp_asc,cmp_desc = arr[:],arr[:]
    asc_num_to_index,asc_swap = {},0
    desc_num_to_index,desc_swap = {},0
    
    for i,num in enumerate(arr):
        asc_num_to_index[num] = i
        desc_num_to_index[num] = i
    
    return min(swap_cnt(asc_num_to_index,asc_sorted,cmp_asc), swap_cnt(desc_num_to_index,desc_sorted,cmp_desc))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
