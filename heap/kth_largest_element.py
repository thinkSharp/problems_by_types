"""
find the kth largest element in a list
example: [3,2,4,5,1,2] k = 2
return 4

Solution approach:
use heap to find the kth largest element
we can use min heap to store the k elements in it
return top which would be the smallest of all k

Time complexity(nlogk) for heapifying the original n elements
Space complexity O(k)
"""
import heapq
import unittest
from typing import List
class Solution:
    def kthLargestElement(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
        return heap[0]
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.kthLargestElement([2,3,1,4,7], k = 2), 4)
        self.assertEqual(self.sol.kthLargestElement([1,2], k=1), 2)

if __name__ == '__main__':
    unittest.main()