class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        bucket = [[]for i in range(len(nums)+1)]
        for num in freq:
            count = freq[num]
            bucket[count].append(num)
        ans =[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
            

       
       