class Solution(object):
    def myAtoi(self, str):
        str=str.strip()

        if len(str) == 0:
            return 0
        elif len(str)==1:
            if str[0].isdigit()==1:
                return int(str)
            else:
                return 0
        _list = []
        neg = 1

        if str[0] == "-":
            neg = -1
        elif str[0] == "+":
            neg=1
        elif str[0].isdigit()==1:
            _list.append(str[0])
        else:
            return 0


        for i in range(1, len(str)):
            if str[i].isdigit():
                _list.append(str[i])
            else:
                break
        if len(_list) == 0:
            return 0
        else:
            return_int = int("".join(_list)) * neg
            if return_int > (2 ** 31) - 1:
                return (2 ** 31) - 1
            if return_int < (-(2 ** 31)):
                return (-1) * (2 ** 31)
            else:
                return return_int

if __name__=="__main__":
    s=Solution()
    print(s.myAtoi("+12"))