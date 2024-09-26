# 7. Нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны).
# Второе макс. -- это когда отсортировали список и берём второй элемент (отсчитывая с 1), если 5,4,3,2,5 например, то второе макс. должно получиться 5. 
# Равенство или неравенство элементов значения не имеет, т.к. оно никак в условии не оговаривается. После того как вы отсортировали массив [2,5,4,3,5] по убыванию [5,5,4,3,2] 
# берёте второй элемент 5, это и будет второе макс. Если массив [2,3,5,4], то второе макс будет 4, и т. д.

def find_second_max_number(max_number: int, second_max_number: int, index: int):
    if index >= len(array):
        return second_max_number
    if array[index] > max_number:
        second_max_number = max_number
        max_number = array[index]
    elif array[index] == max_number:
        second_max_number = max_number
    elif array[index] > second_max_number:
        second_max_number = array[index]
    return find_second_max_number(max_number, second_max_number, index+1)

def main(array: list):
    return find_second_max_number(array[0], array[0], 0)


