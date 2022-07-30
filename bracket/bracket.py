"""
Дано целое число n.
Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n, упорядоченные лексикографически.
В задаче используются только круглые скобки.

Формат ввода

Единственная строка входного файла содержит целое число n, 0 ≤ n ≤ 11

Формат вывода

Выходной файл содержит сгенерированные правильные скобочные последовательности, упорядоченные лексикографически.
"""

# Рекурсивная функция для создания скобочных последовательностей
def writeBracket(num, output_file, write="", left=0, right=0):
    if left == num and right == num:
        output_file.write(write + "\n")
    else:
        if left < num:
            writeBracket(num, output_file, write + "(", left + 1, right)
        if right < left:
            writeBracket(num, output_file, write + ")", left, right + 1)


def createBracket():
    with open(f"bracket/input.txt", "r") as input_file:
        num = int(input_file.readline().strip())

        with open(f"bracket/output.txt", "w") as output_file:
            writeBracket(num=num, output_file=output_file)
