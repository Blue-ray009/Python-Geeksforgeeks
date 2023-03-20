class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        if arr==arr[::-1]:return(True)
        else:return(False)