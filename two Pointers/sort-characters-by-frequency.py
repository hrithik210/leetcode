class Solution:
    def frequencySort(self, s: str) -> str:
        count  = {}
        bucket = defaultdict(list)
        res = []

        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char] = 1

        for char,count in count.items():
            bucket[count].append(char)
    
        for i in range(len(s) ,0 ,-1):
            for c in bucket[i]:
                res += c*i
        return "".join(res)