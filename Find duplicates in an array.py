class Solution:
    def duplicates(self, arr, n):
    	# code here
    	freq={}
    	arr.sort()
    	for elem in arr:
    	    if elem in freq:
    	        freq[elem]+=1
    	    else:freq[elem]=1
        duplicates=[]
        b=[-1]
        for key in freq.keys():
            if freq[key]>1:
                duplicates.append(key)
        duplicates.sort()
        if len(duplicates)>0:return(duplicates)
        else:return(b)
