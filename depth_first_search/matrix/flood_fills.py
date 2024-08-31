"""
flood fill changes the color of the images by cell

change all the cell colors which are same as starting color
"""
from collections import deque
class Solution:
    def flood_fill(self, image, sr, sc, color):
        if color == image[sr][sc]:
            return image
        rows, cols = len(image), len(image[0])
        queue = deque((sr, sc))
        visited = set()
        orginal_color = image[sr][sc]
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            visited.add((r, c))
            for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited \
                and image[nr][nc] == orginal_color:
                    queue.append((nr, nc))
        return image