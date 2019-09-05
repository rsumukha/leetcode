class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums)==0:
            return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_array=[1]*(len(nums)+1)
        dp_array[0]=1

        for i in range(1, len(nums)):
            print(dp_array)
            for j in range(0, i+1):
                if nums[j]<nums[i]:
                    dp_array[i]=max(dp_array[j]+1, dp_array[i])
        return max(dp_array)



    #     lis_global=0
    #     lis_local_array=[0]*len(nums)
    #     # lis_local[0]=1

    #     for i, num in enumerate(nums):
    #         lis_local = self.findLISlocal(nums, num, lis_local_array, i)
    #         print(lis_local_array, lis_local, i , num)

    #         if lis_local!= -1:
    #             lis_local_array[i]=lis_local + 1
    #         else:
    #             lis_local_array[i]=1
    #         lis_global=max(lis_local_array[i], lis_global)

    #     return lis_global

    # def findLISlocal(self, nums, number, lis_local_array, index):
    #     if index==0:
    #         return -1
    #     # print("nums")
    #     # print(nums)
    #     return_lis_local=float("-inf")
    #     set=False
    #     for i in range(index, -1, -1):
    #         if nums[i]<number:
    #             return_lis_local=max(lis_local_array[i], return_lis_local)
    #             set=True
    #     if set==False:
    #         return -1
    #     return return_lis_local

        
        


if __name__=="__main__":
    s=Solution()

    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print("end")