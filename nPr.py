class Solution:
    def nPr(self, n, r):
        # code here
        tempn=1
        tempnr=1
        for i in range(1,n+1):
            tempn*=i
        for i in range(1,(n-r+1)):
            tempnr*=i
        return(tempn//tempnr)