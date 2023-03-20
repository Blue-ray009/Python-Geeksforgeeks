class Solution:
    def convertFive(self,n):
        n_str=str(n)
        x=len(n_str)
        temp="5"
        n_list=list(n_str)
        for i in range(x):
            if int(n_list[i])==0:
               n_list[i] =temp
        N=""
        for item in n_list:N+=item
        n=int(N)
        return(n)