"""
Example: 'abcbbadcfadec' => 'abc'
                  l
                      r
"""
class Solutioin:
    def lengthOflongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_len = 0
        left = right = 0
        sub_set = {}

        while right < len(s):
            if s[right] in sub_set:
                if (right - left) > max_len:
                    max_len = right - left
                last_pos = sub_set[s[right]]
                while left <= last_pos:
                    sub_set.pop(s[left])
                    left += 1
            else:
                sub_set[s[right]] = right
                right += 1

        if (right - left) > max_len:
            max_len = right - left
        
        return max_len


if __name__ == '__main__':
    sol = Solutioin()

    assert(sol.lengthOflongestSubstring(' ')) == 1 
    assert(sol.lengthOflongestSubstring('abcbacdcaa')) == 4
    assert(sol.lengthOflongestSubstring('abcbbadcfadec')) == 5