import collections
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num)==0:
            return None
        stack=[]
        stack.append(num[0])
        top=0
        for i in range(1, len(num)):
            print(stack, num[i])
            if stack[top]>num[i] or k==0:
                while k>0 and top>=0 and stack[top]>num[i]:
                    stack.pop()
                    top-=1
                    k-=1
            stack.append(num[i])
            top+=1
        while k>0:
            stack.pop()
            k-=1

        return "".join(stack)


        


if __name__=="__main__":
    s=Solution()
    print(s.removeKdigits("1111111", 3))