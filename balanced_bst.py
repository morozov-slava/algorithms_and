def get_balanced_bst(array: list):
    if len(array) == 0:
        return []
    balanced_bst = []
    root_index = len(array) // 2
    balanced_bst.append(array[root_index])
    balanced_bst.extend(
        get_balanced_bst(array[:root_index])
    )
    balanced_bst.extend(
        get_balanced_bst(array[root_index+1:])
    )
    return balanced_bst

def GenerateBBSTArray(a: list):
    a = sorted(a)
    return get_balanced_bst(a)


