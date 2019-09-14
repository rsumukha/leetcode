class Solution(object):
    def threeSum(self, nums):
        if len(nums)<3:
            return None
        if len(nums)==3:
            if nums[0]+nums[1]+nums[2]==0:
                return [nums]
            else:
                return None
        nums.sort()
        ans=[]
        # print(nums)
        # for i in range(len(nums)-2):
        i=0
        # moved=False
        while i<len(nums)-2:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j=i+1
            k=len(nums)-1
            
            while j<k:
                print(i,j,k)

                sum__=nums[i]+nums[j]+nums[k]
                if sum__>0:
                    k-=1
                elif sum__<0:
                    j+=1
                
                elif sum__==0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
            i+=1
                    
            
        return ans


if __name__=="__main__":
    s=Solution()
    print(s.threeSum([1,-1,-1,0]))# -1 -1 0 1