# Built in functions
'''
print()
len()
type()
max()
min()
sum()
int()
float()
set()
tuple()
input()
'''
# user defined functions 

# types of arguments 

# positional args 
def ps_args_func(a,b,c):
    return a,b,c


print(ps_args_func(3000,2000,1000))


# keyword args
def ps_args_func(x,y):
    return x,y

print(ps_args_func(y=3000,x=2000))



# default args 
def ps_args_func(y=3000,x=2000):
    return x,y

print(ps_args_func(4000,5000))


# variable length args / arbitary args #  (tuple )

def func(*args):
    return args

print(func(1,2,3,4,5,6,6,7,7,88,8,88,9))

def func(**kwargs):
    return kwargs

print(func(a=10,b=30,c=56,d=89,name="sairam",address="south end park"))



# Difference between Return and Print 

# print() : displays the output , returns None
# does not send any value to the caller 
# can not reuse the printed output 


# Return : sends the value to the caller
# end of the function (it is the last line in the function )
# returned value can be stored , reused , modified 
def addition():
    a=10
    b=20
    c=a+b
    return c

add1= addition()
print(add1)

print(add1 + 50)


# Recursion  : function calling itself 

# factorial : 5! = 5*4*3*2*1

# base condition 
# recursive case 


def factorial(n):
    if n == 1:
        return 1

    return n*factorial(n-1)

print(factorial(5))


'''
    if n==1

    n! = n*(n-1)*(n-2)*(n-3)*......*1 recusive logic 
    
'''







