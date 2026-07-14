# for row in range(1, 4):
#     for column in range(1,3):
#         print(f"({row}, {column})", end =" ")
#     print()


# for row in range(1, 6):
#     for col in range(1, 6):
#         print(row * col, end = " ")
#     print()


# for row in range(1, 4):
#     for col in range(1, 6):
#         print("*", end = "")
#     print()


# for row in range(5):
#     for col in range(row + 1):
#         print("*", end="")
#     print()


# for row in range(6, 1, -1):
#     for col in range(row - 1):
#         print("*", end="")
#     print()


for row in range(5, 0, -1):
    for col in range(row):
        print("*", end="")
    print()

