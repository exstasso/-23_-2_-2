# Конвертер из CSV в JSON формат
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    """Конвертер из CSV в JSON"""
     with open(INPUT_FILENAME, 'r') as file:
        with open(OUTPUT_FILENAME, 'w') as f:
            dict_reader = csv.DictReader(file)
            json_list = [row for row in dict_reader]

            json.dump(json_list, f, indent=4)

if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")