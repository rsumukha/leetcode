class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b_dict = {'(': ')',
                  '[': ']',
                  '{': '}'}
        if len(s) == 1:
            return False
        stack = []
        for i in s:

            if i in b_dict:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if b_dict[stack.pop()] != i:
                    return False
        if len(stack) == 0:
            return True
        return False

if __name__=="__main__":
    s=Solution()
    print(s.isValid("()))"))
