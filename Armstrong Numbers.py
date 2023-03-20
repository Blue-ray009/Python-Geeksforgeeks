class Solution:
    def armstrongNumber (ob, n):
        num_str=str(n)
        tot=0
        for i in range(len(num_str)):
            tot+=(int(num_str[i])**3)
        if tot==n:return("Yes")
        else:return("No")
        # code here
