'''
# File Handling 

# why ??
# store user data 
# logs (activity , errors)
# reports 
# configurations files 
# data processing 

# open file 
# perform operations 
# close file 


f=open("sample.txt","r")
print(f.read())
f.close()


with open("sample.txt","r") as f: # read mode 
    print(f.read())



#with open("sample.txt","w") as f:
    #f.write("this is write mode")


with open("data.txt","w") as f: # write mode 
    f.write("this is first line\n")
    f.write("this is second line\n")

with open("data.txt","a") as f:  # append mode 
    f.write("this is write mode\n")


#with open("newfile.txt", "x") as f :
    #f.write("created new file")

# file modes 

# r ---> Read 
# w---> write (overwrite)
# a ---> append 
# x ---> creating new file 



# read operations 
# read()
# readline()
# readlines()


with open("sample.txt","r") as f: # read mode 
    print(f.read())


with open("sample.txt","r") as f: # read mode 
    print(f.readline())


with open("sample.txt","r") as f: # read mode 
    print(f.readlines())

with open("sample.txt","r") as f: # read mode 
    print(f.readline(5))

with open("sample.txt","r") as f:
    for line in f:
        print(line.strip("@"))






f = open("sample.txt", "r")
for line in f:
    print(line.replace("@",""))
f.close()

'''

f=open("sample.txt", "r")
data=f.read()
h=data.replace("@","")
print(h.strip())
f.close()


f=open("sample.txt", "r")
data=f.read()
print(data.upper())
f.close()


f=open("sample.txt", "r")
data=f.read()
print(len(data))
f.close()


# CSV ----> comma separarted values 
'''
id, name , age ,clas 
101, sai,29,high clas
101, sai,29,high clas

# easy to ready 
# light weight format
# used in excel sheets 


import csv

with open("file.csv", "r") as f:
    reader=csv.reader(f)
    next(reader) #skip the header
    for i in reader:
        print(i)



import csv

with open("file.csv", "r") as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)


'''
import csv
with open("file.csv", "r") as f:
    rocky=csv.reader(f)
    for i in rocky:
        print(i[3])



# JSON files ---> java script object notation 

# json format is like dictionary 

{
'id':101,'name':'sai', 'age':28
}

# light weight 
# used in Api's
# 


import json

with open("data.json","r") as f:
    x=json.load(f)

print(x)





