class Solution(object):
    def isMatch(self, s, p):
        #print(len(s))
        #print(len(p))
        if len(p)==0:
            return False
        if len(s)==0:
            if p[0]==".":
                return True
            else:
                return False
        index=0
        while(s[index]==p[index] and (index<len(s)-1 and index<len(p)-1)):
            index+=1
        if index==len(s):
            return True
        str_index=index
        j_=str_index
        while(j_<=len(p)-1):
            if str_index  == len(s):
                return True
            if s[str_index] == p[j_]:
                str_index+=1
                j_+=1

            else:
                if p[j_] == ".":
                    str_index+=1
                if p[j_] == "*":
                    if p[j_-1]==".":
                        return True
                    _char = p[j_-1]
                    for k in range(str_index, len(s)):
                        if s[k]!=_char:
                            break
                        str_index+=1
                j_+=1
        if (str_index+1)==len(s):
            return True
        else:
            return False


if __name__=="__main__":
    s=Solution()
    print(s.isMatch("aa", "a"))