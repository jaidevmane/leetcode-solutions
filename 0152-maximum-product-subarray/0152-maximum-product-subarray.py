class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            tempCurrMax = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tempCurrMax, currMin * n, n)
            res = max(res, currMax)
        return res

        