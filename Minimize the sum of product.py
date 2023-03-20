class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        a.sort()
        b.sort()
        b.reverse()
        sum=0
        for i in range(n):
            sum+=a[i]*b[i]
        return(sum)