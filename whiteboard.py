# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


def can_balance(arr,target):
    
    def backtrack_sum(nums):
        answer = set()
        def backtrack(i,sum_):
            if i == len(nums):
                answer.add(sum_)
                return
            backtrack(i+1,sum_ + arr[i])
            backtrack(i+1,sum_) 
            
        backtrack(0,0)
        return answer
        
    def find_sum(i,complement_arr,sum_):
        if i == len(arr):
            for candids in backtrack_sum(complement_arr):
                if abs(candids - sum_) == target:
                    return True
            return False
        
        if find_sum(i+1,complement_arr,sum_ + arr[i]):
            return True
        complement_arr.append(arr[i])
        if find_sum(i+1,complement_arr,sum_):
            return True
        complement_arr.pop()
        return False
        
    return find_sum(0,[],0)

print(can_balance([5,10],15))
            
