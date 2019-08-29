class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        create 3 var- mac, min and global_max
        """
        local_max=nums[0]
        local_min=nums[0]
        global_max=nums[0]

        for i in range(1, len(nums)):
            if nums[i]<0:
                temp=local_max
                local_max=local_min
                local_min=temp

            local_min=min(nums[i], nums[i]*local_min)
            local_max=max(nums[i], nums[i]*local_max)
            global_max=max(global_max, local_max)
        return global_max

if __name__=="__main__":
    s=Solution()
    print(s.maxProduct([-1, 2, 3, -5 ]))