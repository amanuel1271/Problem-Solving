# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        for person in range(n):
            know = False
            other_know = True
            for ano_person in range(n):
                if ano_person == person:
                    continue
                    
                if knows(person,ano_person):
                    know = True
                    break
                if not knows(ano_person,person):
                    other_know = False
                    break
            
            if not know and other_know:
                return person
        
        return -1
            
            
                    
                
        