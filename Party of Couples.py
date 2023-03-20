class Solution:
    def findSingle(self, N, arr):
        # code here
        brr=[]
        for i in arr:
            brr.append(arr.count(i))
        x=brr.index(1)
        return(arr[x])