# 6. Печать элементов списка с чётными индексами
def print_even_indices_elements(array: list, index: int):
    if index >= len(array):
        return None
    if index % 2 == 0:
        print(array[index])
    print_even_indices_elements(array, index+1)

def main(array: list):
    return print_even_indices_elements(array, 0)


