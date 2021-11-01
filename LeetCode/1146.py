class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snap_dict = defaultdict(lambda : defaultdict(int))

    def set(self, index: int, val: int) -> None:
        self.snap_dict[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id+=1
        return self.snap_id-1
        

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.snap_dict: return 0
        
        elif snap_id not in self.snap_dict[index]:
            temp = copy.deepcopy(snap_id)
            while temp>=0 and temp not in self.snap_dict[index]:
                temp-=1
            return self.snap_dict[index][temp]
        
        return self.snap_dict[index][snap_id]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)