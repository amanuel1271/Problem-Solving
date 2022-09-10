#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    # Write your code here
    MOD = 10**9+7
    ans = 0
    start = 1
    
    for i in range(len(n)-1,-1,-1):
        ans += start * (int(n[i]) * (i+1))
        ans %= MOD
        start  = (start * 10) + 1
        start %= MOD
        
    return ans%MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
