# Найти сумму произведений из списка словарей
import json

input_file = 'input.json'

def task() -> float:
    """Вычисляет сумму произведения значений по двум ключам"""
    with open(input_file) as file:
        data = json.load(file)

        value = [dict_['score'] * dict_['weight'] for dict_ in data]
        return round(sum(value), 3)

if __name__ == '__main__':
    print(task())