#even/odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")

    # Grade Calculator (if-elif-else)

# marks = int(input("Enter your marks: "))
# if marks >= 80:
#     print("Grade: A+")
# elif marks >= 70:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 50:
#     print("Grade: D")
# else:
#     print("Grade: F")
    
# Positive / Negative / Zero CheckerPython
# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")
# 1 to 100 Print (for loop + while loop দুটোই করো)
# for loop
# for i in range(1, 101):
#     print(i, end=" ")
# print()  # for new line
# while loop
# i = 1
# while i <= 100:
#     print(i, end= " ")
#     i += 1

# Multiplication Table (user-এর number-এর 1-10 table)
correct_pass = "secret123"
attempts = 3
while attempts > 0:
    user_pass = input(f"Enter password ({attempts} attempts left): ")
    if user_pass == correct_pass:
        print("Access granted!")
        break
    else:
        print("Wrong password!")
        attempts -= 1
if attempts == 0:
    print("Access denied. Too many wrong attempts.")