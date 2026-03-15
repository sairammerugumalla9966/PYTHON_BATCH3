x=[1,2,3]
y=x

y.append(4)
print(y)
print(x)


def add(a,b=5):
    return a+b
print(add(3))
print("python"[-2])


x=[1,2,3]
print(x*2)

y=x.copy()
y.append(4)
print(y)



nums=[1,2,3,4]

total_product=1
for num in nums:
    total_product *=num

result=[]

for num in nums:
    result.append(total_product // num)

print(result)














