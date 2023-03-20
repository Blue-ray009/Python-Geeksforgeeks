class Solution:
    def find_median(self, v):
        # Code here
        v.sort()
        x = len(v)
        if x % 2 == 0:
            a = v[(x - 1) // 2]
            b = v[(x + 1) // 2]
            return ((a + b) // 2)
        else:
            return (v[(x - 1) // 2])
