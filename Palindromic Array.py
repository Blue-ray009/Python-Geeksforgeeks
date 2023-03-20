def PalinArray(arr ,n):
    # Code here
    count=0
    for item in arr:
        b=str(item)
        x=len(b)
        c=""
        for i in range(x):
            c+=b[x-1-i]
        if b==c:count+=1
        else:count+=0
    if count==n:return(True)
    else:return(False)