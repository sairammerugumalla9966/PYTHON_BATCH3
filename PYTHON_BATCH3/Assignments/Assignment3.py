num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\nFirst Number:", num1)
print("Second Number:", num2)
print("\nAddition (+):", num1 + num2)
print("Subtraction (-):", num1 - num2)
print("Multiplication (*):", num1 * num2)
print("Division (/):", num1 / num2)
print("Floor Division (//):", num1 // num2)
print("Modulus (%):", num1 % num2)
print("Exponent (**):", num1 ** num2)



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\nFirst Number:", num1)
print("Second Number:", num2)
print("\nnum1 == num2 :", num1 == num2)   
print("num1 != num2 :", num1 != num2)    
print("num1 > num2  :", num1 > num2)     
print("num1 < num2  :", num1 < num2)     
print("num1 >= num2 :", num1 >= num2)    
print("num1 <= num2 :", num1 <= num2)



#Logical AND : 
Returns True only if both conditions are True.
#Truth Table:
A	     B	    A and B
True	True	True
True	False	False
False	True	False
False	False	False
#Logical OR :
Returns True if at least one condition is True.
#Truth Table:
A	     B	    A or B
True	True	True
True	False	True
False	True	True
False	False	False
#Logical NOT :
Reverses the result.
#Truth Table:
A	not A
True	False
False	True
#Example : 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Logical AND (a > 0 and b > 0):", a > 0 and b > 0)
print("Logical OR (a > 0 or b > 0):", a > 0 or b > 0)
print("Logical NOT (not(a > 0)):", not(a > 0))



num = int(input("Enter a Number:"))
if num > 10 and num < 50:
   print("The Number lies between 10 and 50")
else:
   print("The Number does NOT lies between 10 and 50")



x = 10
print("Initial value of x:", x)
# = 
x = 20
print("After x = 20:", x)
# += 
x += 10      
print("After x += 10:", x)
# -= 
x -= 5     
print("After x -= 5:", x)
# *= 
x *= 2      
print("After x *= 2:", x)
# /=
x /= 4      
print("After x /= 4:", x)



numbers = [10, 20, 30, 40, 50]
value = int(input("Enter a number to search: "))
if value in numbers:
    print("Value exists in the list")
else:
    print("Value does not exist in the list")



x = 100
y = 100
print("With integers:")
print("Using == :", x == y)
print("Using is :", x is y)



num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")



length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("Area of the rectangle is:", area)



result1 = 20 + 10 * 2
result2 = (20 + 10) * 2
result3 = 20 + 10 * 2 ** 2
print("Result without parentheses (10 + 5 * 2):", result1)
print("Result with parentheses ((10 + 5) * 2):", result2)
print("Result with exponent (10 + 5 * 2 ** 2):", result3)









