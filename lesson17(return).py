# def double(number):
#     print(number*2)
# result = double(10)
#from unittest import result


# def double(number):
#     return number*2
# result = double(8) #Якщо даси мені число, я помножу його на 2 і поверну результат
# print(result)


# def subtract(a, b):
#     return a - b
# result = subtract(10, 4)
# print(result)


# def triple(number):
#     return number*3
# result = triple(4)
# print(result)


# def operation(number):
#     return number + 10
#
# result = operation(5) * 2
# print(result)


# def add(a, b):
#     return a + b
#
# result = add(5, 10)
# result = add(result, 20)
#
# print(result)


# def subtract(a, b):
#     return a - b
#
# x = subtract(20, 5)
# y = subtract(10, 3)
#
# print(x + y)


# def is_even(number):
#     if number % 2 == 0: #так перевіряємо, чи число парне
#         return True
#     else:
#         return False
#
# print(is_even(4))
# print(is_even(7))


# def is_even(number):
#     return number % 2 == 0
# result1 = is_even(5)
# result2 = is_even(6)
#
# # print(result1)
# # print(result2)
#
# print(result1, result2, sep="\n")
# result3 = is_even(7)
# result4 = is_even(8)
# print()


# def grade_result(score):
#     if score >= 60:
#         return "Pass"
#     else:
#         return "Fail"
#
# print(grade_result(75))
# print(grade_result(40))


# def count_passed(grades): #тут grades як параметр функції
#      count = 0
#      for grade in grades: #grade — це сама оцінка, а count — кількість знайдених оцінок.
#          if grade >= 60:
#              count = count + 1
#      return count
# grades = [85, 42, 90, 55, 30, 100] #а тут grades, як змінна поза функцією, тому python попереджає
# result = count_passed(grades)
# print(f"There are {result} passing grades")


def sum_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            result = sum(numbers)
            count = count +1
    return count
