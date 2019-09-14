class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]

        maxlen=0

        for i, char in enumerate(s):
            if char=='(':
                stack.append(i)
            elif len(stack)!=0:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    maxlen=max(maxlen, i-stack[len(stack)-1])
        return maxlen
