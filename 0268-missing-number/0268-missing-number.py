class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        total = n*(n+1)//2
        missing = total - sum(nums)
        return missing
        


        

        
        