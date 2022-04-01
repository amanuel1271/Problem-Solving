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
            prev_val,prev_count = self.time_to_finish[name][stationName][0],self.time_to_finish[name][stationName][1]
            self.time_to_finish[name][stationName] = (prev_val + (t-start_time),prev_count + 1)
        elif name in self.time_to_finish:
            self.time_to_finish[name][stationName] = (t-start_time,1)
        else:
            self.time_to_finish[name] = {stationName:(t-start_time,1)}
            
        del self.id_reg[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time_to_finish[startStation][endStation][0] / (self.time_to_finish[startStation][endStation][1])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)