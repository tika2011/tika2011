#homework1
for i in range(20):
    if i % 2 == 0:
        print(str(i), "even")
    else:
        print(str(i), "odd")
#homework2
number_sum = 0
for i in range (10):
    number_sum += i
    print(number_sum)
    #homework3
    mystery_number= 7
    user_guess= int(input("please choos number from 1-10: "))
    while mystery_number !=user_guess:
        user_guess =int(input("please choos number from 1-10: "))
#homework4
password="131636"
user_guess = input("guess the password: ")
while password !=user_guess:
    user_guess = input("guess the password: ")