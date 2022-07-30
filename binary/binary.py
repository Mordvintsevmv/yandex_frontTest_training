"""

Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.
Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.

Формат ввода

Первая строка входного файла содержит одно число n, n ≤ 10000.
Каждая из следующих n строк содержит ровно одно число — очередной элемент массива.

Формат вывода

Выходной файл должен содержать единственное число — длину самой длинной последовательности единиц во входном массиве.

"""

def getBinaryCount():
    with open(f"binary/input.txt", "r") as input_file:

        # Считываем количество символов
        num = int(input_file.readline().strip())

        # Максимальная длина ряда за всё время
        max_length = 0

        # Длина текущего ряда
        count = 0

        for i in range(num):
            if input_file.readline().strip() == "1":
                count += 1
                if count > max_length:
                    max_length = count
            else:
                count = 0

        with open(f"binary/output.txt", "w") as output_file:
            output_file.write(str(max_length))

