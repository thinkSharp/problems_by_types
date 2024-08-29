"""
return the k cloest point to origin, [0,0]
formula for closet point to origin (x**2 + y **2)
idea is to use heap to store the K elements in the list
since we want to remove the cloest elements which means minimum elements, 
we use negative value to store in the heap
"""
import heapq
import unittest
class Solution:
    def kCloestPoints(self, points: list[int], k: int) -> list[int]:
        if not points:
            return []
        heap = []

        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            if len(heap) < k:
                heapq.heappush(heap, [-distance, i])
            elif distance < -heap[0][0]:
                heapq.heappushpop(heap, [-distance, i])
        
        return [points[p[1]] for p in heap]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        val = self.sol.kCloestPoints([[3,4],[2,2],[1,1],[0,0],[5,5]], 3)
        print(val)

if __name__ == '__main__':
    unittest.main()