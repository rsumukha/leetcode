
class Solution(object):
        
    def maxSlidingWindow(self, nums, k):
        if len(nums)==0 or k == 0: return []
        if k==1: return nums
        ans=[]
        queue = collections.deque()
            
        for i in range(0,len(nums)): #WE have to put index caus the queue might shrink 
            while queue and queue[0] <= i - k: queue.popleft()
            while queue and nums[queue[-1]] < nums[i]: queue.pop()
            queue.append(i)
            if (i>=k-1):
                ans.append(nums[queue[0]])     
        return ans
        
    def bruteforce(self, nums, k):
        if len(nums)==0 or k == 0:
            return []
        ans=[]
        for i in range(len(nums)-k+1):
            ans.append( max(nums[i:i+k]) )
        return ans
    
"""
[1,3,1,2,0,5]
3
(deque([]), 1)
(deque([1]), 3)
(deque([3]), 1)
(deque([3, 1]), 2)
(deque([3, 2]), 0)
(deque([3, 2, 0]), 5)
[3,3,3,5]
[3,3,2,5]
"""    

