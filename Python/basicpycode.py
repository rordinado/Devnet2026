# Simple Python Program

def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

def main():
    # Variables
    name = "World"
    num1 = 10
    num2 = 20
    
    # Function calls
    print(greet(name))
    print(f"Sum of {num1} and {num2} is: {add_numbers(num1, num2)}")
    
    # Loop
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(f"Number: {i}")
    
    # List
    fruits = ["apple", "banana", "cherry"]
    print("\nFruits:")
    for fruit in fruits:
        print(f"  - {fruit}")

if __name__ == "__main__":
    main()
