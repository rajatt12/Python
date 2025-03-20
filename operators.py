
'''print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) #a^b
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)'''
#simple calculator
num1=int(input("Enter first number="))
num2=int(input("Enter second number="))
operation=input("Enter the operation you want to perform ")
if(operation=="+"):
    print(num1+num2)
elif(operation=="-"):
    print(num1-num2)
elif(operation=="*"):
    print(num1*num2)
elif(operation=="/"):
    print(num1/num2)  