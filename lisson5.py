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


a = [1, 2, 5, 6 , 8, 9, 2.0, 2, 2, 4, 2] #скільки двійок в списку
res = 0
for i in range(0, len(a)): #від 0 до кінця списку
    if a[i] == 2 and issubclass(int, type(a[i])):
        res += 1
print(res)
# 2.0 = 2
print(a.count(2))