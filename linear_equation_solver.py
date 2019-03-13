class Solution(object):
    def solve(self, string):
        string.strip()
        arr=string.split("=")

if __name__=="__main__":
    s=Solution()
    print(s.solve("x =x+1"))