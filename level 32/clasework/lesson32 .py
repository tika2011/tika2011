#1. შექმენი ფუნცია, სადაც არგუმენტად გადასცემ ორ რიცხვს, შემდეგ დაპრინტე ამ ორი რიიცხვის განაყოფი.
def divide_numbers(num1, num2):
    if num2 != 0:
        print(num1 / num2)
    else:
        print("we can't divid this number")
#2. შექმენი ფუნქცია, სადაც არგუმენტად გადასცემ დაბადების თარიღს, შემდეგ დაპრინტე თუ რამდენი წლისაა მომხმარებელი.
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    print(age)

#3. შექმენი ფუნქცია, სადაც არგუმენტად გადასცემ რიცხვ, შემდეგ დაპრინტე ეს რიცხვი გამრავლებული 5-ზე.
def multiply_by_five(number):
    print(number * 5)