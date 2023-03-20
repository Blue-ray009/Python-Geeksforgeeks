def countOfElements( a, n, x):
    tot=0
    for item in a:
        if item<=x:tot+=1
        else:tot+=0
    return(tot)