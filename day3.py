# # Basic List Create + OperationsPython
# #Problem 1: create and modify list
# friends = ["Rahim", "karim", "Jamal", "Salam"]
# print("Original list:", friends)

# friends.append("Rina") #add at end
# print("After append:", friends)

# friends.insert(1, "Sohag") # insert at position 1
# print("After insert:", friends)

# friends.remove("karim") # remove by value
# print("After remove:", friends)

# print("Length:", len(friends))
# print("Index of Salam:", friends.index("Salam"))

# Loop দিয়ে List Print + Sum/AveragePython
#problem 2: Numbers of list with loop

# numbers = [5, 12, 8,19,7]

# print("Numbers:", numbers)
# total = 0
# for num in numbers:
#     total += num
#     print(num, end=" ") # print each number
# print() # for new line

# print("Sum:", total)
# average = total / len(numbers)
# print("Average:", average)
# Find Max / Min in List (without built-in max/min)Python

#problem 3: max and min manually

# scores = [45, 78, 92, 61, 88, 55]
# max_score = scores[0]
# min_score = scores[0]

# for score in scores:
#     if score > max_score:
#         max_score = score
#     if score < min_score:
#         min_score = score

# print("Max score:", max_score)
# print("Min score:", min_score)


# Problem 4: Reverse using loop
fruits = ["apple", "banana", "cherry", "date"]
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1): # backwards loop
    reversed_fruits.append(fruits[i])

print("Original list:", fruits)
print("Reversed list:", reversed_fruits)
