class Solution:

	def getMoreAndLess(self,arr, n, x):
		# code here
		countmax=0
		countmin=0
		for item in arr:
		    if item<x:countmin+=1
		    elif item>x:countmax+=1
		    elif item==x:
		        countmin+=1
		        countmax+=1
	    return(countmin,countmax)