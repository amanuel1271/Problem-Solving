def BinarySearch(arr,val):
    if len(arr) == 0 or val < arr[0]:
        return 0
    
    l = 0
    r = len(arr)
    while l + 1 < r:
        n = (l + r) // 2
        if val >= arr[n]:
            l = n
        else:
            r = n
            
    return r




def Classify(o_arr,x,y_of_x):
    i = 0
    l = len(o_arr)
    
    while i < l:
        val = o_arr[i]
        nl = []
        fin = False
        
        while o_arr[i][0] == val[0]:
            nl.append(o_arr[i][1])
            if i < l - 1:
                i += 1
            else:
                fin = True
                break
        x.append(val[0])
        y_of_x.append(sorted(nl))
        if fin:
            i += 1

            
            

def StoreIndice(y_of_x,y_list,i_list):
        y_len = len(y_list)
        for index in range(len(y_of_x)):
            another_len = len(y_of_x[index])
            for i in range(y_len + 1):
                if i == y_len:
                    i_list[index][i] = another_len
                    break 
                elem =  y_list[i]
                the_list = y_of_x[index]
                
                if elem <= the_list[0]:
                    i_list[index][i] = 0  
                elif elem > the_list[-1]:
                    i_list[index][i] = another_len 
                else:
                    for j in range(another_len):
                        if elem <= the_list[j]:
                            i_list[index][i] = j
                            break
            

            
            
class Solution(object):

    def __init__(self, points):
        self.points = points
        self.store_x = []
        self.store_y_of_cor_x = []        
        self.points.sort(key=lambda x: x[0])
        self.all_y = [x[1] for x in self.points]
        self.all_y.sort()
        self.index_info = []
        
        Classify(self.points,self.store_x,self.store_y_of_cor_x)  
        for j in range(len(self.store_y_of_cor_x)):
            y = [0  for i in range(len(self.all_y) + 1)]
            self.index_info.append(y)    
        StoreIndice(self.store_y_of_cor_x,self.all_y,self.index_info)
        



    def query(self, rect):
        count = 0
        left_most  = rect[0][0]
        right_most = rect[0][1]
        lower_most = rect[1][0]
        upper_most = rect[1][1]
        
        x1 = BinarySearch(self.store_x,right_most)
        x0 = BinarySearch(self.store_x,left_most - 1)
        y1 = BinarySearch(self.all_y,upper_most)
        y0 = BinarySearch(self.all_y,lower_most - 1)
        
        
        for i in range(x0,x1):      
            count += (self.index_info[i][y1] - self.index_info[i][y0]) 
            
        return count


if __name__ == "__main__":
    points = [[1, 1], [3, 3], [2, 2], [1, 3]]
    sol = Solution(points)
    print(sol.query([[1,3], [1,3]]))
    print(sol.query([[1,5], [2,5]]))
