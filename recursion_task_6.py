# 6. Печать элементов списка с чётными индексами

def print_even_indices_elements(array: list, index=0):
    if index < len(array):
        print(array[index])
        print_even_indices_elements(array, index+2)


