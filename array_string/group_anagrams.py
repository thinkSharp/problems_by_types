"""
create a dictionary of frozen set of each letters and value as original string
while looping through the list, 
  - create forzen set,
  - compare with the dictionary and length of the diction with the word
  - if matched add in th list
  - if not create a new entry

  At the end of loop,
  loop through the dictionary, get all the list of anagrams out of it and return output

  Time complexity O(n * len(words))
  Space complexity is O(n * s)

  ['a']
  ['']
  ['eat', 'tea','tan', 'ate','nat', 'bat']

"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            s_word = sorted(word)
            s_word = ''.join(s_word)
            if s_word in map:
                map[s_word].append(word)
            else:
                map[s_word] = [word]
        output = []
        for value in map.values():
            output.append(value)

        return output
    
if __name__ == '__main__':
    sol = Solution()
    assert(sol.groupAnagrams(['a'])) == [['a']]
    assert(sol.groupAnagrams([''])) == [['']]
    print(sol.groupAnagrams(['eat','tea','tan','ate', 'nat', 'bat']))
