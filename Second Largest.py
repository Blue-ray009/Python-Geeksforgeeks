class Solution:

	def print2largest(self,arr, n):
		# code here
        arr_set=set(arr)
        arr_list=list(arr_set)
        arr_list.sort()
        arr_list.reverse()
        if len(arr_list)>1:return(arr_list[1])
        else:return(-1)