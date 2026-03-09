# Function : it is a reuseable block of code which is used for performing particular task .

# uses :
# reduce duplicate code 
# reuse code 
# easy maintaince 
# modularity 

'''

def function_name(): # definition 
    statements 
    statements 
    statements 
    statements
    statements 


function_name() # function calling


# snake_case naming convention 
# CamelCase naming convention 

'''
'''
def sample_function():
    print("function defined successfully")


sample_function()

print("outside function")

'''
def addition():
    a=10
    b=20
    c=a+b

add1=addition()
print(add1)


def addition():
    a=10
    b=20
    c=a+b
    return c

add2=addition()
print(add2)


# functions with parameters 

#def function_name(parmeters):
    #statements / functionbody


#function_name(arguments)



def addition1(num1, num2):
    return num1 + num2

print(addition1(70,30))


# claculate the grade 
'''
marks >= 90 ---> A 
marks >80 ---> B
marks >70 ---> c
marks >60 ---> passs
marks <60 ---> fail
'''

def get_grade(marks):

    if marks >=90:
        return "A GRADE"

    elif marks >=80:
        return "B GRADE"
    
    elif marks >=70:
        return "C GRADE"
    
    elif marks >=60:
       return "passs"

    else :
        return "Fail"
    
print(get_grade(90))   

print(get_grade(65)) 




def user_login(username, password):

    if username=="sairam" and password==12345:
        return "Login successful"
    
    return "invalid details"


print(user_login("Rocky",12345))

print(user_login("sairam",12345))






















