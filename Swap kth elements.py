class Solution:

    def swapKth(self, arr, n, k):

    # code here
    temp = arr[-k]
    arr[-k] = arr[k - 1]
    arr[k - 1] = temp
    return