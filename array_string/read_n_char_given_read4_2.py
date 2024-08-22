# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

"""
we have a file to read from a read4 api, with the list of 
since read can be called multiple times, we will have to keep track of query in the class
- For every query, we will have to skip the previous count
"""
from collections import deque
from typing import List

def read4(buff):
    pass

class Solution:
    def __init__(self):
        self.count = 0
        self.queue = deque()

    def read(self, buf: List[str], n: int) -> int:
        self.count = 0
        temp_buffer = [''] * 4
        remain_read_count = len(self.queue)
        if remain_read_count > 0:
            min_remain_read = min(n, remain_read_count)
            i = 0
            while i < min_remain_read:
                val = self.queue.popleft()
                buf[self.count + i] = val
                i += 1

            n -= min_remain_read
            self.count += min_remain_read

        while n > 0:
            read_count = read4(temp_buffer)
            min_count = min(n, read_count)
            buf[self.count: self.count + min_count] = temp_buffer[:min_count]
            self.count += min_count
            n -= min_count
            while min_count < read_count:
                self.queue.append(temp_buffer[min_count])
                min_count += 1
            if read_count == 0:
                break

        buf = buf[:self.count]
        return self.count