# In this example we will be working on building a greceory stroe
#calculator.

num1 = input("Please enter a number: ")
print("what kind of operation would you like to perform")
Operator = input("Please specify in + - / * ")
num2 = input("Please enter the second number: ")


if (Operator == "+"):
    ans = (int(num1)+int(num2))
    print(ans)
elif(Operator == "-"):
    ans = (int(num1) - int(num2))
    print(ans)
elif(Operator == "*"):
    ans = (int(num1) * int(num2))
    print(ans)
elif(Operator == "/"):
    ans = (int(num1) / int(num2))
    print(ans)
else:
    print("invalid operation requested")



