class Solution(object):
    def convroman(self, roman, values, rem, place):
        num=rem*place
        index = 0
        while (index <= len(values) - 1):
            if num > values[index]:
                index += 1
            elif num == values[index]:
                return roman[index]
            else:
                break
        index -= 1

        split=num%values[index]

        i = values.index(place)
        if rem == 4 or rem == 9:
            return roman[i] + roman[index + 1]

        if split==0:
            return roman[index] * int(num / values[index])
        else:
            return roman[index]+ roman[index-1]*int(split/ values[index-1])



    def intToRoman(self, num):
        roman = ["I", "V", "X", "L", "C", "D", "M"]
        values=[1, 5, 10, 50, 100, 500, 1000]

        num_copy=num
        place=1
        return_list=[]
        while(num>0):
            rem=num % 10
            return_list.append(self.convroman(roman, values, rem, place))
            place=place*10
            num =int( num / 10)
        return "".join(return_list[::-1])

if __name__=="__main__":
    s=Solution()
    print(s.intToRoman(8))