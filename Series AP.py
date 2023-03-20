class Solution:
    def nthTermOfAP(self,A1,A2,N):
        #code here
        d=A2-A1
        return(A1+((N-1)*d))