# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.index = 0
        self.value = math.inf # result of self.hasNext
        
    
    def next(self) -> int:
        return self.value
            
    def hasNext(self) -> bool:
        if self.index >= len(self.nestedList):
            return False
        
        if self.nestedList[self.index].isInteger():
            self.value = self.nestedList[self.index].getInteger()
            self.index += 1
            return True
        
        def dfs(lst):
            for element in lst:
                if element.isInteger():
                    self.value = element.getInteger()
                    lst.remove(element)
                    return True

                if dfs(element.getList()):
                    return True
            
            return False
        
        if dfs(self.nestedList[self.index].getList()):
            return True
        self.index += 1
        return self.hasNext()
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())