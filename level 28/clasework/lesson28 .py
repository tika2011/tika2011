
#clasework1
def add_numbers(a, b):
  return a + b

print(add_numbers(3,5))


# clasework2

def is_even(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "False"
  
print(is_even(13))

# clasework3

def find_max(a, b):
  if a > b:
    return f"{a} is larger"
  else:
    return f"{b} is larger"
  
print(find_max(2,4))


# clasework4

def reverse_string(text):
  return text[::-1]

print(reverse_string("Never give up on your dream"))

#clasework5

def count_vowels(text):
  vowels = "aeiou"
  count = 0
  for i in text:
    if i in vowels:
      count += 1
  return count

print(count_vowels("dream"))

# clasework6
def is_divisible(a, b):
  if b == 0:
    return False
  else:
    return True
  
print(is_divisible(2, 0))