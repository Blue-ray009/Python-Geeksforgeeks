class Solution:
    def sumOfDigits (self, N):
        # code here
        s=str(N)
        tot=0
        for i in s:tot+=int(i)
        return(tot)