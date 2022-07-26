#programmers.co.kr practice 
import math
answer = math.inf


def solution(N, number):   
    def DFS(pos, num, number):
        global answer
        if pos > 8:
            return
        if num == number:
            answer = min(answer,pos)
            return

        nn=0
        for i in range(8):
            nn=nn*10+N
            DFS(pos+1+i, num+nn, number)
            DFS(pos+1+i, num-nn, number)
            DFS(pos+1+i, num*nn, number)
            DFS(pos+1+i, num/nn, number)
            
    DFS(0, 0, number)    
    return answer if answer != math.inf else -1
