class Solution(object):
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        start = newInterval[0]
        end = newInterval[1]
        results = []
        i = 0
        
        #case left append
        if end < intervals[0][0]:
            results.append([start, end])
            [results.append(i) for i in intervals]
            return results
        
        #case right append
        if start > intervals[len(intervals)-1][1]:
            intervals.append([start, end])
            return intervals
        
        #case merge
        while i < len(intervals):
            current = intervals[i]
            if start <= current[0] and current[0] <= end <= current[1]:
                end = intervals[i][1]
                i += 1
            elif end >= current[1] and current[0] <= start <= current[1]:
                start = intervals[i][0]
                i += 1
            elif (current[0] <= start <= current[1]) and (current[0] <= end <= current[1]):
                start = current[0]
                end = current[1]
                i+=1
            elif start <= current[0] and end >= current[1]:
                i+=1
            else:
                results.append(current)                
                i+=1
                
        ret = []
        appendflag =False
        for item in results:
            if not appendflag and item[0]>start:
                ret.append([start, end])
                appendflag = True
            ret.append(item)
        if not appendflag:
            ret.append([start, end])
        return ret
