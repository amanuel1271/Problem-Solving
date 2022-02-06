class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(remain, comb, start):
            if remain == 0:
                results.append(comb[:])
                return
            elif remain < 0:
                return

            i,lenn = start,len(candidates)
            while i < lenn:
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i+1)
                comb.pop()
                i += 1
                while i < lenn and candidates[i] == candidates[i-1]:
                    i += 1

        backtrack(target, [], 0)

        return results
