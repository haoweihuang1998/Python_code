#Max
#Min
#Swap

 #can't use list.sort() or sorted()
import random

def numbers_generator(n):
	random.seed()
	numbers = []
	for i in range(0, n):
		a = random.randint(1,100)
		numbers.append(a)
	return numbers
	
#NumberList = [2,5,33,4,1,66]

NumberList = numbers_generator(200)
print(NumberList)

Max_index = 0
Min_index = 0


for index in range(len(NumberList)):#convert to for loop
	if NumberList[index] > NumberList[Max_index]:
		Max_index = index
	if NumberList[index] < NumberList[Min_index]:
		Min_index = index
	
	
print("Max index is: "+str(Max_index)+" value is: "+str(NumberList[Max_index]))
print("Min index is: "+str(Min_index)+" value is: "+str(NumberList[Min_index]))
