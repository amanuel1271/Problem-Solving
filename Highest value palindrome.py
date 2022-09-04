#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#
def different_pairs(s):
    l,r,cnt = 0,len(s)-1,0
    while l <= r:
        if s[l] != s[r]:
            cnt += 1
        l,r = l+1,r-1
    return cnt
        
def is_not_nine(ch):
    return 0 if ch == "9" else 1
    
def highestValuePalindrome(s, n, k):
    # Write your code here
    min_needed = different_pairs(s)
    if k < min_needed:
        return "-1"
    
    list_s = list(s) #because a string is immutable
    for i in range(len(s)//2):
        complement_index = -i-1
        if s[i] == s[complement_index]:
            if s[i] == '9':
                continue
            elif k >= 2 and k-2 >= min_needed-1:
                list_s[i] = '9'
                list_s[complement_index] = '9'
                k -= 2
            continue
            
        min_needed -= 1
        count_non_nine = is_not_nine(s[i]) + is_not_nine(s[complement_index])
        
        if k-count_non_nine >= min_needed:
            list_s[i] = '9'
            list_s[complement_index] = '9'
            k -= count_non_nine
        else:
            k -= 1
            list_s[i] = str(max(int(s[i]),int(s[complement_index])))
            list_s[complement_index] = list_s[i]
            
    if len(s)%2 == 1 and k >= 1:
        list_s[len(s)//2] = '9'
        
        
    return "".join(list_s)
            
            
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
