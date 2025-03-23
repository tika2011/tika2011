#homework1
#.lower()-eეს არის ფუნქცია რომელსაც სტრინგში გამოაქვს სიტყვა პატარა ასოებით.
#.upper()-ეს არის ფუნქცია რომელსაც სტრინგში გამოაქვს სიტყვა დიდი ასოებით.
#.capitalize()- ეს არის ფუნქცია რომელსაც სტრინგში სიტყვის გამოტანას იწყებს 
# დიდი ასოთი და აგრძელებს პატარა ასოებით.
#homework2
input = input("Enter your name: ")
if input == input.capitalize():
    print("hello")
else:
    print("bye")
#homework3
input = input("Enter your name: ")
input = input("Enter your username: ")
if input.find(a) == -1:
    print("theres no a in your name and username")
else:
    print("theres an a in your name and username")
#homework4
input = input("Enter your username: ")
input = input("how wuld you like your username to be displayed?: ")
if input == "upper":
    print(input.upper())
elif input == "lower":
    print(input.lower())
elif input == "capitalize":
    print(input.capitalize())