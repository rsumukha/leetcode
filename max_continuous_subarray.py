#DOESNT WORK, TAKE GLOBAL VAR and TRY
class Solution(object):
    def maxSubArray(self, nums):
        max=0
        flag=True
        for i in range(0,len(nums)):
            if flag==True:
                if nums[i]+max>gmax:
                    max=nums[i]+max
                else:
                    flag=False
            else:
                if nums[i]>max:
                    max=nums[i]
                    flag=True
        return max




if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))