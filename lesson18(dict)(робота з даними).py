def create_user(name, age):
    user = {
        "name": name,
        "age": age
    }
    return user
user = create_user("Anna", 20)
print(user)