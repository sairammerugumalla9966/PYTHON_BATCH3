num = int(input("Enter number: "))
for i in range(1, num):
    if num % i == 0:
        print(" not a Prime Number")
    break
else:
    print("  Prime Number")