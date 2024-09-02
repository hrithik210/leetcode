
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr_monotonic = True
        dec_monotonic  = True

        for i in range(1 , len(nums)):
            if (nums[i] > nums[i-1]):
               incr_monotonic = False
            elif nums[i]<nums[i-1]:
               dec_monotonic = False
        
        return incr_monotonic or dec_monotonic