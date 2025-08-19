class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(start, end):
            # Check if s[start:end+1] is a palindrome
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(start, curr_partition):
            # Base case: if we've processed the entire string
            if start >= len(s):
                result.append(curr_partition[:])
                return
            
            # Try all possible substrings starting from 'start'
            for end in range(start, len(s)):
                # If substring s[start:end+1] is a palindrome
                if is_palindrome(start, end):
                    curr_partition.append(s[start:end + 1])
                    backtrack(end + 1, curr_partition)
                    curr_partition.pop()  # Backtrack
        
        backtrack(0, [])
        return result
