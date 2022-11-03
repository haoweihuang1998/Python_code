blood_pressure = [165, 109, 175, 110, 193, 140, 130, 180, 158, 120, 116, 99, 169, 119, 119, 136, 125, 147]
a=0
blood_pressure.sort()
print("Min = " + str(blood_pressure[0]))
print("Max = " + str(blood_pressure[-1]))
print("Median  = " + str(blood_pressure[int(len(blood_pressure)/2)]))
for i in range(len(blood_pressure)):
    a=int(blood_pressure[i])+a
    b=int(a)/int(len(blood_pressure))
print("Average = " + str(b))
