class Solution:
    def MissingNumber(self,array,n):
        tot=0
        # we find the sum of all numbers upto n
        for item in range(n+1):tot+=item

        #the difference between the sum upto n and sum of all elements of array is the missing no
        return (tot-sum(array))