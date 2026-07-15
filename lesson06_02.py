username = input("Enter username: ").lower()
password = input("Enter password: ") #У реальних програмах паролі не зберігають прямо в коді!

if username == "denys" and password == "1234":
    print("Access granted")
else:
    print("Wrong username or password.") #