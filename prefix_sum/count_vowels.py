class Solution:
    def vowelStrings(self, word: str, queries: list[list[int]]):
        # Your code goes here
        vowels = set({'a', 'e', 'i', 'o','u','A','E','I','O','U'})
        prefix = [0] * (len(word) + 1)
        for i in range(1, len(word) + 1):
            if word[i - 1] in vowels:
                prefix[i] += 1
            prefix[i] += prefix[i - 1]
            
        result = []
        for q in queries:
            result.append(prefix[q[1] + 1] - prefix[q[0]])
        return result
    

if __name__ == '__main__':
    sol = Solution()
    sol.vowelStrings('aba', [[0,1],[0,2]])

"""
Time complexity O(n * q) n is the len of word and q is no. of query
"""