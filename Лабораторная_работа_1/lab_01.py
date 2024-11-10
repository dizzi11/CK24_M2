numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a = numbers[:4]
b = numbers[5:]
numbers_without_NONE = (a+b)
some_number = round(sum(numbers_without_NONE)/(len(numbers_without_NONE)+1),2)
numbers[4] = some_number


# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
