"""
for a given course schedule, find if all courses can be taken:
example:
numCourses = 2, prerequisites = [[1,0]] => this case we can take 
numCourses = 2, prerequisites = [[1,0],[0,1]] => this case we can not take

calculate indegree source to increment destination
in the eample one souece = 0, destination = 1 because in order to take 1, you must finish 0

solution approach:
create adjastent graph and indegree then
add all zeros indegree in the queue
popleft and start reducing all the indegree for neighbor, 
if pop count is same as number of course, return true
"""
from collections import defaultdict, deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for dest, source in prerequisites:
            graph[source].append(dest)
            indegree[dest] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        course_taken = 0
        while queue:
            course = queue.popleft()
            course_taken += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return course_taken == numCourses
    