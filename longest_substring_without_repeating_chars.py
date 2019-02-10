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

if __name__=="__main__":
    long_sub=Solution()
    print(long_sub.lengthOfLongestSubstring(" "))