class Solution(object):
    def searchRange(self, nums, target):
        def find_first(nums,target):
            l=0
            r=len(nums)-1
            ans=-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    ans = mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return ans
        def find_last(nums,target):
            l=0
            r=len(nums)-1
            ans=-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    ans = mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return ans
        first = find_first(nums,target)
        last = find_last(nums,target)
        return [first,last]

       
        