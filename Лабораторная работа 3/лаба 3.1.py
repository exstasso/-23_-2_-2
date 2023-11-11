#Поиск индекса элемента в списке товаров
def find_index(items, item_find):
    for index, item in enumerate(items):
        if item == item_find:
            return index

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
items_find = ['банан', 'груша', 'персик']

for find_item in items_find:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
