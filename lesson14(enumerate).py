# fruits = ["apple", "banana", "orange"]
#
# for index, fruit in enumerate(fruits, start=1):  #start=1 - перерахувати #нумерація з одного
#     print(index, fruit)


# fruits = ["apple", "banana", "orange"]
#
# for i in range(len(fruits)):
#     print(i, fruits[i])

animals = ["dog", "cat", "bird", "horse"]
for index, animal in enumerate(animals, start=1):
    #print(index, animal) #без крапки
    #print(index, ".", animal) #з крапкою і пробілом
    #print(f"{index}.{animal}") #база
    print(index, animal, sep=". ") #separator - роздільник

# animals = ["dog", "cat", "bird", "horse"]
# for animal in enumerate(animals, start=1):
#     print(animal)