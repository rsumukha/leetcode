class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        global even
        global median_index
        if (len(nums1)+len(nums2))%2 ==0:
        	even=1
        	median_index=(len(nums1)+len(nums2)/2)+0.5
        else:
        	even=0
        	median_index=len(nums1)+len(nums2)/2

        findMedianSortedArrays_(nums1, nums2, 0)
        return median
    
    def findMedianSortedArrays_(self,nums1, nums2,counter):    
        len1=len(nums1)
        len2=len(nums2)

        if counter>= median_index:
        	if nums1[]
        		median= nums1[len1]
        		return 
        	else:
        		median=nums2[len2]
        		return
        if len1>=len2:
        	if nums2[0]>nums1[abs(len1/2)]:
        		return findMedianSortedArrays_(nums2[(len2/2):], nums1, ceil(len1+len2)/2 )
        	else:
        		return findMedianSortedArrays_(nums2[0:(len2/2)], nums1, (len1+len2)/2 )
        else:
        	return findMedianSortedArrays_(nums2, nums1, counter)
        return




obj=Solution()
print(obj.findMedianSortedArrays([1,2], [3,4]))