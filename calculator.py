#Basic input
while True:
 try:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
 except:
    print("please enter valid numbers")
    continue
    


#ask user what opreation they want
operation = input("Choose operation (+, -, *, /):")

#perform the calculation
if operation == "+":
    result = num1+num2
elif operation == "-":
    result = num1-num2
elif operation == "*":
    result = num1*num2     
elif operation == "/": 
    result = num1/num2
else:
    print("Invalid operation")  
    

print("Result:", result)      

again = input("Do you want another calculation? (y/n):")

 if again == "n":
   