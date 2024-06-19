class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # select element in decision tree
            curr.append(candidates[i])
            helper(i, curr, total + candidates[i])

            # not selecting element in decision tree
            curr.pop()
            helper(i + 1, curr, total)

        helper(0, [], 0)
        return res
        