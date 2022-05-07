from datetime import datetime

def get_log(func):

    def fun(*args, **kwargs):
        date_time = datetime.now()
        func_name = func.__name__
        result = func(*args, **kwargs)
        with open('_file.txt', 'w', encoding='utf-8') as file:
            file.write(f'Дата/время: {date_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Результат: {result}\n')
        return result

    return fun

