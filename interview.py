from collections import defaultdict
import math

def add_tup(x,y):
    return (x[0] + y[0],x[1] + y[1])

def check_completed(pos,coor,lb_pos_next):
    coor_1,coor_2,coor_3 = coor
    coordinate_path = []
    for x,y in [pos]:
        for dx,dy in [(0,0),coor_1,coor_2,coor_3]:
            coordinate_path.append((x + dx,y+dy))    
    coordinate_path.sort()

    cond_1 = add_tup(pos,coor_1) in lb_pos_next[pos]
    cond_2 = add_tup(pos,coor_2) in lb_pos_next[add_tup(pos,coor_1)]
    cond_3 = add_tup(pos,coor_3) in lb_pos_next[add_tup(pos,coor_2)]
    cond_4 = pos in lb_pos_next[add_tup(pos,coor_3)]

    res = cond_1 and cond_2 and cond_3 and cond_4
    res_str = ''

    for x,y in coordinate_path:
        res_str += str(x) + str(y)

    return (res,res_str) if res else (res,'')




def solution(moves):
    cnt = 0
    pos = (0,0)
    lb_pos_completed = set()
    lb_pos_next = defaultdict(set)
    visited = {pos}
    ch_to_dist = {'U': (1,0),'D': (-1,0),'L': (0,-1),'R': (0,1)}

    for move in moves:
        print(pos)
        dx,dy = ch_to_dist[move]
        x_,y_ = pos[0] + dx,pos[1] + dy
        lb_pos_next[pos].add((x_,y_))
        n = (x_,y_)

        if (x_,y_) not in visited:
            visited.add((x_,y_))
        else:
            for coor in [((1,0),(1,1),(0,1)), ((0,1),(1,1),(1,0))]:
                cond_1,res_str = check_completed(n,coor,lb_pos_next)
                if cond_1 and res_str not in lb_pos_completed:
                    cnt += 1
                    lb_pos_completed.add(res_str)
                    pos = n
                    break
            for coor in [((0,-1),(1,-1),(1,0)), ((1,0),(1,-1),(0,-1))]:
                cond_1,res_str = check_completed(n,coor,lb_pos_next)
                if cond_1 and res_str not in lb_pos_completed:
                    cnt += 1
                    lb_pos_completed.add(res_str)
                    pos = n
                    break

            for coor in [((-1,0),(-1,-1),(0,-1)), ((0,-1),(-1,-1),(-1,0))]:
                cond_1,res_str = check_completed(n,coor,lb_pos_next)
                if cond_1 and res_str not in lb_pos_completed:
                    cnt += 1
                    lb_pos_completed.add(res_str)
                    pos = n
                    break
            for coor in [((0,1),(-1,1),(-1,0)), ((-1,0),(-1,1),(0,1))]:
                cond_1,res_str = check_completed(n,coor,lb_pos_next)
                if cond_1 and res_str not in lb_pos_completed:
                    cnt += 1
                    lb_pos_completed.add(res_str)
                    pos = n
                    break
           

        pos = n

    return cnt


moves = 'URDLDLURRDLUULDR'
print(solution(moves))