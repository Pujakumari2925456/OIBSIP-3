import random
import string

print("Welcome to the Password Generator")


total_size = int(input("Enter the total size of the password you require: "))
letters = int(input("Enter the number of letters you require: "))
numbers = int(input("Enter the number of numbers you require: "))
symbols = int(input("Enter the number of symbols you require: "))


if letters + numbers + symbols > total_size:
    print("Error: The sum of letters, numbers, and symbols exceeds the total size.")
    exit(1)

# Generate the required characters
lists = []
for _ in range(letters):
    lists.append(random.choice(string.ascii_letters))
for _ in range(numbers):
    lists.append(random.choice(string.digits))
for _ in range(symbols):
    lists.append(random.choice(string.punctuation))


while len(lists) < total_size:
    print("you have enterd values less than specified so its randomly generated")
    lists.append(random.choice(string.ascii_letters + string.digits + string.punctuation))


random.shuffle(lists)


password = ''.join(lists)

print(f"Your generated password is: {password}")
