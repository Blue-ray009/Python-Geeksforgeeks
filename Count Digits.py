class Solution:
    def evenlyDivides (self, N):
        cou=0
        li=list(str(N))
        bi=[]
        for item in li:
            if int(item)!=0:
                bi.append(item)
        for item in bi:
            if N%int(item)==0:cou+=1
            else:cou+=0
        return(cou)