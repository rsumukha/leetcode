class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        ans=[]
        for index in range(len(nums)):
            l=index+1
            r=len(nums)-1
            while(l<r):
                if nums[index]+nums[l]+nums[r]==0:
                    print(index, l, r)
                    ans.append([nums[index], nums[l], nums[r]])
                    while(l<r and nums[l]==nums[l+1]):
                        l+=1
                    while(l<r and nums[r]==nums[r-1]):
                        r-=1
                if nums[index]+nums[l]+nums[r]>0:
                    l+=1
                if nums[index]+nums[l]+nums[r]<0:
                    r-=1
                else:
                    l+=1
                    r-=1

        return ans



if __name__=="__main__":
    s=Solution()
    print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))