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


users = [
    {"name": "Alex",
     "age": 25
     },
    {"name": "Maria",
     "age": 30
     },
    {"name": "John",
     "age": 17
     }
]
def get_adults(users):
    adults = []
    for user in users:
        if user["age"] >= 18:
            
    return user

print(users)
