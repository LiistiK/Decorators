from logger import get_log
from log_path import log_constructor
from pprint import pprint


@get_log
def create_cook_book(input_file_name):
    cook_book = {}

    try:
        with open(input_file_name, encoding='utf-8') as f:
            lst = [line.strip() for line in f]
        for i, c in enumerate(lst):
            if c.isdigit():
                cook_book[lst[i-1]] = []
                for separator in lst[i+1:i+int(c)+1]:
                    ingredient_name = separator.split('|')[0]
                    quantity = int(separator.split('|')[1])
                    measure = separator.split('|')[2]

                    cook_book[lst[i-1]].append(
                        dict(ingredient_name=ingredient_name, quantity=quantity, measure=measure))
        return cook_book

    except FileNotFoundError:
        return (f'Файл: {input_file_name} не найден.')
    except Exception as error:
        return f'Ошибка - {error}'


if __name__ == '__main__':
    pprint(create_cook_book('giir.txt'))
