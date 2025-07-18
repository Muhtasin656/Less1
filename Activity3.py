def add(p,q):
    return p+q
def subtraction(p,q):
    return p-q
def multipliplication(p,q):
    return p*q
def division(p,q):
    return p/q
print("Select a option:")
print("press a for addition")
print("press b for subtraction")
print("press c for multiplication")
print("press d for division")
choice=input("Enter a choice")
num1=int(input("enter your first number"))
num2=int(input("enter your second number"))
if choice=="a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=",subtraction(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"=",multipliplication(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"=",division(num1,num2))
else:
    print("Invalid input")