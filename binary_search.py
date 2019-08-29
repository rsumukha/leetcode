def binary_search(nums, target):
	l=0
	r=len(nums)-1

	while l<r:
		mid=int((l+r)/2)
		if nums[mid]==target:
			return mid

		if target<=nums[mid]:
			r=mid
		elif target>nums[mid]:
			l=mid+1
	return None

