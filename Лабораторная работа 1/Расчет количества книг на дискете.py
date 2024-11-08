# Параметры дискеты и книги
disk_size_mb = 1.44  # объем дискеты в Мб
disk_size_bytes = disk_size_mb * 1024 * 1024  # переводим объем дискеты в байты

# Параметры книги
pages_per_book = 100            # количество страниц в книге
lines_per_page = 50             # число строк на странице
chars_per_line = 25             # количество символов в строке
bytes_per_char = 4              # объем одного символа в байтах

# Вычисляем объем одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

# Вычисляем количество книг, которое можно поместить на дискету
books_on_disk = int(disk_size_bytes // book_size_bytes)  # округляем вниз до целого числа

print("Количество книг, помещающихся на дискету:", books_on_disk)
