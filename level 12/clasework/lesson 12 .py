name = "Tika"
password = "1222"

user_name = (input("enter your name:"))
user_password = (input("enter your password:"))

if name == user_name and password == user_password:
    print ("done!")
else:
    print ("wrong")
    user_name = (input("enter your name:"))
user_password = (input("enter your password:"))