class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        perf = 1
        for i in range(len(nums)):
            res[i] = perf
            perf *= nums[i]
        
        postf = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postf
            postf *= nums[i]
        return res 