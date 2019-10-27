class HitCounter(object):

    def __init__(self):
        self.hitarray = [0 for i in range(300)]
        self.timearray = [0 for i in range(300)]
        

    def hit(self, timestamp):
        if self.timearray[timestamp%300] == timestamp:
            self.hitarray[timestamp%300] += 1
        else:
            self.timearray[timestamp%300] = timestamp
            self.hitarray[timestamp%300] = 1
        

    def getHits(self, timestamp):
        total = 0
        for i in range(300):
            if timestamp - self.timearray[i] < 300:
                total += self.hitarray[i]
        return total
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
