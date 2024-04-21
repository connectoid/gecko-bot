import os
import re

def replace_tabs_with_spaces(directory):
    # Получаем список всех файлов в директории
    files = os.listdir(directory)
    
    for file in files:
        # Проверяем, является ли файл скрытым (чтобы его не обрабатывать)
        if not file.startswith('.'):
            with open(f'{directory}/{file}', 'r') as f:
                content = f.read()
            
            # Заменяем все символы табуляции на пробелы
            content = re.sub(' ', '\t', content)
            
            with open(f'{directory}/{file}', 'w') as f:
                f.write(content)

# Пример использования функции
replace_tabs_with_spaces('cookies')
