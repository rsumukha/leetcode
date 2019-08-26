class Solution(object):
    def subarraySum(self, nums, k):
        # count=0
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i, len(nums)):
        #         # print(i, j)
        #         sum+=nums[j]
        #         if sum==k:
        #             count+=1

        # return count
        count=0
        s=0
        d={}
        for n in nums:
            print(n)
            s+=n
            if s-k in d:
                count=count+d[s-k]
            if s==k:
                count+=1            
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        return count

if __name__=="__main__":
    s=Solution()
    print(s.subarraySum([1,1,1], 2))