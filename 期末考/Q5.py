list1=[2,2,3,3,4,4,53,4,5,2]
list1.sort()
list2=[]
for i in range(len(list1)-1):
    if int(list1[i])==int(list1[i+1]):
        list1[i+1]=list1[i]
    elif int(list1[i])!=int(list1[i+1]):
        list2.append(list1[i])
    if len(list1)-3<i<len(list1):
        if int(list1[len(list1)-1])>int(list1[len(list1)-2]):
            list2.append(list1[len(list1)-1])
    else:
       pass
print(list2)
