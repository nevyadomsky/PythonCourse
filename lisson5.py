# a = [1, "3", 3.0, 2, 3, "asd", "asdf", 3.0, 3]
#    0   1    2   3  4    5      6      7   8
#   -9  -8   -7  -6 -5   -4     -3     -2  -1
# print(len(a))
#
# b = []
# c = list()
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))


# print(b)
# b.append(123)
# print(b)
#
#
# print(a)
# a.remove(3)
# del a[3]
# a.pop(3)
# del a[-3]
# a.insert(3, "efwefwf")
# print(a)
# a[3]= "gegegegeg"
# print(a)
# print(a[3])


# a = [1, 2, 5, 6 , 8, 9, 2.0, 2, 2, 4, 2] #скільки двійок в списку
# res = 0
# for i in range(0, len(a)): #від 0 до кінця списку
#     if a[i] == 2 and issubclass(int, type(a[i])): # провіряє чи число ціле
#         res += 1
# print(res)
# # 2.0 = 2
# print(a.count(2))


# res = 0
# all_elements = []
# while True:
#     a = int(input())
#     if not a: # якщо 0, то кінець
#         break
#     all_elements.append(a)
# print(sum(all_elements), all_elements, sep='\n')
# print(max(all_elements), sep='\n')
# print(min(all_elements), sep='\n')


# a = [1, 2, 3, 4, 5]
# print(*a, sep="\n") # * пише кожний елемент зі списку з нового рядка
# print(a[0], a[1], a[2], a[3], a[4], sep=" servus ")


# чи є сенс рахувати двійки, якщо їх там немає
# a = [1, 2, 5, 6 , 8, 9, 2.0, 2, 2, 4, 2]
# if 99 in a:
#     res = 0
#     for x in a:
#         if x == 99:
#             res += 1
#     print(res)
# else:
#     print("Keine 99")


# a = [1, 2, 5, 6 , 8, 9, 2.0, 2, 2, 4, 2]
# res = 0
# for i in range(len(a)): #для кожного індексу в списку
#     a[i]
# for i in a: #для кожного значення в списку


# написати код, щоб виводив список справа наліво
# a = [i for i in range(1,11)]
# print(a)
# for i in range(-1, -len(a)+1,-1):
#     print(i,a[i])

# a = [i for i in range(1, 11)]
# print(a)
# b = []
# for i in range(len(a)):
#     b.insert(0, a[i])
# print(b)

# a = [i for i in range(50,80)]
# print(a)
# a.reverse() #дописуємо ще раз прінт а після цієї команди
# print(a)
# print(list(reversed(a)))
# print(a)
# a = [i for i in range(50,80)]
# print(a)
# print(a[3:15:2]) # вирізати з 3-го по 15-ий елемент з кроком 2

# a = [i for i in range(50,80)]
# b1 = a[-10:-1:1]
# b2 = a[-1:-10:-1]
# b3 = a[10:1:-1]
# b4 = a[1:10:1]
# print(a, b1, b2, b3, b4, sep='\n')

# #аналогічні конструкції
# a = [i**2 for i in range(0,20,3)]
# print(a)
#
# a = []
# for i in range(0,20,3):
#     a.append(i**2)
# print(a)


# a = [i for i in range(0,10)]
# print(a)
# b = [i**2 for i in a]
# print(b)


# a = [1, 2, 3, 4, 5]
# b = a.copy() # незалежний список
# b = a[::] # також
# print(a)
# print(b)
# a.append(66666)
# print(a)
# print(b)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 4, 3, "1", "2"]
# b = []
# for x in a:
#     if x not in b:
#         b.append(x)
# print(a)
# print(b)


# a = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15]
# ]
# print(a[1][4]) #10
# print(*a, sep="\n")


a = [['.'] * 7 for x in range(7)]
for x in range(7):
    for y in range(7):
        if x == y:
            a[x][y] = "*"
        if x == 7//2:
            a[x][y] = "*"
        if y == 7//2:
            a[x][y] = "*"
        if x + y == len(a) - 1:
            a[x][y] = "*"
print(*a, sep='\n')