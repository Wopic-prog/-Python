numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим индекс пропущенного элемента (None)
missing_index = numbers.index(None)

# Вычислим сумму всех элементов, исключая пропущенное значение (None)
total_sum = sum(num for num in numbers if num is not None)

# Вычислим количество элементов, исключая пропуск (None)
count_without_missing = len([num for num in numbers if num is not None])+1

# Вычислим среднее арифметическое всех чисел, кроме пропуска
average = round(total_sum / count_without_missing, 2)

# Заменим пропущенный элемент на среднее арифметическое
numbers[missing_index] = average

print("Измененный список:", numbers)
