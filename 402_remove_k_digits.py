import collections
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=collections.deque()
        top=0
        loc_max=-1
        while i<len(num) and k>0:

            if num[i]<num[i+1]:
                stack.append(num[i])
                loc_max=max(loc_max, int(num[i])

            elif num[i]>loc_max:
                k-=1
            
            i+=1


        if i==len(num)-1 and k>0:
            while k>0:
                stack.pop()

        for i in range(len(stack)):
            ret_num.append(stack.popleft())

        if len(ret_num)==0:
            return 0
        return int("".join(ret_num))
            
        


if __name__=="__main__":
    s=Solution()
    print(s.removeKdigits("1432219"))