class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            tempCurrMax = n * currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(tempCurrMax, n * currMin, n)
            res = max(res, currMax)
        return res