class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        lis_global=0
        lis_local_array=[0]*len(nums)
        # lis_local[0]=1

        for i, num in enumerate(nums):
            lis_local = self.findLISlocal(nums, num, lis_local_array, i)
            print(lis_local_array, lis_local, i , num)

            if lis_local!= -1:
                lis_local_array[i]=lis_local + 1
            else:
                lis_local_array[i]=1
            lis_global=max(lis_local_array[i], lis_global)

        return lis_global

    def findLISlocal(self, nums, number, lis_local_array, index):
        if index==0:
            return -1
        # print("nums")
        # print(nums)
        return_lis_local=float("-inf")
        set=False
        for i in range(index, -1, -1):
            if nums[i]<number:
                return_lis_local=max(lis_local_array[i], return_lis_local)
                set=True
        if set==False:
            return -1
        return return_lis_local

        
        


if __name__=="__main__":
    s=Solution()

    print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
    print("end")