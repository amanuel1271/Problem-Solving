class UndergroundSystem:

    def __init__(self):
        self.id_reg = {}
        self.time_to_finish = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.id_reg:
            return
        self.id_reg[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.id_reg:
            return
        name,start_time = self.id_reg[id]
        if name in self.time_to_finish and stationName in self.time_to_finish[name] :
            self.time_to_finish[name][stationName].append(t-start_time)
        elif name in self.time_to_finish:
            self.time_to_finish[name][stationName] = [t-start_time]
        else:
            self.time_to_finish[name] = {stationName:[t-start_time]}
            
        del self.id_reg[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        size = len(self.time_to_finish[startStation][endStation])
        return sum(self.time_to_finish[startStation][endStation]) / size
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)