# # Day 1 - Learning Lists

numbers = [5, 10, 15, 20, 25]
print("My numbers list:", numbers)

# Accessing elements
print("First number:", numbers[0])
print("Second number:", numbers[1])
print("Last number:", numbers[-1])

print("\nAll numbers using loop:")
for num in numbers:
    print(num)

numbers.append(30)
print("\nAfter appending 30:", numbers)

numbers.insert( 2,12)
print("After insert:", numbers)

# Sum of all numbers
total = 0
for num in numbers:
    total += num
print("Sum of all numbers:", total)

# Average of numbers
average = total / len(numbers)
print("Average:", round(average, 2))