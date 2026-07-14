# fruits = ["apple", "banana", "cherry", "grape", "watermelon"]
# print(fruits)
# print(fruits[0])
# print(fruits[4])
# print(len(fruits)) #len - кількість значень змінної


# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "orange"
# print(fruits)


# fruits = ["apple", "banana", "cherry"]
# fruits.append("watermelon") #додає один елемент
# fruits.append("grape")
# print(fruits)
# #fruits.extend(["watermelon", "grape"])


# animals = ["dog", "cat", "bird", "fish"]
# animals.remove("cat")
# animals.append("horse")
# print(animals)


# fruits = ["apple", "banana", "cherry", "orange"]
# for fruit in fruits:
#     print(f"I like {fruit}")


# numbers = [5, 10, 15, 20, 25]
# for number in numbers:
#     if number >= 15:
#         print(number)

# count = 0
# grades = [85, 42, 90, 55, 30, 100]
# for grade in grades:
#     if grade >= 60:
#         count = count + 1
#         print(grade)
# print(f"There are {count} passing grades")


friends = ["Alex", "Denys", "Mark", "John"]
name = input("Enter your name: ").title()
if name in friends:
    print("You are my friend")
else:
    print("I don't know you")



