# import keyword
# print(keyword.kwlist)
from operator import add

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


# print(42/8, 42//8, 42%8)
# print(-42/-8, -42//-8, -42%-8)
# print(-42/8, -42//8, -42%8)
# print(42/-8, 42//-8, 42%-8)

# a//b=q remainder r
# b*q+r=a



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
erehehwegegewg