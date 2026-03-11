originalprice=float(input("enter the original price:"))
discountpercentage=float(input("enter the discount percentage"))
discountamount=(originalprice*discountpercentage)/100
finalprice=originalprice - discountamount
print(finalprice)