# for row in range(4):            #Повтори 4 рази:
#     for columm in range(3):         #Повтори 3 рази:
#         print("#", end="")                #Надрукуй "#"
#     print()                         #Перейди на новий рядок


# for row in range(1, 5): #Повтори рядок 4 рази.
#     for column in range (1, 4): #виведи числа від 1 до 3.
#         print(column, end=" ")
#     print() #перейди на новий рядок


# numbers = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in numbers:
#     for number in row:
#         print(number, end=" ")
#     print()


numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in numbers:
    for number in row:
        if number % 2 == 0:
            print(number)
print()