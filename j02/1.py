def fisa(x,y,z):
    if (x**2)+(y**2)==(z**2) or (x**2) + (z**2) == (y**2) or (y**2) + (z**2) == (x**2):
        print("YES")
    else:
        print("NO")
a=int(input())
b=int(input())
c=int(input())
if 1<=a<=150 and 1<=b<=150 and 1<=c<=150:
    fisa(a,b,c)