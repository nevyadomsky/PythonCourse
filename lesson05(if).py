#if означає "якщо"
#Після : Python очікує блок коду з відступом
#> більше, < менше, >= більше або дорівнює, <=	менше або дорівнює, ==	дорівнює, != не дорівнює
#else — інакше

age = int(input("How old are you? "))
if age < 0:
    print("Invalid age.")
elif age < 13:
    print("You are child.")
elif 13 <= age <= 17:
    print("You are teenager")
else:
    print("You are an adult.")
