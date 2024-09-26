# 8. Поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
# Для хождения по директориям используйте стандартную функцию. Результат выдавайте списком, List например.
import os

def get_all_catalog_files(path: str):
    catalog_files = []
    for file in os.listdir(path):
        current_path = os.path.join(path, file)
        if os.path.isdir(current_path):
            catalog_files.extend(get_all_catalog_files(current_path))
        else:
            catalog_files.append(file)
    return catalog_files


