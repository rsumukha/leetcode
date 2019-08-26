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
        print(nums)
        # for i in range(len(nums)-2):
        i=0
        # moved=False
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            # print(i,j,k)
            while(j<k):
                f=0
                if nums[i]+nums[j]+nums[k]==0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        f=1
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                        f=1
                        
                    if f:
                        continue
                
                elif j<k and nums[i]+nums[j]+nums[k]<0:
                    j+=1
                    continue
                elif j<k and nums[i]+nums[j]+nums[k]>0:
                    k-=1
                    continue
                if j<k:
                    j+=1
                    k-=1
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return ans
    # def threeSum(self, nums):
    #     res = set()
    #     nums.sort()
        
    #     for i in range(len(nums)-2):
    #         left = i + 1
    #         right = len(nums)-1
            
    #         while left < right:
    #             if nums[i] + nums[left] + nums[right] < 0:
    #                 left += 1
    #             elif nums[i] + nums[left] + nums[right] > 0:
    #                 right -= 1
    #             else:
    #                 res.add((nums[i], nums[left], nums[right]))
    #                 left += 1
    #                 right -= 1
        
    #     return list(res)



if __name__=="__main__":
    s=Solution()
    print(s.threeSum([1,-1,-1,0]))