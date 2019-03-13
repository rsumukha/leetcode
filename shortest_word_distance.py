class Solution():
    def shortWordDist(self, arr, w1, w2):
        ptr1=-1
        ptr2=-1
        min=9999
        for i in range(0,len(arr)):
            if arr[i]==w1:
                ptr1=i
                if ptr2!=-1:
                    if min>abs(ptr1-ptr2):
                        min=abs(ptr1-ptr2)
            elif arr[i]==w2:
                ptr2=i
                if ptr1!=-1:
                    if min> abs(ptr2-ptr1):
                        min=abs(ptr2-ptr1)

        return min


if __name__=="__main__":
    s=Solution()
    print(s.shortWordDist(["aa", "ab", "cc", "aa", "cc"], "aa", "cc"))