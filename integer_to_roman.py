class Solution(object):
    def intToRoman(self, num):
        roman = ["I", "V", "X", "L", "C", "D", "M"]
        values=[1, 5, 10, 50, 100, 500, 1000]
        return self.cal(roman, values, num)

    def cal(self, roman, values, num):
        #whats the biggest value that divides the number
        index=0
        while(index<=len(values)-1):
            if num>values[index]:
                index+=1
            elif num==values[index]:
                return roman[index]
            else:
                break
        if values[index]==num+values[index-1]:
            return roman[index-1]+roman[index]+self.cal(roman[0:index], values[0:index], num%values[index-1])
        else:
            
        exit()


if __name__=="__main__":
    s=Solution()
    print(s.intToRoman(60))