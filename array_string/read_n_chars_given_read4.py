"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file

delcare a temp buffer of size 4
call read4 api, 
check the amount that needs to be read by comparing n with read count. we sould take min value
append the result in buffer
update the running count
if api returns 0 read count
break
"""
def read4(buff):
    pass

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        t_buffer = [''] * 4
        count = 0
        while n >= 0:
            read_count = read4(t_buffer)
            local_read_count = min(n, read_count)
            buf[count: count + local_read_count] = t_buffer[:local_read_count]
            count += local_read_count
            n -= local_read_count
            if local_read_count < 4:
                buf = buf[:count]
                return count
