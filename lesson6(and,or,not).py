age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? ").lower() #перший варіант на маленьку букву

#if age >= 18 and (has_ticket == "Yes" or has_ticket == "yes"): #другий
#if age >= 18 and has_ticket == "Yes".lower():
if age >= 18 and has_ticket == "yes":
    print("You can enter")
else:
    print("Sorry, you cannot enter")