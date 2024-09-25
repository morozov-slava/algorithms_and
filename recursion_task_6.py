# 6. Печать элементов списка с чётными индексами
def get_zero_index():
    return 0

def print_even_indices_elements(array: list, index: int):
    if index < len(array):
        print(array[index])
        print_even_indices_elements(array, index+2)

array = [1, 2, 3, 4, 5]
print_even_indices_elements(array, get_zero_index())


### НОВОЕ РЕШЕНИЕ ###

def main(array: list):
    def print_even_indices_elements(array: list, index: int):
        if index >= len(array):
            return None
        if index % 2 == 0:
            print(array[index])
        print_even_indices_elements(array, index+2)
    return print_even_indices_elements(array, 0)
