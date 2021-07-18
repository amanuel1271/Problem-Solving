
def BinarySearch(Arr,Elem):
    if len(Arr) == 0 or Elem < Arr[0]:
        return 0
    
    Left = 0
    Right = len(Arr)
    while Left + 1 < Right:
        N = (Left + Right) // 2
        if Elem >= Arr[n]:
            Left = N
        else:
            Right = N 
            
    return Right




def Classify(Two_Dim_Arr,X_List,Y_Of_Corr_X):
    arr_len = len(Two_Dim_Arr)
    for index in range(arr_len):
        value = Two_Dim_Arr[index]
        new_list = []
        while (Two_Dim_Arr[index][0] == value[0]):   
            new_list.append(Two_Dim_Arr[index][1]) 
            if index == len_ - 1:
                break 
                
        X_List.append(value[0])
        Y_Of_Corr_X.append(sorted(new_list))

            
            

def StoreIndice(Y_Of_Corr_X,All_Y_list,Indice_List):
        Y_Len = len(All_Y_list)
        for index in range(len(Y_Of_Corr_X)):
            Another_Len = len(Y_Of_Corr_X[index])
            for i in range(Y_Len + 1):
                if i == Y_Len:
                    Indice_List[index][i] = Another_Len
                    break 
                Elem =  All_Y_list[i]
                The_List = Y_Of_Corr_X[index]
                
                if Elem <= The_List[0]:
                    Indice_List[index][i] = 0  
                elif Elem > The_List[-1]:
                    Indice_List[index][i] = Another_Len 
                else:
                    for j in range(Another_Len):
                        if Elem <= The_List[j]:
                            Indice_List[index][i] = j
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
        



    def query(self, rect) -> int:
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
