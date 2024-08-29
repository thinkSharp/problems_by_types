"""
finding the k cloest element to target
formula for cloest: absolute distance between target and i
We can use heap for store k elements
since we need to get min values, we will be saving -distance 
"""
import heapq

class Solution:
    def kCloestElementToTarget(self, nums: list[int], k: int, target: int) -> list[int]:
        if not nums:
            return []
        
        heap = []
        for i in range(len(nums)):
            distance = abs(target - nums[i])
            if len(heap) < k:
                heapq.heappush(heap, [-distance, nums[i]])
            elif distance < -heap[0][0]:
                heapq.heappushpop(heap, [-distance, nums[i]])

        result = [p[1] for p in heap]
        result.sort()

        return result
    

if __name__ == '__main__':
    sol = Solution()

    val = sol.kCloestElementToTarget([-1, 0, 1, 4, 6], 3, 1)
    print (val)

    val = sol.kCloestElementToTarget([5, 6, 7, 8, 9], 2, 10)
    print(val)

