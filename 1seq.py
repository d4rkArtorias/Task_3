from unicodedata import numeric


elements_of_list = int(input("Введите количество элементов списка: "))
result = []
for elements in range(elements_of_list):
    element =  int(input("Введите число "))
    result.append(element)

result.sort()
print(result)