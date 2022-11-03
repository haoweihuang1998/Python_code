a=input("put in variable n:")
n=int(a)
print(" "*(n-1)+"*")
for i in range(1,n):
    print(" "*(n-i-1)+"*"+" "*((i)*2-1)+"*")
for i in range(n-2,0,-1):
    print(" "*(n-i-1)+"*"+" "*((i)*2-1)+"*")
print(" "*(n-1)+"*")
