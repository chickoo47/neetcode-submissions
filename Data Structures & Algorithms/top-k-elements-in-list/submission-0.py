class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        f = [[] for i in range(len(nums) + 1)]
        for n in nums:
            c[n] = 1 + c.get(n, 0)
        for n, x in c.items():
            f[x].append(n)
        res = []
        for i in range(len(nums) , 0,-1):
            for n in f[i]:
                res.append(n)
            if len(res) == k:
                return res 
        