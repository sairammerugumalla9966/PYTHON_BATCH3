# Nested loops 
# loop inside another loop 

# outer loop ----> no of rows 
# inner loop ----> no of elements / columns 
'''
for i in range(3):
    for j in range(3):
        print(i,j)

'''
# SQUARE PATTERN 

for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()


# Right angle triangle

for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print()

'''

* * * *
* * *
* *
*

'''

for i in range(5,0,-1):
    for j in range(i):
        print("*", end= " ")
    print()



# multiplication table 
'''
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15 
'''

for i in range(1,5): # rows
    for j in range(1,6):
        print(i*j , end=" ")
    print()

for i in range(1):
    for j in range(1,6):
        print(f"3 * {j} = {3*j}")

