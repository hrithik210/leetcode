class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_map = {}
        res= []
        n = len(nums)

        for i in nums:
            if i in count_map:
                count_map[i]+=1
            else:
                count_map[i] = 1
        
        for num,count in count_map.items():
            if count > n/3:
                res.append(num) 
        return res
        