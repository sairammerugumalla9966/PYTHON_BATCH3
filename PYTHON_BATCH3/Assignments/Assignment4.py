for i in range(1,11):
    print(i)


for i in range(1, 51):
if i % 2 == 0:
       print(i) 
    

n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print("The sum of first n natural numbers is:", sum)  


for i in range(1, 11):
    print(4, "x", i, "=", 4 * i)


num = 4567
count = 0
while num != 0:
    num = num // 10
    count += 1
print("Number of digits:", count)  


num = 1234
reverse = 0
while num != 0:
    digit = num % 10          
    reverse = reverse * 10 + digit
    num = num // 10   
print("Reverse number:",reverse)


for i in range(1,6):      
    for j in range(i):            
        print("*", end=" ")
    print()  


num = 7
if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number") 


#break
for i in range(1, 11):
    if i == 6:
        break
    print(i)
#continue
for i in range(1, 11):
    if i == 6:
        continue
    print(i) 


num = 4
factorial = 1
i = 1
while i <= num:
    factorial = factorial * i
    i += 1
print("Factorial of number is", factorial)
