class Solution:
	def binarysearch(self, arr, n, k):
		# code here
		count=0
        if n%2==0:
            x=(n//2)+1
            if k>=arr[x]:
                for i in range(x,n):
                    if arr[i]==k:return(i)
                    else:count+=1
                if count==n-x:return(-1)
            else:
                for i in range(0,x):
                    if arr[i]==k:return(i)
                    else:count+=1
                if count==x:return(-1)
        else:
            x=n//2
            if k>=arr[x]:
                for i in range(x,n):
                    if arr[i]==k:return(i)
                    else:count+=1
                if count==n-x:return(-1)
            else:
                for i in range(0,x):
                    if arr[i]==k:return(i)
                    else:count+=1
                if count==x:return(-1)