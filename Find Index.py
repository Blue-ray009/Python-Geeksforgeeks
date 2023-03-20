class Solution:
    def findIndex(self, a, N, key):
        # code here.
        b = []
        x = len(a)
        for i in range(x):
            if a[i] == key: b.append(i)

        if len(b) >= 1:
            c = [min(b), max(b)]
            return (c)
        else:
            d = [-1, -1]
            return (d)