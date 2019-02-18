class Solution(object):
    def reverse(self, x):
        string_x = str(x)
        if string_x[0].isdigit() == False:
            return_x = int(string_x[0] + string_x[len(string_x):0:-1])
        else:
            return_x = int(string_x[::-1])
        if return_x > (2 ** 31 - 1) or return_x < -(2 ** 31):
            return 0
        else:
            return return_x

if __name__=="__main__":
    s=Solution()
    print(s.reverse(1563847412))
