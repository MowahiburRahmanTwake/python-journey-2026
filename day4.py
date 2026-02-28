#Function 1 : Greeting
# def greet():
#     print("Hello, Md. Mowahibur! Welcome to day 4")
#     print("You are doing getting closer to google/ openAI level!")


# #call the function
# greet()
# greet()

#Function 2: Personalized greeting
# def greet_name(name):
#     print(f"Hello, {name} ! How are you today?")


# greet_name("Mowahibur")
# greet_name("Rahim")
# greet_name(input("Enter your friend's name: "))

#Function 3: Add two numbers and return the result
# def add_numbers(num1, num2):
#     result = num1 + num2
#     return result

# sum1 = add_numbers(5, 10)
# print("5 + 7 = ", sum1)

# sum2 = add_numbers(10, 20)
# print("10 + 20 = ", sum2)

#Function 4: Calculate the area of a circle
# def calculate(x, y, operation):
#     if operation == "+":
#         return x + y
#     elif operation == "-":
#         return x - y
#     elif operation == "*":
#         return x * y
#     elif operation == "/":
#         if y != 0:
#             return x / y
#         else:
#             return "Cannot divide by zero!"
#     else:
#         return "Invalid operation!"
    
# print(calculate(10, 5, "+"))
# print(calculate(10, 5, "/"))
# print(calculate(10, 5, "/"))

#Function 5: Factorial (using loop)
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers!"
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print("Factorial of 5 is:", factorial(5))  # Output: 120
# print("Factorial of 0 is:", factorial(0))  # Output: 1
# print("Factorial of 7 is:", factorial(7))   # Output: 5040

#Function 6: Is Prime ?
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print("Is 17 prime?", is_prime(7))   # Output: True
# print("Is 15 prime?", is_prime(10))  # Output: False
# print("Is 2 prime?", is_prime(2))    # Output: True

# Function 7: Print shopping list nicely
def print_shopping_list(items):
    print("\n Your Shopping List:")
    if not items:
        print("List is empty!")
    else:
        for i, item in enumerate(items, start =1):
            print(f"{i}. {item}")

my_list = ["দুধ", "ডিম", "আলু"]
print_shopping_list(my_list)

empty_list = []
print_shopping_list(empty_list)