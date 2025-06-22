#homework1
numbers = []

for i in range(5):
    num = int(input(f"{i+1}-ლი რიცხვი: "))
    numbers.append(num)

numbers.reverse()
print("შებრუნებული სია:", numbers)
#homework2
numbers = []

for i in range(5):
    num = int(input(f"{i+1}-ლი რიცხვი: "))
    numbers.append(num)

numbers.reverse()
print("შებრუნებული სია:", numbers)
#homework3
def word_lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

print(word_lengths(["apple", "banana", "kiwi"])) 
#homework4
students = []

for i in range(3): 
    name = input("მოსწავლის სახელი: ")
    grades = []
    for j in range(3): 
        grade = float(input(f"{name} - ქულა {j+1}: "))
        grades.append(grade)
    avg = sum(grades) / len(grades)
    students.append((name, avg))

print("\n📘 სკოლის ჟურნალი:")
for student in students:
    print(f"{student[0]} - საშუალო ქულა: {student[1]:.2f}")

#homework5
def filter_long_strings(strings):
    result = []
    for s in strings:
        if len(s) > 3:
            result.append(s)
    return result

print(filter_long_strings(["cat", "apple", "dog", "sunshine"]))  # ['apple', 'sunshine']


