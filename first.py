import os
import datetime as dt

def logger(old_function):

    def new_function(*args, **kwargs):
        date_now = dt.date.today()
        time_now = dt.datetime.now().strftime("%H:%M:%S")
        name_fun = old_function.__name__
        value = old_function(*args, **kwargs)
        result_list = [
            f'date: {date_now}\n',
            f'time: {time_now}\n',
            f'name_fun: {name_fun}\n',
            f'value: {value}\n',
            f'args: {args if args else "Args не переданы в функцию"}\n',
            f'kwargs: {kwargs if kwargs else "Kwargs не переданы в функцию"}\n'
        ]
        with open('main.log', 'a', encoding='utf-8') as f:
            f.writelines(result_list)
            f.write('\n')
        return value

    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)
    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()