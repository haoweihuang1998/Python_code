number = 20
temp=0
a = 5
b = 3
s = 0

for n in range(number):
  s=s+a/b
  temp=a
  a=2*a+b
  b=temp+2
print("The sum of first 20 fractions is: " + str(s))
