N = 5
for i in range(1, N + 1):
    print(i)


N = 6
sum_even = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers:", sum_even)


num = 1234
reverse = 0
while num != 0:
    digit = num % 10          
    reverse = reverse * 10 + digit
    num = num // 10   
print("Reverse number:",reverse)


num = 4567
count = 0
while num != 0:
    num = num // 10
    count += 1
print("Number of digits:", count)  


for i in range(1, 11):
    print(5, "x", i, "=", 5 * i)


#without spaces
for i in range(4):
    for j in range(4):
        print("*", end = "")
    print()
#with spaces
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()


# Upper half of diamond
for i in range(1, 6):  
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()  
# Lower half of diamond
for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print() 


num = 1
for i in range(4):          
    for j in range(5):     
        print(num, end=" ")
        num += 1
    print()

