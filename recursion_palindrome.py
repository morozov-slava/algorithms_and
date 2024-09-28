# Реализуйте функцию, проверяющую, является ли строка палиндромом, с использованием рекурсии
def is_palindrome_string(string: str, index: int):
    if index >= len(string) // 2:
        return True
    print(f"{string[index]} --- {string[-1*index-1]}") 
    if not string[index] == string[-1*index-1]:
        return False
    return is_palindrome_string(string, index+1)


