
#dictionary solution takes too much space and doesnt scale properly,  it blows up if too many messages come
#make the program threadsafe by putting locks

class Logger(object):

    def __init__(self):
        from collections import deque
        self.dictionary = {}
        
        # dictionary solution takes too much space
        #self.dictionary = {}
        

    def shouldPrintMessage(self, timestamp, message):
        for item in self.dictionary.keys():
            if timestamp - self.dictionary[item] >= 10:
                del self.dictionary[item]
                
        if message in self.dictionary:
            return False
        self.dictionary[message] = timestamp
        return True
        
        
        # if message in self.dictionary:
        #     if timestamp - self.dictionary[message] < 10:
        #         return False
        # self.dictionary[message] = timestamp
        # return True
            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
