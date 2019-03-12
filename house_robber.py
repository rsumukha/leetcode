class Solution(object):
    def rob(self, nums):
        if len(nums)==0:
            return 0

        ans=[0]*len(arr)
        ans[0]=nums[0]
        ans[1]=nums[1]
        max=0
        for i in range(2,len(arr)):
            ans[i]=arr[i]+ans[i-2]
            if ans[i]>max:
                max=ans[i]
        return max




if __name__ == "__main__":
    s = Solution()
    print(s.rob([1,2,3,1]))