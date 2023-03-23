#fibonacci series:

a , b = 0 , 1
term = int(input("Enter the number of term: "))
if term ==1:
 print(0)
elif term ==2:
 print("0\n1")
else:
 print("0\n1")
for i in range(1,term-1):
 c = a+b
 print(c)
 a = b
 b = c
