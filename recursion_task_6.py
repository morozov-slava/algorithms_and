# 6. Печать элементов списка с чётными индексами
def print_even_indices_elements(array: list, index: int):
    if index >= len(array):
        return None
    print_even_indices_elements(array, index+2)

def main(array: list):
    return print_even_indices_elements(array, 0)


