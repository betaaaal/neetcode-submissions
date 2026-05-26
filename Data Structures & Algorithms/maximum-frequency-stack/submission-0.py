class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)      # val -> frequency
        self.group = defaultdict(list)    # frequency -> stack of values
        self.maxfreq = 0

    def push(self, val: int) -> None:
        # increase frequency
        self.freq[val] += 1
        f = self.freq[val]

        # update max frequency
        self.maxfreq = max(self.maxfreq, f)

        # add value to that frequency stack
        self.group[f].append(val)

    def pop(self) -> int:
        # pop from highest frequency stack
        val = self.group[self.maxfreq].pop()

        # decrease its frequency
        self.freq[val] -= 1

        # if no elements left with max frequency
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()