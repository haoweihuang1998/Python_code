count=0
a=1
b=2
stair=30
def ww(a,b):
    v=1
    f=1
    g=1
    for i in range(a+b):
        g=g*(a+b-i)
    for i in range(b):
        v=v*(b-i)
    for i in range(a):
        f=f*(a-i)
    e=v*f
    m=g/e
    return m
for x in range(int(stair/a)+1):
    for y in range(int(stair/b)+1):
        if (a*x+b*y)==stair:
            if x==0:
                count=count+1
            elif y==0:
                count=count+1
            elif x<=y:
                v=ww(x,y)
                count=count+v
            else:
                v=ww(y,x)
                count=count+v
            
print(int(count))
                
                
                
