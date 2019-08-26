def twoSum(nums, target):
    # out=[]
    # for i in range(0, len(nums)-1):
    #   for j in range(i+1, len(nums)):
    #       if nums[i]+nums[j]==target:
    #           return[i,j]
   
    res=[]
    nums.sort()
    left=0
    right=len(nums)-1
    
    while left<right:
        # print(left, right)
        if (nums[left]+nums[right])==target:
            return [left, right]
        elif nums[left]+nums[right]>target:
            right-=1
        else:
            left+=1
    return None


x=twoSum([2,7,11,15],9)
print(x)

