#1. Develop a Python program to find factorial of given number

number = int(input("Enter the number :"))
ans =1
if number==0:
 print(f"Factorial of {number} is 1")
else:
 for i in range(1,number+1):
  ans=ans*i
 print(f"Factorial of {number} is {ans}")