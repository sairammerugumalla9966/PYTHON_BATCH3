# lambda function : a function defined using Lambda keyword in a single line . 


def is_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

print(is_even(16))

# syntax : 

# definition of lambda function ---->   lambda parameters : expression 
  
# calling a lambda function --->  (lambda parameters : expression)(arguments)


(lambda n : print("even") if n%2==0 else print("odd"))(20)

(lambda text : print(text.upper()))("good morning")



# higher order functions 

# function takes another function as an argument 
# function returns another function 


# map()  : applies function to each and every element of the iterator 
l=[2,3,4,5,6,7,8]

def square(n):
    return n*n
print(tuple(map(square,l)))
 
#  filter() : 

num=[1,2,3,4,5,6,7,8,9,10]

def is_even(n):
    return n%2==0

print(list(filter(is_even,num)))

# reduce() :  cummulative output 






























