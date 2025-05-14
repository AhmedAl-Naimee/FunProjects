
#Implement a basic calculator that can take 2 
# numbers as input and do the following operations: +  -  *  /  mod (%)  pow()  abs()

num1 = int(input())
num2 = int(input())

add = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
abss = abs(num1)
poww = pow(num1,num2)

print("addition = ", add)
print("subtruction = ", sub)
print("multiplication = ", mult)
print("division = ", div)
print(f"mod of {num1} and {num2} = ", mod)
print(f"absolute of {num1} = ", abss)
print(f"{num1} power of {num2} = ", poww)

