#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def count(n):
    return (n*(n+1))//2

def convert(string):
    freq = [0]*26
    for ch in string:
        freq[ord(ch) - ord('a')] += 1
        
    for i in range(len(freq)):
        freq[i] = str(freq[i])
        
    return ''.join(freq)
    
def sherlockAndAnagrams(s):
    # Write your code here
    anagram_cnt = dict()
    for l in range(len(s)):
        for r in range(l,len(s)):
            converted_str = convert(s[l:r+1])
            anagram_cnt[converted_str] = anagram_cnt.get(converted_str,0) + 1
            
    pair_cnt = 0
    for word in anagram_cnt:
        pair_cnt += count(anagram_cnt[word] - 1)
        
    return pair_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
