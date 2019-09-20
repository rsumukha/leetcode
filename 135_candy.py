class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        #2 pass O(n) and O(n), 2 array
        # larray=[1,2,3,4,1,1,1]
        # rarray=[1,1,1,1,3,2,1]
        
        
        ###One pass O(n) and O(1)
        totalC=1
        downCount=0
        upCount=1
        maxi=1
        for nextp in range(1,len(ratings)):
            extra=0
            if ratings[nextp]>ratings[nextp-1]:
                downCount=0
                upCount+=1
                maxi=upCount
                totalC+=upCount
            elif ratings[nextp]<ratings[nextp-1]:
                downCount+=1
                if downCount>=maxi:
                    extra=1
                    maxi+=1
                upCount=1
                totalC+=downCount+extra
            else:
                downCount=0
                upCount=1
                maxi=upCount
                totalC+=1
                
        return totalC
            
        