class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
         # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Return the kth largest element
        return nums[-k]
                