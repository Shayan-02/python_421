a=input()
lst=[]
for i in range(len(a)):
    if a[i] == "=":
        if lst:
            # i=lst.index("=")
            lst.pop()
    else:
        lst.append(a[i])
for _ in lst:
    print(_,end="")
