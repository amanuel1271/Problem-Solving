#programmers.co.kr practice 


import math

answer = math.inf

def DFS(n, pos, num, number):
    global answer
    if pos > 8:
        return
    if num == number:
        answer = min(answer,pos)
        return

    nn=0
    for i in range(8):
        nn=nn*10+n
        DFS(n, pos+1+i, num+nn, number)
        DFS(n, pos+1+i, num-nn, number)
        DFS(n, pos+1+i, num*nn, number)
        DFS(n, pos+1+i, num/nn, number)

def solution(N, number):    
    DFS(N, 0, 0, number)    
    return answer if answer != math.inf else -1
