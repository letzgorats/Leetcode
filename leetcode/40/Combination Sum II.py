class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)
        if sum(candidates) < target:
            return []

        def backtracking(idx, curr, curr_sum):

            if curr_sum == target:
                answer.append(curr[:])
                return

            if curr_sum > target:
                return

            for i in range(idx, len(candidates)):
                # 중복 조합 피하기
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                backtracking(i + 1, curr, curr_sum + candidates[i])
                curr.pop()

        answer = []
        backtracking(0, [], 0)

        return answer