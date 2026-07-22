a = "sall=am"
lst = []

for i in a:
    if i != "=":
        lst.append(i)
    else:
        lst.pop()
