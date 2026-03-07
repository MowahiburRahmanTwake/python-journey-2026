# # Day 0 - Starting again in English
# print("Hello, I am Md. Mowahibur!")
# print("Today I am starting fresh.")
# print("I will get a job at Google / OpenAI / xAI!")

# # Ask for name and greet
# name = input("What is your name? ")
# print("Hello", name + "!")
# print("You are doing great!")

name = input("What is your name? ")
run_count = 1
#day 0 -Adding two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Division - check if num2 is zero
if num2 != 0:
    division_result = num1 / num2
    print(f"Division: {division_result:.2f}")
else:
    print("Division: Cannot divide by zero!")

if num1 > num2:
    print("The bigger number is:", num1)
elif num2 > num1:
    print("The bigger number is:", num2)
else:
    print("Both numbers are equal!", num1)



print(f"Good job, {name}! You will get a job at Google/OpenAI/xAI!")

#Load previous run count from file
try:
    with open("run_count.txt", "r") as file:
        run_count = int(file.read())
except FileNotFoundError:
        run_count = 0
run_count += 1

print(f"This program has been run {run_count} time(s)!")

#save updated run count to file
with open("run_count.txt", "w") as file:
    file.write(str(run_count))
print(f"Welcome back! This program has been run {run_count - 1} time(s) before.")
print("Thanks for practicing today!")