#homework1
#>
print(54 > 66)
print(33 > 12)
print(76 > 67)
#<
print(43 < 66)
print(90 < 99)
print(68 < 80)
#==
print(66 == 60+6)
print(12 == 6*2)
print(33 == 33)
#homework2
for i in range(20):
    if i % 2 == 0:
        print(str(i), "even")
#homework3
print("Welcome to Guess the number game!")

print("Try to guess the number i am thinking of")

number = 5

guess = int(input("Enter the number> "))

if guess == number:
    print("You are correct!")
else:
    print("You are incorrect, try again")