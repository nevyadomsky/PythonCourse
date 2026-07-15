# def create_user(name, age):
#     user = {
#         "name": name,
#         "age": age
#     }
#     return user
# user = create_user("Anna", 20)
# print(user)

# Множина (set):
#   colors = {"red", "blue", "green"}
# Словник (dict):
#    user = {
#        "name": "Anna",
#        "age": 20
#    }        # Пари: ключ → значення


# def create_user(name, age):
#     user = {
#         "name": name,
#         "age": age
#     }
#     return user
# user = create_user("Anna", 20)
# print(user)


# def create_user(name, age):
#     return {
#         "name": name,
#         "age": age
#     }
# user = create_user("Anna", 20)
# print(user)


# users = [
#     {"name": "Alex",
#      "age": 25
#      },
#     {"name": "Maria",
#      "age": 30
#      },
#     {"name": "John",
#      "age": 17
#      }
# ]
# def get_adults(users):
#     adults = []
#     for user in users:
#         if user["age"] >= 18:
#             adults.append(user)
#     return adults
#
# print(get_adults(users))


# users = [
#     {"name": "Alex",
#      "age": 25
#      },
#     {"name": "Maria",
#      "age": 30
#      },
#     {"name": "John",
#      "age": 17
#      }
# ]
# def find_user(users, name):
#     for user in users:
#         if user["name"] == name:
#             return user            #return означає:"Зупини функцію і віддай результат назад"
#     return None
# print (find_user(users, "Maria"))
# print (find_user(users, "Bob"))


# def find_big_number(numbers):
#     for number in numbers:
#         if number > 10:
#             return number
#     return None
# numbers = [3, 7, 12, 5, 20]
# print(find_big_number([1, 2, 3]))


# def find_word(words, target):
#     for word in words:
#         if word == target:
#             return word
#     return None
#
# words = ["cat", "dog", "bird"]
# result = find_word
# print(result(words, "fish"))
# print(result(words, "cat"))
# print(find_word(words, "fish"))
# print(find_word(words, "cat"))


# passwords = [
#     "abc123",
#     "hello",
#     "python2026"
# ]
# def check_password(passwords, password):
#     for saved_password in passwords:
#         if saved_password == password:
#             return "Access granted"
#     return "Access denied"
# print(check_password(passwords, "hello"))
# print(check_password(passwords, "bye"))



products = [
    {
        "name": "Mouse",
        "price": 50
    },
    {
        "name": "Keyboard",
        "price": 100
    },
    {
        "name": "Monitor",
        "price": 300
    }
]
def find_expensive_product(products):
    expensive_product = None
    for product in products:
        if expensive_product is None:
            expensive_product = product
        elif product["price"] > expensive_product["price"]:
            expensive_product = product
    return product
print(find_expensive_product(products))