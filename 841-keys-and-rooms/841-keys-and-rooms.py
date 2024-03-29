class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        Q = deque([rooms[0]])
        
        while Q:
            room_list = Q.popleft()
            for room in room_list:
                if room not in visited:
                    visited.add(room)
                    Q.append(rooms[room])
        

        return len(visited) == len(rooms)
        
        