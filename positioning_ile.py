def custom_write(file_name, strings):
    # Словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл для записи в режиме 'w' с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            # Получаем текущую позицию в файле (номер байта)
            byte_position = file.tell()

            # Записываем строку в файл с переходом на новую строку
            file.write(string + '\n')

            # Добавляем информацию в словарь
            strings_positions[(line_number, byte_position)] = string

    # Возвращаем словарь с позициями строк
    return strings_positions


# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Вывод результата
for elem in result.items():
    print(elem)