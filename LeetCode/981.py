class TimeMap:

    def __init__(self):
        self.store = dict()
        self.time = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = dict()
            self.time[key] = list()
            
        self.store[key][timestamp] = value
        self.time[key].append(timestamp)
        


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        if timestamp in self.store[key]:
            return self.store[key][timestamp]
        
        idx = bisect.bisect_left(self.time[key], timestamp)-1
        if idx ==-1:
            return ""
        return self.store[key][self.time[key][idx]]
