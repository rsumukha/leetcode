class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s
        if numRows==2:
            return_string = (s[0 : len(s) : 2])+(s[1 : len(s): 2])
            return return_string
        return_string=[[] for i in range(numRows)]
        #print(return_string)
        index=0
        index_out_of_bound=0
        #print(len(s))
        #exit()
        while(index<=len(s)-1 and index_out_of_bound==0):
            j=0
            while(j<numRows and index_out_of_bound==0):#for j in range(numRows):
                #print(s[index])
                return_string[j].append(s[index])
                index+=1
                if index==len(s):
                    index_out_of_bound=1
                j+=1
                #print(return_string)

            j-=2
           # p(return_string)
            #print(j)

            while(j>0 and index_out_of_bound==0):
                #print(index)
                return_string[j].append(s[index])
                index += 1
                if index == len(s):
                    index_out_of_bound = 1
                j-=1
            #p(return_string)
            #exit()
        _string=""
        #print(return_string)
        for i in range(numRows):
            _string=_string+''.join(return_string[i])

        return _string

def p( s):
        for i in range(len(s)):
            print(s[i])

if __name__=="__main__":
    s=Solution()
    print(s.convert("PAYPALISHIRING", 4))
    print("PINALSIGYAHRPI")
