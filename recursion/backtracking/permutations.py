class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(curr_perm, used):
            print(curr_perm)
            # Base case: if permutation is complete
            if len(curr_perm) == len(nums):
                result.append(curr_perm[:])
                return
            
            # Try each number that hasn't been used yet
            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    curr_perm.append(nums[i])
                    backtrack(curr_perm, used)
                    curr_perm.pop()
                    used.remove(i)
        
        backtrack([], set())
        return result
