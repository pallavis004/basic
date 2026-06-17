# Basic Python Concepts

# Variables
name = "Alice"
age = 25
height = 5.6

print(f"Name: {name}, Age: {age}, Height: {height}")

# List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Function
def greet(person):
    return f"Hello, {person}!"

print(greet("Bob"))

# Dictionary
student = {"name": "John", "grade": "A", "score": 95}
for key, value in student.items():
    print(f"{key}: {value}")

# Conditional
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
