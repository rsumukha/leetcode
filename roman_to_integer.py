class Solution(object):
    def romanToInt(self, s):
        roman = ["I", "V", "X", "L", "C", "D", "M"]
        values = [1, 5, 10, 50, 100, 500, 1000]

        value=0
        val_copy=0
        for r in s:
            val= values[roman.index(r)]
            if val>val_copy:
                value=v
            value=value+val
            val_copy=val
        return value

if __name__=="__main__":
    s=Solution()
    print(s.romanToInt("XIV"))
