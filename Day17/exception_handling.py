# exception handling ?? ---> an exception is an error which occurs during program execution. 

# protecting program from crashing and handling the errors is called exception handling . 

# try 
# except 
# else 
# finally 

'''
try :
    # where the risk is

except someerror_name:
    # handle error 



try:
    num1=int(input("enter num1 : "))
    num2=int(input("enter num12 : "))
    result=num1/num2
    print(int(result))

except ZeroDivisionError:
    print("you can't divide number with 0")

'''


try:
   num= int("78")  
   num+=10

except ValueError:
    print("error in conversion")

else:
    print("conversion successful", num)


finally:
    print("exceptions handled perfectly ")


# custom exceptions / user defined exceptions 


class InsufficientBalanceError(Exception):
  pass

try:
    balance=5000
    withdraw=int(input("enter withdraw amount :"))

    if withdraw > balance:
        raise InsufficientBalanceError("insufficient balance")
    
except InsufficientBalanceError as e:
    print("error", e)

else:
    print("withdraw successful")

finally:
    print("transaction completed")

















