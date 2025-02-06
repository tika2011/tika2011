# 1.  ფუნქცია: ელემენტის მოძებნა
#შექმენი ფუნქცია find_item(item_list, item), რომელიც მიიღებს ორი პარამეტრი:
#item_list - სია ელემენტების.
#item - ელემენტი, რომლის შეძენა გსურს სიაში. ფუნქციამ უნდა დააბრუნოს True, თუ ელემენტი არსებობს სიაში და False, თუ არ არსებობს.
def  find_item(item_list, item):
     if find_item > item:
          return("True")
     else:
          return("False")


#2. ფუნქცია: მაქსიმალური ელემენტი
#შექმენი ფუნქცია max_item(num_list), რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ამ რიცხვებიდან ყველაზე დიდს.
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def max_item(num_list):
     if max_item > num_list:
          return("big numbers")
          

#3. დაასრულეთ საკლასო დავალება


#4. ფუნქცია: ზრდა
#შექმენი ფუნქცია increment_list(num_list), რომელიც მიიღებს რიცხვების სიას და თითოეულ რიცხვს 1-ს მოუმატებს.
def increment_list(num_list):
     return [num + 1 for num in num_list]
     
#5. ფუნქცია: სიტყვის შებრუნება
#შექმენი ფუნქცია reverse_string(word), რომელიც მიიღებს სიტყვას და დააბრუნებს მას პირიქით.

def reverse_string(word):
     return word[::-1]