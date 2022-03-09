from __future__ import division


def addition(num1,  num2 ):
    return num1 + num2 
def subtraction(num1, num2):
    return num1 - num2 
def multiplication(num2, num1):
    return num1 * num2
def divide(num1, num2) :
    return num1, num2  

print ("1 addition")
print ("2 subtraction")
print ("3 multiplication")
print ("4 division")

choice = input ("enter your choice")

if choice == "1":
    num1 = int(input("enter number 1 :"))
    num2 = int(input("enter  number 2 :"))
    sum = addition(num1, num2)
    print (num1, "+" , num2, "=", sum)
elif choice == "2":
    num1 = int(input("enter number 1 :"))
    num2 = int(input("enter  number 2 :"))
    difference = subtraction(num1, num2)
    print (num1, "-" , num2 ,  "=", (difference))
elif choice == "3":
    num1 = int(input("enter number 1 :"))
    num2 = int(input("enter  number 2 :"))
    product= multiplication(num1, num2)
    print (num1, "*" , num2 , "=", (product))
elif choice == "4":
    num1 = int(input("enter number 1 :"))
    num2 = int(input("enter  number 25:"))
    division = divide(num1, num2)
    print (num1, "/" , num2 , "=", (division))
else:
    print("please enter a valid choice")







