"""
solution appraoch:
')()())()'
stack
max_valid
curr_valid
if closing then check the stack
  append in curr_valid
else:
  max_valid = max(max_valid, curr_valid)
  reset the stack

return max_valid

time complexity O(n)
space complexity O(n)

"(()"
    c
")()())()"
        c
"(((("

"()(()()()"
     c
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_count = 0
        stack = [-1]
        for i, char in enumerate(s):
            if char == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_count = max(max_count, i - stack[-1])
                
            else:
                stack.append(i)
        return max_count


import unittest
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.longestValidParentheses('()(()()()(()()'), 6)
        self.assertEqual(self.sol.longestValidParentheses('()(()'), 2)
        self.assertEqual(self.sol.longestValidParentheses('(()'), 2)
        self.assertEqual(self.sol.longestValidParentheses(')()())()'), 4)
        self.assertEqual(self.sol.longestValidParentheses('))))'), 0)
        self.assertEqual(self.sol.longestValidParentheses('(((()())))))))'), 10)


if __name__ == '__main__':
    unittest.main()
