numbers = input("Введите числа через запятую ")
split_numbers = numbers.split(',')
result = []
for num in split_numbers:
    if numbers.count(num) == 1:
        result.append(num)
print(result)