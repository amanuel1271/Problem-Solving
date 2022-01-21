class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # use kahn topological sorting method
        # if it is acyclic and all courses can be taken return True else False
        
        prereq,courses_that_need = defaultdict(int),defaultdict(list)
        
        for prerequisite,need in relations:
            prereq[need] += 1
            courses_that_need[prerequisite].append(need)
            
            
        Q = deque()
        visited = set()
        res = [[]]
        hold = []


        for course in range(1,n+1):
            if prereq[course] == 0:
                Q.append(course)
                visited.add(course)
                res[-1].append(course)
                
        if not res[-1]:
            return -1
            
        while Q:
            course = Q.popleft()
            if course not in res[-1]:
                res.append(hold)
                hold = []
                
            for classes in courses_that_need[course]:
                prereq[classes] -= 1
                if prereq[classes] == 0:
                    Q.append(classes)
                    visited.add(classes)
                    hold.append(classes)
                    

        
        return len(res) if len(visited) == n else -1
        
