class FreqStack:

    def __init__(self):
        self.frequency=defaultdict(int)
        self.stack=[]

    def push(self, val: int) -> None:
        self.frequency[val]+=1
        self.stack.append(val)

    def pop(self) -> int:
        maxfreq=0
        for val in self.stack:
            maxfreq=max(maxfreq, self.frequency[val]) 
        for i in range(len(self.stack)-1, -1, -1):
            v=self.stack[i]
            if self.frequency[v]==maxfreq:
                self.stack.pop(i)
                self.frequency[v]-=1
                return v

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()