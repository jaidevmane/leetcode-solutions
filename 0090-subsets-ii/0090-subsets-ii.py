class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            # decision tree to select the element
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # decision tree - to not select the element while preventing duplicates in the subsets
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res

        