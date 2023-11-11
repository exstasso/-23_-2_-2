#Поиск общих участков
def find_common_participants(first_group, second_group, splitter=','):
    first = first_group.split(splitter)
    second = second_group.split(splitter)
    result = list(set(first).intersection(set(second)))
    result.sort()
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

#participants_first_group = "Иванов,Петров,Сидоров"
#participants_second_group = "Петров,Сидоров,Смирнов"

#Проверка функции с разделителем в виде запятой
#print(f"Общие участники: {find_common_participants(participants_first_group, participants_second_group)}")

#Проверка функции с разделителем отличным от запятой
print(f"Общие участники: {find_common_participants(participants_first_group, participants_second_group, splitter='|')}")
