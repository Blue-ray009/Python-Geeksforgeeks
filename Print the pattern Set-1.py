def printPat(n):
    # Code here
    b = ""
    for i in range(n, 0, -1):
        ci = ""
        for item in range(n, 0, -1):
            ci += (str(item) + " ") * i
        b = b + ci + "$"
    print(b)
