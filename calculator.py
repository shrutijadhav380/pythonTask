a=float(input("enter a  first Number:"))
b=float(input("enter a  first Number:"))
op=input("enter a operator(+,-,*,/)")
if op=="+":
    print("Additon of number:",a+b)
elif op=="-":
    print("subtraction of Number",a-b)
elif op=="*":
    print("multiplication of Number",a*b)
elif op=="/":
    if b==0:
        print("cannot divide by zero")
    else:
        print("divison of number",a/b)
else:
    print("Invalid operator")


