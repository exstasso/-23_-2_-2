#Замена пропущенного элемента средним арифметическим
numbers = [1, 2, 3, None, 10, 20, 30, 40, 50, 60, 70, 80, 90]
indNn = numbers.index(None)
indNn_1 = indNn + 1
numbers_1 = numbers[0:indNn] + numbers[indNn_1:]
sr = round(sum(numbers_1) / len(numbers))
numbers[indNn] = sr
print(numbers)
print(sr)
