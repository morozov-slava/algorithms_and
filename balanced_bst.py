def get_balanced_bst(arr: list, start: int, end: int):
    if start > end:
        return []
    balanced_bst = []
    mid = start + (end - start) // 2
    balanced_bst.append(arr[mid])
    balanced_bst = get_balanced_bst(arr, start, mid - 1) + balanced_bst
    balanced_bst = balanced_bst + get_balanced_bst(arr, mid + 1, end) 
    return balanced_bst

def GenerateBBSTArray(a: list):
    a = sorted(a)
    return get_balanced_bst(a, 0, len(a)-1)


