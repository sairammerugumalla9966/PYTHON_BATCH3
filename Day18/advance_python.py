# advance python 

# iterators 

# __iter__() --> go through each and every element 

# __next__() ---> go to next value 
'''
l=[1,2,3,4,5]
p=iter(l)

print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))



name="sairam"

n=iter(name)

print(next(n))
print(next(n))
'''
# generators 
 
# generator is a function which returns the iterator and used yield instead of return 

def even_num(n):
    for i in range(n):
        if i%2 == 0:
            yield i

gen=even_num(10)

for x in gen:
    print(x)


'''
# decorators

def my_decorator(func):

    def display():
        print("before function")
        func()
        print("after function")

    return display
    
@my_decorator
def say_hello():
    print("hello")
    print("decorator implemented ")
    def new_func():
        print("second decorator")
    new_func()


say_hello()

# decorators with arguments 

def my_decorator(func):

    def display(name):
        print("before function",name)
        func(name)
        print("after function",name)

    return display
    
@my_decorator
def say_hello(name):
    print("hello" , name)
    print("decorator implemented ",name)
   

say_hello("sairam")



# regular expression 

# used for pattern matching in strings


import re

text="python is very easy"

print(re.search("java",text))
print(re.sub("python","java",text))


import re

text="db dblite sqldb db dblite sqldb"

print(re.findall("db",text))


'''