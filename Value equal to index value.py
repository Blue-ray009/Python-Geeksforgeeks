class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		b=[]
		for i in range(1,n+1):
		    if i==arr[i-1]:
		        b.append(i)
		return(b)