def get_balanced_bst(one_level_arrays: list):
    balanced_bst_array = []
    next_level_arrays = []
    for array in one_level_arrays:
        if len(array):
            mid_i = len(array) // 2
            balanced_bst_array.append(array[mid_i])
        if len(array) > 2: 
            next_level_arrays.append(array[:mid_i])
            next_level_arrays.append(array[mid_i+1:])
        elif len(array) == 2:
            next_level_arrays.append(array[:mid_i])
    if len(next_level_arrays):
        balanced_bst_array.extend(
            get_balanced_bst(next_level_arrays)
        )
    return balanced_bst_array
    

def GenerateBBSTArray(a: list):
    a = sorted(a)
    return get_balanced_bst([a])


