# lib/functions.py

# 1. greet_programmer()
def greet_programmer():
    print("Hello, programmer!")

# 2. greet(name)
def greet(name):
    print(f"Hello, {name}!")

# 3. greet_with_default(name="programmer")
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# 4. add(num1, num2)
def add(num1, num2):
    return num1 + num2

# 5. halve(number)
def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2
