"""
merge k sorted list can be done multiple ways
simply take 2 lists at a time and merge them
until one list remain
time complexity O(n * m) n is no. of list, m is number of element

or we can use heap as well
push all the values in the heap
then pop them all again and 
"""
import heapq
class Solution:
    def mergeKListsHeap(self, lists: list[list[int]]) -> list[int]:
        heap = []
        for l in lists:
            for num in l:
                heapq.heappush(heap, num)
        return [heapq.heappo(heap) for _ in range(len(heap))]
    
    def merge2Lists(self, l1: list[int], l2: list[int]) -> list[int]:
        if not l2:
            return l1
        if not l1:
            return l2
    
        i, j = 0, 0
        result = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        if i > j:
            result.extend(l1[i:])
        else:
            result.extend(l2[j:])

        return result

    def mergeKLists(self, lists: list[list[int]]):
        # Your code goes here
        if not lists:
            return []
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 <= len(lists) -1 else None
                temp.append(self.merge2Lists(l1, l2))
            lists = temp
        return lists[0]