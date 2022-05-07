from datetime import datetime
import os

def log_constructor(file_name, file_path = None):
    if file_path is None:
        file_place = os.path.join(os.getcwd())
    else:
        file_place = os.path.join(os.path.abspath(file_path))

    file_path = os.path.join(file_place, file_name)

    def get_log_path(func):

        def fun(*args, **kwargs):
            date_time = datetime.now().strftime("%d %B %Y  time %H:%M:%S")
            func_name = func.__name__
            result = func(*args, **kwargs)
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result

        return fun

    return get_log_path
