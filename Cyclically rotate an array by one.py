def rotate( arr, n):
    tmp=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=tmp
    return(arr)