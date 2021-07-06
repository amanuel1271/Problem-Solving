
def binary_search(arr,x):
    if len(arr) == 0 or x < arr[0]:
        return 0
    left = 0
    right = len(arr)
    
    while( left + 1 < right):
        n = (left + right)
        n  = n // 2
        if x >= arr[n]:
            left = n
        else:
            right = n
            
    return right


def classify(ori_arr,x,y_of_x):
    index = 0
    len_ = len(ori_arr)
    
    while  index < len_:
        value = ori_arr[index]
        new_list = []
        exit_loop = False    
        while (ori_arr[index][0] == value[0]):   
            new_list.append(ori_arr[index][1])  
            if index < len_ - 1:
                index += 1
            else:
                exit_loop = True
                break
                
        x.append(value[0])
        y_of_x.append(sorted(new_list))
        if (exit_loop):
            index += 1


def store_indice(y_of_x,all_y,indice_list):
        index = 0
        len__ = len(all_y)
        
        while (index < len(y_of_x)):
            i = 0
            another_len = len(y_of_x[index])
            
            while (i < len__ + 1):
                if i == len__:
                    indice_list[index][i] = another_len
                    break 
                    
                elem =  all_y[i]
                the_list = y_of_x[index]
                
                if elem <= the_list[0]:
                    indice_list[index][i] = 0  
                elif elem > the_list[-1]:
                    indice_list[index][i] = another_len 
                else:
                    j = 0
                    
                    while (j < another_len):
                        if elem <= the_list[j]:
                            indice_list[index][i] = j
                            break
                            
                        j += 1
                        
                i += 1 
                
            index += 1
            

class Solution(object):

    def __init__(self, points):
        self.points = points
        self.store_x = []
        self.store_y_of_cor_x = []
        self.points.sort(key=lambda x: x[0])
        self.all_y = [x[1] for x in self.points]
        self.all_y.sort()
        self.index_info = []
        
        classify(self.points,self.store_x,self.store_y_of_cor_x)    
        
        for j in range(len(self.store_y_of_cor_x)):
            y = [0  for i in range(len(self.all_y) + 1)]
            self.index_info.append(y)
            
        store_indice(self.store_y_of_cor_x,self.all_y,self.index_info)
        



    def query(self, rect) -> int:

        count = 0
        left_most  = rect[0][0]
        right_most = rect[0][1]
        lower_most = rect[1][0]
        upper_most = rect[1][1]

        x1 = binary_search(self.store_x,right_most)
        x0 = binary_search(self.store_x,left_most - 1)
        initial_loop = True
        
        for i in range(x0,x1):
            
            if (initial_loop):
                y1 = binary_search(self.all_y,upper_most)
                y0 = binary_search(self.all_y,lower_most - 1)
                save_y0  = y0
                save_y1 = y1
                y1 = self.index_info[i][y1]
                y0 = self.index_info[i][y0]
                initial_loop = False

            else:
                y1 = self.index_info[i][save_y1]
                y0 = self.index_info[i][save_y0]
                
            count += (y1 - y0) 
            
        return count


if __name__ == "__main__":
    points = [[1, 1], [3, 3], [2, 2], [1, 3]]
    sol = Solution(points)
    print(sol.query([[1,3], [1,3]]))
    print(sol.query([[1,5], [2,5]]))
