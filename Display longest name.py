class Solution:
    def longest(self, names, n):
    	# code here
    	length=[]
    	for item in names:
    	    x=len(item)
    	    length.append(x)
    	y=length.index(max(length))
    	return(names[y])