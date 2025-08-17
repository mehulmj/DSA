#leetcode - https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort for consistent order
        
        def backtrack(remain, curr_comb, start):
            # Base case: if sum equals target
            if remain == 0:
                result.append(curr_comb[:])  # Deep copy only when adding to result
                return
            # If sum exceeds target, stop
            if remain < 0:
                return
            
            # Try each candidate from start index
            for i in range(start, len(candidates)):
                curr_comb.append(candidates[i])  # Include candidate
                backtrack(remain - candidates[i], curr_comb, i)  # Allow same candidate
                curr_comb.pop()  # Backtrack
                
        backtrack(target, [], 0)
        return result
