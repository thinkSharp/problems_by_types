"""
Check if given string has valid parantheses
parentheses are (), {}, []
solution approach:
use stack to save all the open parantheses,
when meet with close parantheses, pop from the stack, if the open and close matches, continue
else return False

Time complexity O(n) n is the lenght of the string
space complexity O(n) n is the open parantheses
"""
class Solution:
    def valid_parentheses(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        mapping = {')':'(', '}': '{', ']': '['}
        for p in s:
            if  p in mapping:
                if not stack or stack[-1] != mapping[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)

        return len(stack) == 0
    

import unittest
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):

        self.assertEqual(self.sol.valid_parentheses('(){({})}'), True)
        self.assertEqual(self.sol.valid_parentheses('({ )'), False)

if __name__ == '__main__':
    unittest.main()



