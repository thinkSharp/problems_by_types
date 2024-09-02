"""
return a list of all unique combination of sum to a given target from numbers using the nums list

uing the back tracking, sum list can be generated
based condintion is remaining target == 0, if remaining target < 0 or index out of bound then stop

two recursive call
call on same index
call on new index
"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        result = []

        def backtrack(sums, index, remaining_target):
            if remaining_target == 0:
                result.append(sums[:])
                return
            sums.append(candidates[index])
            backtrack(sums, index, remaining_target - candidates[index])
            sums.pop()
            backtrack(sums, index + 1, remaining_target)
        
        backtrack([], 0, target)
        return result
    