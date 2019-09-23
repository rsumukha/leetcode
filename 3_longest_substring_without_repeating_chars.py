class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length=0
        longest_sub=[]
        for character in s:
            if character not in longest_sub:
                longest_sub.append(character)
            else:
                longest_sub=longest_sub[longest_sub.index(character)+1:]
                longest_sub.append(character)
            if len(longest_sub) > max_length:
                max_length = len(longest_sub)
        return max_length

        """ using hashmap
        max_length=0
        mydict={}
        local_length=0
        position=0
        for i, character in enumerate(s):
            if mydict.get(character, -1)==-1:
                mydict[character] = i
                local_length+=1
            else:
                if mydict.get(character)<position:
                    mydict[character]=i
                    local_length+=1
                else:                    
                    position=mydict.get(character)
                    local_length=i-position
                    mydict[character]=i           
            
            max_length=max(max_length, local_length)
        return max_length

        """

if __name__=="__main__":
    long_sub=Solution()
    print(long_sub.lengthOfLongestSubstring(" "))