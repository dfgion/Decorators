from first import logger

@logger
def in10(n):
    n_str = str(n)
    if '.' in n_str:
        #Переводим целую часть
        list_n = n_str.split('.')
        dict_n = {'start': [x for x in reversed(list_n[0])], 'end': [x for x in list_n[1]]}
        minus = 0
        if '-' in dict_n['start']:
            minus = '-'
            dict_n['start'].remove('-')
        start_10 = 0
        for index in range(0, (len(dict_n['start']))):
            start_10+=int(dict_n['start'][index])*(2**index)
        #Переводим число, которое получается после точки или же дробную часть
        index_list_end = 0
        end_10 = 0
        for index in range(1, len(dict_n['end'])+1):
            grade = 2**(-index)
            end_10+=int(dict_n['end'][index_list_end])*grade
            index_list_end+=1
        if minus == '-':
            return float(minus+str(start_10+end_10))
        return start_10+end_10
    else:
        if int(n_str) == 0:
            return 0
        list_n = [x for x in reversed(n_str)]
        minus = 0
        if '-' in list_n:
            minus = '-'
            list_n.remove('-')
        start_10 = 0
        for index in range(0, (len(list_n))):
            start_10+=int(list_n[index])*(2**index)
        if minus == '-':
            return int(minus+str(start_10))
        return start_10

@logger
def in6(number):
    number = in10(number)
    if number == 0:
        return 0
    n_str = str(number)
    minus = 0
    if '-' in n_str:
        minus = '-'
        number = -number
    if '.' in n_str:
        #Переводим целую часть
        list_n = str(number).split('.')
        n = ''
        number = int(list_n[0])
        while number > 0:
            n = n + str(number % 6)
            number = number // 6
        n =  list(reversed(n))
        start_number = ''.join(n)
        #Переводим число, которое получается после точки или же дробную часть
        fractional_part = float('0.' + list_n[1])
        end_number = '0.'
        while True:
            end_number = end_number + str(fractional_part*6)[:1]
            fractional_part = float('0.' + str(fractional_part*6)[2:])
            if fractional_part == 0:
                break    
        if minus == '-':
            return -(int(start_number)+float(end_number))
        return int(start_number)+float(end_number)
    else:
        n = ''
        k = ''
        while number > 0:
            n = n + str(int(number) % 6)
            number = number // 6
        n =  list(reversed(n))
        for j in range(len(n)):
            k += n[j]
        if minus == '-':
            return -int(k)
        return int(k)

if __name__ == "__main__":
    number = input('Введите число в двоичной системе счистления:\n')
    verify = {'0', '1', '.'}
    if (set(number) == {'0', '.'} or
        set(number) == {'0', '1', '-'} or
        set(number) == {'1', '-'} or
        set(number) == {'1', '.'} or
        set(number) == {'1', '.', '-'} or
        set(number) == {'1', '.', '-', '0'} or
        set(number) == verify or 
        set(number) == {'1'} or 
        set(number) == {'0'} or 
        set(number) == {'0', '1'}) and number.count('.') <= 1:
        if '-' in set(number):
            if number[0] != '-':
                raise 'Поставьте правильно минус'
        print(in6(float(number)))