class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pm = {}
        for i, n in enumerate(nums):
            d = target - n
            if d in pm:
                return[pm[d], i]
            pm[n] = i