class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        #Your code here
        if X in arr:return(arr.index(X))
        else:return(-1)