class Solution:
    def productExceptSelf(self, nums):
        left_product=[]
        right_product=[]
        i=1
        j=len(nums)-2
        left_product.append(1)
        right_product.append(1)

        while i<len(nums):
        	# print(i,j)
        	left_product.append(left_product[i-1]*nums[i-1])
        	right_product.append(right_product[i-1]*nums[j+1])
        	i+=1
        	j-=1
        result=[]
        for i in range(len(nums)):
        	result.append(left_product[i]*right_product[len(nums)-1-i])
        # print(left_product, right_product)
        return result


if __name__=="__main__":
	s=Solution()
	print(s.productExceptSelf([2,3,4]))
