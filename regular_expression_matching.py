class Solution(object):
    def isMatch(self, s, p):
        #print(len(s))
        #print(len(p))
        if len(p)==2:
            if p[0]=="." and p[1]=="*":
                return True
        if len(p)==0:
            return False
        if len(s)==0:
            if p[0]==".":
                return True
            else:
                return False
        index=0
        while(index<=len(s)-1 and index<=len(p)-1):
            if (s[index]==p[index]):
                index+=1
            else:
                break
        if index==len(s):
            return True
        str_index=index
        j_=str_index
        traversed=False
        while(j_<=len(p)-1):
            if str_index  == len(s):
                traversed=True
                break
            if s[str_index] == p[j_]:
                str_index+=1
                j_+=1
            else:
                if p[j_] == ".":
                    str_index+=1
                if p[j_] == "*":
                    if p[j_-1]==".":
                        _char=s[str_index-1]
                    else:
                        _char = p[j_-1]
                    for k in range(str_index, len(s)):
                        if s[k]!=_char:
                            break
                        str_index+=1
                if p[j_].isalpha()==1:
                    #handle for alpha neding and nit
                    return False
                j_+=1
        if traversed==True:
            ei_p=len(p)-1
            ei_s=len(s)-1

            while(ei_p>j_ and ei_s>=0 ):
                if p[ei_p]!=s[ei_s]:
                    return False
                else:
                    ei_p-=1
                    ei_s-=1
            return True
        if (str_index)==len(s):
            return True
        else:
            return False


if __name__=="__main__":
    s=Solution()
    print(s.isMatch("aab", "c*a*b"))