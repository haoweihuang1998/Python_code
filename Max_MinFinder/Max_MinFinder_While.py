
#Max
#Min
#Swap

#For to while

NumberList = [2,5,33,4,1,66]
Max_index = 0
Min_index = 0
x=len(NumberList)
for index in range(x-1):
        if NumberList[index] < NumberList[index+1]:
                Max_index = index+1
        if NumberList[index]>NumberList[index+1]:
                Min_index=index+1
				
print("Max index is: "+str(Max_index)+" value is: "+str(NumberList[Max_index]))
print("Min index is: "+str(Min_index)+" value is: "+str(NumberList[Min_index]))
