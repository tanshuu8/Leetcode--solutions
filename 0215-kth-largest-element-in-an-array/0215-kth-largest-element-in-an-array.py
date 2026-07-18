class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        ans=nums[-k]
        return ans
        
        