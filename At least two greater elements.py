class Solution:
    def findElements(self,a, n):
        # Your code goes here
        a.sort()
        a.remove(max(a))
        a.remove(max(a))
        return(a)