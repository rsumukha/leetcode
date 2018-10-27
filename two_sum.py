def twoSum(nums, target):
	out=[]
	for i in range(0, len(nums)-1):
		for j in range(i+1, len(nums)):
			if nums[i]+nums[j]==target:
				return[i,j]


x=twoSum([2,5,5,11], 10)
print(x)

