class Solution(object):
    def reorderLogFiles(self, logs):
        
        llogs = []
        dlogs = []
        
        for log in logs:
            if log.split(" ")[1].isdigit():
                dlogs.append(log)
            else:
                llogs.append(log)
        llogs.sort(key = lambda x: x[0])
        llogs.sort(key = lambda x : x.split()[1:] )
        return llogs+dlogs
    
        
