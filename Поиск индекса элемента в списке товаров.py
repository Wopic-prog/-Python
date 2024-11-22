# TODO Напишите функцию для поиска индекса товара
def find_item_index(items, item):
    try:
        return items.index(item)  # Возвращаем индекс первого вхождения товара
    except ValueError:
        return None  # Если товар не найден, возвращаем None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции, чтобы получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
