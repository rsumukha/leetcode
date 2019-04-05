class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        max_diff = -1
        i = 0
        j = len(prices) - 1
        max = prices[j]
        min = prices[i]
        while (prices[i] >= prices[i + 1] and i + 1 < j):
            i += 1
        while (prices[j] <= prices[j - 1] and i < j - 1):
            j -= 1

        while (i < j):
            min = prices[i]
            max = prices[j]
            if max - min > max_diff:
                max_diff = max - min
                print(i,j,max_diff)
            while i + 1 < j and prices[i] >= min:
                if prices[i] > max:
                    if prices[i]-min>max_diff:
                        max_diff = prices[i] - min
                        print(i, j, max_diff)
                i += 1
            min = prices[i]
            max = prices[j]
            if max - min > max_diff:
                max_diff = max - min
                print(i,j,max_diff)


        if max_diff == -1:
            return 0
        return max_diff


if __name__=="__main__":
    s=Solution()
    print(s.maxProfit([7,1,5,3,6,4]))