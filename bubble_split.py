def bubble_sort(param):
    for i in range(len(param)):
        for j in range(len(param)-i-1):
            if param[j] > param[j+1]:
                param[j], param[j+1] = param[j+1], param[j]
    return (param)


def binary_search(array, element, left, right):
    try:
        middle = (right+left) // 2
        if (array[middle-1] < element) and (array[middle] >= element):
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle-1)
        else:
            return binary_search(array, element, middle+1, right)
    except RecursionError:
        print('Ошибка. Индекс соседей выходит за диапазон списка.')
        exit(0)
################################################################################


try:
    element = int(input("Введите число для сравнения. \n"))
except ValueError:
    print('Ошибка. Необходимо вводить целые числа.')
    exit(0)

sequence = input(
    "Введите последовательность целых чисел, разделенных пробелом. \n")
word_list = sequence.split()
array_int = []

for word in word_list:
    if word.isnumeric():
        array_int.append(int(word))
    if len(array_int) == 0:
        print('Ошибка. Необходимо вводить целые числа и  разделять их пробелами')
        exit(0)

array = (buble_sort(array_int))
print('Отсортированный список ')
print(array)

res = binary_search(array, element, 0, len(array_int)-1)
print('Номера индексов элементов списка, между которыми находится заданное число: ')
print(res-1, "<=>", res)
