"""
find the longest substring with at most K distinct element:
idea
2 pointers, left and right, right move pointers one at a time
- set to hold K distinct elements
- Counter to hold K distinct count
left, right pointers
while right < len():
  if len(set) == K:
    if [item] in set:
        increment count
    else:
        while left most item in counter > 0:
            derement count
            if count == 0:
                remove from set
        add new item
        add that to set
        increment count
        compare right - left + 1 and max
  else:
    add to the set
    increment the count

eceba
  l
   r
ccaabbb
  l
      r

"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        sub_set = set()
        count = {}
        left = right = max_sub_string = 0
        while right < len(s):
            if len(sub_set) == k:
                if s[right] in sub_set:
                    count[s[right]] += 1
                else:
                    sub_set.add(s[right])
                    count[s[right]] = 1
                    item_to_remove = s[left]
                    while count[item_to_remove] > 0:
                        count[s[left]] -= 1
                        if count[s[left]] == 0:
                            sub_set.remove(s[left])
                            left += 1
                            break
                        left += 1
                max_sub_string = max(max_sub_string , right - left + 1)
            else:
                sub_set.add(s[right])
                count[s[right]] = 1
                max_sub_string = max(max_sub_string , right - left + 1)

            right += 1

        return max_sub_string