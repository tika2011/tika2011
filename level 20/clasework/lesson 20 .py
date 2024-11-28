a = 3 > 2
b = 7 < 10
c = 5 == 5
d = 2 < 10
e = 6 > 8
f = 3 != 4
g = 5 == 10
h = 2 != 9

first = a and b
second = c or d
third = e and f
fourth = g or h

print("first (a and b):",first )
print("second (c or d):",second)
print("third (e and f):",third)
print("fourth (g or h):",fourth )

# clasework
#2)შექმენით სია რომლის სიგრძეც იქნება 6 (ანუ ექნება 6 ელემენტი) შემდეგ დაბეჭდეთ ამ სიის
#სიგრძე len() ფუნქციის გამოყენებით და სათითაოდ ყველა ელემენტი რიგის ნომრის ანუ index-ების გამოყენებით 

the_list= ["apple","pear","banana","peach","orange","tangerine"]
print(len(the_list))

print(the_list[0])
print(the_list[1])
print(the_list[2])
print(the_list[3])
print(the_list[4])
print(the_list[5])