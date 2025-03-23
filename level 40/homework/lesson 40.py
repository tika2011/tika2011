#homework1
name = input("Enter your name: ")
name = name.lower()
print(name)
#homework2
surname = input("Enter your surname ")
surname = surname.upper()
print(surname)
#homework3
text = input("Write the text in Oatara letters:")
text = text.capitalize()
print(text)
#homework4
text = input("Enter taxt: ")
letter = input("Write the letter: ")
index = text.find(letter)
if index != -1:
    print(f"love'{letter}'corect{index}")
else:
    print(f"q'{letter}' not found")
#homework5
strings = ["programing", "python", "HTML", "css"]
for i in range(len(strings)):
    strings[i] = strings[i].upper()
print(strings)
