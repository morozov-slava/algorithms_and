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
