# Python Program to Swap Two Numbers #

a = float(input("Please Enter the first Value a:"))
b = float(input("Please Enter the Second Value b:"))

print("Before Swaping Two Numbers :a ={0} and b = {1}".format(a,b))

temp = a
a=b
b=temp

print("After Swaping Two Numbers :a={0} and b ={1}".format(a,b))
