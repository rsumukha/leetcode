class Solution(object):
    def threeSum(self, nums):
        if len(nums)<3:
            return None
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k]==0:
                    ans.append([nums[i], nums[j], nums[k]])
                while j==j+1:
                    j+=1
                while k==k-1:
                    k-=1
                while nums[i]+nums[j]+nums[k]<0 and j<k:
                    j+=1
                while nums[i]+nums[j]+nums[k]>0 and j<k:
                    k-=1
                j+=1
                k-=1


        return ans



if __name__=="__main__":
    s=Solution()
    print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))