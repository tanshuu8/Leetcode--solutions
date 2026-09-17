class Solution(object):
    def majorityElement(self, nums):
        n= len(nums)
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        ans =[]
        for key in freq:
            if freq[key]>n//3:
                ans.append(key)
        return ans
            
            
       
        
                
        
        