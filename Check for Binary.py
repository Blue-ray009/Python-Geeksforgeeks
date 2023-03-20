def isBinary(str):
    #code here
    count=0
    for item in str:
        if int(item)==0 or int(item)==1:count+=1
        else:count+=0
    if count==len(str):return(True)
    else:return(False)