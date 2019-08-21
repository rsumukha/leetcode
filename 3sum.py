class Solution(object):
    def threeSum(self, nums):
        if len(nums)<3:
            return None
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            print(i)
            j=i+1
            k=len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k]==0:
                    print(i, j, k)
                    ans.append([nums[i], nums[j], nums[k]])
                while nums[j]==nums[j+1] and j<k and j<len(nums)-1:
                    print(j, k)
                    j+=1
                while nums[k]==nums[k-1] and j<k :
                    k-=1
                while nums[i]+nums[j]+nums[k]<0 and j<k:
                    j+=1
                while nums[i]+nums[j]+nums[k]>0 and j<k:
                    k-=1
                j+=1
                k-=1
            while nums[i]==nums[i+1] and i < len(nums)-1:
                print("a")
                i += 1
            print(i)

        return ans



if __name__=="__main__":
    s=Solution()
    print(s.threeSum([0,0,0,0]))