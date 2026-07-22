# import keyword
# print(keyword.kwlist)
from operator import add
#from zipimport import path_sep

# integers = 450070850
# floating_points = 4.50070850
# strings = "450070850"
# print(integers, floating_points, strings)
#
#
# a, b, c = 2, 2., "2"
# print(a, b, c)


# a = 2
# b = 3.
# c = "4"
#
# a1 = type(a)
# b1 = type(b)
# c1 = type(c)
#
# a2 = type(a1)
#
# print(a, a1, a2)


# a = 2
# b = "4"
# print(a, b)
# a, b = b, a
# print(a, b)


# a = 2
# b = "4"
# a = b
# print(a, b)


# a = 4
# b = 4
# a = b = 4


# a, b = 3, 4
# c = "10"
# d = "20"
# e = 6.5
# k = 12.9

# region add
# print(b+a, type(b+a)) #ok
# print(a+b, type(a+b)) #ok
# print("_____________")
# print(a+c, type(a+c)) #mistake
# print(c+a, type(c+a)) #mistake
# print("_____________")
# print(a+e, type(a+e)) #ok
# print(e+a, type(e+a)) #ok
# print("_____________")
# print(c+d, type(c+d)) #ok
# print(d+c, type(d+c)) #ok
# print("_____________")
# print(c+e, type(c+e)) #mistake
# print(e+c, type(e+c)) #mistake
# print("_____________")
# print(k+e, type(k+e)) #ok
# print(e+k, type(e+k)) #ok
# print("_____________")
# print(0.3+0.3+0.3) #!!!!!!!!!
# endregion
# region subtr
# print(b-a, type(b-a)) #ok
# print(a-b, type(a-b)) #ok
# print("_____________")
# print(a-c, type(a-c)) #mistake
# print(c-a, type(c-a)) #mistake
# print("_____________")
# print(a-e, type(a-e)) #ok
# print(e-a, type(e-a)) #ok
# print("_____________")
# print(c-d, type(c-d)) #mistake
# print(d-c, type(d-c)) #mistake
# print("_____________")
# print(c-e, type(c-e)) #mistake
# print(e-c, type(e-c)) #mistake
# print("_____________")
# print(k-e, type(k-e)) #ok
# print(e-k, type(e-k)) #ok
# print("_____________")
# print(9**19-int(float(9**19))) #!!!!!!!!!
# endregion

# region

# print(42/8, 42//8, 42%8)
# print(-42/-8, -42//-8, -42%-8)
# print(-42/8, -42//8, -42%8)
# print(42/-8, 42//-8, 42%-8)

# a//b=q remainder r
# b*q+r=a

# endregion

# a = int(input("Enter a number: "))
# print((-9)**a) #порядок дій


# a = 0.3*9
# a = round(0.3*9, 1) #округлення
# print(a==2.7)
# a = 0.3
# print(a*9, round(a*9, 10), round(a*9, 20), sep='\n')


# a, b, c = int(input("Enter a number 1: ")), int(input("Enter a number 2: ")), int(input("Enter a number 3: "))
# print(a**(b/c))



# a = int(input())
# b = int(input())
# if a > 10:
#     if b > 0:
#         a = a+10
#     else:
#         a = a+20
# elif a > 0:
#     a = a +3
# else:
#     a = a + 1
# print(a, b)


# a, b = int(input()), int(input())
# if b != 0:
#     print(a/b)
# else:
#     print("Error")


# a, b, c = int(input()), int(input()), int(input())
# if a <= c and c <= b:
#     print("c in range")
# else:
#     print("c is not in range")


# print(int(True))
# print(int(False))



# print(bool(10)) #любе значення не нуль - це тру. пустота це нуль
# a = int(input())
# if a:
#     print("ok")


# and
# 0 0   0
# 0 1   0
# 1 0   0
# 1 1   1
# or
# 0 0   0
# 1 0   1
# 0 1   1
# 1 1   1


# z = 10
# a = b = (z==0)
# print(a, b, z)


# z = 1
# b = 0
# a = (b==(z==0))
# print(a, b, z)


# a, b = int(input()), int(input())
# # if a==b!=0 and a<10 and b<10: #те саме, що і знизу
# # if a<10 and b<10 and a and b:
# if a<10>b and a and b:
#     print(a*b)
# else:
#     print(a+b)


# a, b = int(input()), int(input())
# c = a + b if a > b else a * b
# print(c)


# a = 10
# a > 5 and print("dadad")


# a = 10
# b = (a > 5 and print("dadad"))
# print(b)


# try:
#     ...
# except (TypeError, ZeroDivisionError) as e:
#     ...
# except:
#     ...
# else:
#     выполнится если исключение не было поймано
# finally:
#     всегда запускается в конце блока try


# try:      #перехват помилки
#     a = int(input())
# except:      #якщо знайшли помилку йдемо сюди
#     print("Not number")


# try:
#     a, b = int(input()), int(input())
#     print(a/b)
# except ZeroDivisionError:
#     print("Zero")
# except ValueError:
#     print("Not number")
# except NameError:
#     print("Name error")
# except:
#     pass
# else:
#     print("Without error")


# try:
#     a, b = int(input()), int(input())
#     if a > b or b > a:
#         print(a/b)
#     else:
#         print("A and B are equal")
# except ZeroDivisionError:
#     print("Division Impossible")
# except ValueError:
#     print("Value Error")



# a = a +2
# a += 2
#
# a = a / 3
# a /= 3


# print(int(input())+int(input()))


# x = int(input())
# print("He works until: ", 12+x//60,":", x%60, sep="")


# x, h, m = int(input("when she arrives:")), int(input("how many hours she works:")), int(input("how many minutes she works:"))
# print((h*60+m+x)//60)
# print((h*60+m+x)%60)


# a = int(input())
# a1 = a%10
# a2 = (a//10)%10
# a3 = (a//100)%10
# a4 = (a//1000)%10
# a5 = a//10000
# res = a1*10000+a2*1000+a3*100+a4*10+a5
# print(res)
# print(a1,a2,a3,a4,a5)


# ab = int(input())
# ab, b5 = ab // 10, ab % 10
# ab, b4 = ab // 10, ab % 10
# ab, b3 = ab // 10, ab % 10
# ab, b2 = ab // 10, ab % 10
# print(b5, b4, b3, b2, ab, sep="")


# year = int(input())
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Bissextile year")
# else:
#     print("Standard year")


# month_num = int(input())
#
# if 3 <= month_num <= 5:
#     print('Spring')
# elif 6 <= month_num <= 8:
#     print('Summer')
# elif 9 <= month_num <= 11:
#     print('Autumn')
# elif 1 <= month_num <= 12:
#     print('Winter')

# region while + infinit while

# a = 0
# while a < 55:
#     print(a)
#     a += 1


# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)


# number = int(input("Enter a number: "))
# i = 0
# while i <= number:
#     if not i % 2:
#         print(i, end=" ")
#     i += 1
# print()


# number = int(input("Enter a number: "))
# i = 0
# while i <= number - 2:
#     i += 2
#     print(i, end=" ")


# while True:
#     a = int(input())
#     print(add(a,a))


# res = 0
# a = int(input())
# while a:
#     res += a
#     a = int(input())
# print(res)


# res = 0
# while True:
#     a = int(input())
#     res += a
#     if not a:
#         print(res)
#         break
#
# endregion


# for i in 10, 4, 7, 5, "ert", True:
#     print(i)

# i = 0
# y = int(input())
# for i in range(1, y+1, 1):
#     res = i * (i + 1)
# print(res)


a = int(input())
i = 1
res = 1
# while i <= a:
#     res *= i
#     i += 1
# print(res)
for i in range(1, a + 1):
    res *= i
print(res)







