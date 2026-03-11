# git clone https://github.com/sairammerugumalla9966/PYTHON_BATCH3.git

# Loops ?? for loop and while loop 


#For loop : is used to iterate over a sequence (range , list , tuple , string)

#syntax :
#for var in sequence:
    # statements 


for i in range(0,6):
    print(i)
    print("loop running")

print("loop completed")



name=["sairam", "keerthi" ,"naveen"]

for y in name:
    print(y)




# while loop : repeats untill the condition is true ,we use when we dont know the range 

#hile condition :
   #statements 

i=1  # initialise the value 

while i<=5: # condition 

    print(i,"while loop running")

    i+=1 # incrementation 

print("while loop complete ")




# loop control statements 

# break --->stop the loop 
# continue ---> skip the current interation 
# pass ---> hold the place 

for i in range(0,6):

    if i==4:
        break

    print(i)

print("loop is breaked ")


# continue

for i in range(0,6):

    if i==4:
        print("4 is skipped ")
        continue

    print(i)


# pass 

for i in range(5):
    pass



# nested loops 

# loop inside another loop 

for i in range(5): # 0-4 outer loop   0

    for j in range(6): # inner loop 0-5 
        print(i,j)

  
