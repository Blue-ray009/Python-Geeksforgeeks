class Solution:
	def is_palindrome(self, n):
		# Code here
        a=str(n)
        b=a[::-1]
        if a==b:return("Yes")
        else:return("No")