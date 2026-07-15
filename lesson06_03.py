#is_tired = input("Are you tired? ").lower()

#if is_tired == "no":
    #print("You can study Python")
#else:
    #print("You should rest")


answer = input("Are you tired? ").lower()
is_tired = answer == "yes"
if not is_tired:
    print("You can study Python")
else:
    print("You should rest")