# 6. Печать элементов списка с чётными индексами
def print_even_indices_elements(array: list, index: int):
    if index < len(array):
        print(array[index])
        print_even_indices_elements(array, index+2)

START_INDEX = 0
array = [1, 2, 3, 4, 5]
print_even_indices_elements(array, START_INDEX)

