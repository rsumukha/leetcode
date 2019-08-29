import math
class Solution:
    def findMin(self, nums):
        if nums[0]<=nums[len(nums)-1]:
            return nums[0]
        l=0
        r=len(nums)-1
        while l<r:
            mid=math.floor((l+r)/2)
            # print(l, r, mid)
            
            if nums[l]<=nums[r]:
                return nums[l]

            
            elif nums[l]>nums[mid]:
                r=mid
                
            else:
                l=mid+1
                
        return nums[l]



if __name__=="__main__":
    s=Solution()
    print(s.findMin([6,7,8,0,1,3,5]))


# 0, 1, 2, 3, 4, 5, 6