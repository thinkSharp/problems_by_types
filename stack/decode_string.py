"""
For decoding a string
we will utilize a stack:
we will append everything until closing bracket
then pop until opening bracket and have all the items append together to form a string
multiply the int value pop from the stack.
add that back in the stack and continue till the end of the string
if end of string return stack -1

time complexity O(n)
space complexity O(n)
'3[a]2[bc]'

"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                items  = []
                while stack:
                    if stack[-1] == '[':
                        word = ''.join(items[::-1])
                        stack.pop()
                        if stack[-1].isdigit():
                            word = word * int(stack.pop())
                            stack.append(word)
                            break
                    else:
                        items.append(stack.pop())
            else:
                stack.append(char)
        return ''.join(stack)
    
import unittest
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.decodeString('3[a]'), 'aaa')
        self.assertEqual(self.sol.decodeString('2[abc]3[cd]ef'), 'abcabccdcdcdef')
        self.assertEqual(self.sol.decodeString('3[a2[c]]'), 'accaccacc')


if __name__ == '__main__':
    unittest.main()
