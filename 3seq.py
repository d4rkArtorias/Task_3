numbers = input("Введите числа через запятую ")
split_numbers = numbers.split(',')
numbers_2 = input("Введите числа через запятую ")
split_numbers = numbers.split(',')
for num in split_numbers[:]:
    if num in numbers_2:
        split_numbers.remove(num)
print(split_numbers)