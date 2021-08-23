from typing import Union


class IntSlownie:
    UNITS = [None, 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć',
        'dziesięć', 'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szestnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście']
    DZIESIATKI = [None, None, 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']
    SETKI = [None, 'sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset']
    ODMIANY = [
        None,
        ['tysiąc', 'tysiące', 'tysięcy'],
        ['milion', 'miliony', 'milionów'],
        ['miliard', 'miliardy', 'miliardów'],
        ['bilion', 'biliony', 'bilionów'],
        ['biliard', 'biliardy', 'biliardów'],
        ['trylion', 'tryliony', 'trylionów'],
        ['tryliard', 'tryliardy', 'tryliardów'],
    ]

    def __init__(self, num:int):
        '''Argument value: -10**24 < num < 10**24'''
        to_power = len(self.ODMIANY)*3
        num_max = 10**to_power
        if not isinstance(num, int) or  abs(num) >= num_max:
            raise TypeError(f'A number must be integer in (-10**{to_power}, 10**{to_power})')
        self.positive = True if num > 0 else False
        self.num = abs(num)
        self.num_str = str(self.num)

    @staticmethod
    def odmien_rzeczownik(n, odmiany:Union[tuple[str, str, str], list[str, str, str]]):
        if not isinstance(odmiany, (tuple, list)) or len(odmiany) != 3:
            raise TypeError('Param "odmiany" must be tuple/list and must have 3 items!')
        elif n < 0:
            raise TypeError('Param "n" cannot be a negative number!')
        elif n == 0:
            return None
        elif n == 1:
            result = odmiany[0]
        elif 1 < n % 10 < 5:
            result = odmiany[1]
        else:
            result = odmiany[2]
        return result
                        
    def hundreds(self, n):
        '''words of number 0 < n < 1000'''
        s, unit = divmod(n, 100)
        if unit == 0:
            result = ''
        elif unit < 20:
            result = self.UNITS[unit]
        else:
            d, unit = divmod(unit, 10)
            result = self.DZIESIATKI[d] 
            if unit:
                result += f' {self.UNITS[unit]}' 
        if s:            
            if result:
                result = f'{self.SETKI[s]} {result}'
            else:
                result = self.SETKI[s]
        return result

    def slownie(self):
        if not self.num:
            return 'zero'
        num_str_len = len(self.num_str)
        loop = -(-num_str_len//3)
        #i = 1
        for i in range(loop):
            index_from = -(i+1)*3 if (i+3) < num_str_len else -num_str_len 
            index_to = -i*3
            if i == 0:
                t = int(self.num_str[index_from:])
                str_res = self.hundreds(t)
            else:
                t = int(self.num_str[index_from:index_to])
                odmiana = self.odmien_rzeczownik(t, self.ODMIANY[i]) if t != 0 else None 
                if odmiana:
                    str_res = self.hundreds(t) + ' ' + odmiana + ' ' + str_res            
        return str_res if self.positive else 'minus ' + str_res


def kwota_slownie(num):
    PLN = [('złoty', 'złote', 'złotych'), ('grosz', 'grosze', 'groszy')]
    to_power = len(IntSlownie.ODMIANY)*3
    num_max = 10**to_power
    if abs(num) >= num_max:
        raise TypeError(f'A number must be in (-10**{to_power}, 10**{to_power})')
    num = int(num*100)
    gr = int(abs(num) % 100)
    zl = int(((num - gr) if num >= 0 else (num + gr))/100)
    result = IntSlownie(zl).slownie() + ' ' + IntSlownie.odmien_rzeczownik(abs(zl), PLN[0])
    if gr:
        result += ' ' + IntSlownie(gr).slownie() + ' ' + IntSlownie.odmien_rzeczownik(gr, PLN[1])  
    return result