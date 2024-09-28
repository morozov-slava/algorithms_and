# Реализуйте функцию, проверяющую, является ли строка палиндромом, с использованием рекурсии
def is_palindrome_string(string: str):
    if len(string) <= 1:
        return True
    if not string[0] == string[-1]:
        return False
    return is_palindrome_string(string[1:-1])


