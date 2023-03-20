class Solution:
    def isDigitSumPalindrome(self,N):
        #code here
        n=str(N)
        sum=0
        for i in n:
            sum+=int(i)
        x=str(sum)
        y=x[::-1]
        if x==y:return(1)
        else:return(0)