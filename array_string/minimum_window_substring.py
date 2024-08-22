"""
minumum wondow substring including duplicates
sliding window technique:
ADOBECODEBANC
         L
            R

queue (b:7, a:8, c:9)
set(c, b, a)
len(set) == len(t)
  min(min_lengh, r - l + 1)

afbbdcefabbbdedddfeg
l
        r
    
queue((a,0), (b,2), (b,3),(c,5))
set(a, b,c)
check the length:
    repace the min

"""