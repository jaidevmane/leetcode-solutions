class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(curr, i, total):
            if target == total:
                res.append(curr[::])
                return
            if i >= len(candidates) or total > target:
                return

            # select element from the decision tree
            curr.append(candidates[i])
            backtrack(curr, i + 1, total + candidates[i])
            curr.pop()

            # do not select element from the decision tree and also removing duplicates
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            backtrack(curr, i + 1, total)
        backtrack([], 0, 0)
        return res


        