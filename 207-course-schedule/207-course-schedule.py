class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use kahn topological sorting method
        # if it is acyclic and all courses can be taken return True else False
        
        prereq,courses_that_need = defaultdict(int),defaultdict(list)
        
        for need,prerequisite in prerequisites:
            prereq[need] += 1
            courses_that_need[prerequisite].append(need)
            
            
        Q = deque()
        visited = set()
        res = []
        for course in range(numCourses):
            if prereq[course] == 0:
                Q.append(course)
                visited.add(course)
                res.append(course)
            
        while Q:
            course = Q.popleft()
            for classes in courses_that_need[course]:
                prereq[classes] -= 1
                if prereq[classes] == 0:
                    Q.append(classes)
                    visited.add(classes)
                    res.append(course)

        
        
        return res if len(visited) == numCourses else []
            
        
        