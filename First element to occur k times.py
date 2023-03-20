class Solution:
    def firstElementKTime(self,  a, n, k):
        # code here
        coun={}
        for i in a:
            if i in coun:
                coun[i]+=1
                if coun[i]>=k:return(i)
            else:
                coun[i]=1
                if coun[i]>=k:return(i)
        return(-1)