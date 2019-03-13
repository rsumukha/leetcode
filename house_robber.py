#similar to subset sum where you consider weather we want to include the element or not
#implement by recursion
class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
        ptr1=nums[0]
        ptr2=nums[1]
        for i in range(2, len(nums)):
            flag=i%2
            if flag==0:
                ptr2=max(ptr1, ptr2)
                ptr1=ptr1+nums[i]
            else:
                ptr1=max(ptr2, ptr1)
                ptr2=ptr2+nums[i]
            print(ptr1, ptr2)

        return max(ptr1, ptr2)

if __name__ == "__main__":
    s = Solution()
    print(s.rob([2,7,9,3,1]))