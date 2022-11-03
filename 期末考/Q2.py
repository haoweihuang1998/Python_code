def FindintAns(a,b,Limit):
    IntAnsList=[]
    a=int(a)
    b=int(b)
    for x in range(Limit+1):
        for y in range(Limit+1):
            if a*x+b*y==0:
                if x>0:
                    IntAnsList.append("["+str(x)+","+str(y)+"]")
  
                    
    return IntAnsList
print(FindintAns(3,-4,10))
