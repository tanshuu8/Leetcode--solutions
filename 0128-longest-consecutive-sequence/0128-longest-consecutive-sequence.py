class Solution(object):
    def longestConsecutive(self, nums):
        #in this problem take numset =set(nums)
        longest =0
        numset =set(nums)
        for nums in numset:
            if nums-1 not in numset:
                length =1
                while length + nums in numset:
                    length+=1
                longest = max(longest,length)
        return longest
       
            

        
        
        
       