class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if not list1 or not list2:
            return []
        d1 = {}
        for i, item in enumerate(list1):
            d1[item] = i
            
        result = []
        minval = float("inf")
        for i, item in enumerate(list2):
            if item in d1:
                if i+d1[item] < minval:
                    minval = i+d1[item]
                    result = [item]
                elif i+d1[item] == minval:
                    result.append(item)
        return result
        
