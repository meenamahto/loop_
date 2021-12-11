string=input("Enter your name:")
i=0
while i<len(string):
    a=string.upper()
    b=string.lower()
    j=0
    while j<=i:
        print(a[i],end="")
        break
        j=j+1
    k=0
    while k<=i:
        print(b[i],end="")
        k=k+1
    u=0
    while u<=i:
        print("-",end="")
        u=u+1
    print()
    i=i+1
