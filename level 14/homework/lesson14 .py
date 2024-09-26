
#homework2
for i in range(0, 20, 2):
   print(i)
#homework3
for i in range(20, 100, 1):
   print(i)
#homework4
for i in range(1,99,2):
    print("odd"+str(i))
for i in range(0,100,2):
    print("even"+ str(i))
 #bonus
print("--- C A L C U L A T O R ---")
print("CALCULATE")

num1 = int(input("Write the first number: "))
print("NEXT")

num2 = int(input("Enter the second number: "))
print("NEXT")

print("-- operators --")
print("+, -, /, *")
print("OK")
operator = input("Enter the required operator: ")
if operator == "+":
   print(num1 + num2)
   print("you choose plus")

elif operator == "-":
   print(num1 - num2)
   print("you choos a disadvantage")
elif operator == "/":
   if num1 == 0 or num2 == 0:
     print("Could not divide by zero")
     print("oh no")
   else:
     print(num1 / num2)
     print("you choose division")

elif operator == "*":
   print(num1 * num2)
   print("you choose to multiply")
else:
   print("does not exist!")
print("Thank you for using Chevney Calculator")