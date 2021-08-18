from typing import Union


class LiczbaSlownie:
    UNITS = [None, 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć',
        'dziesięć', 'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szestnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście']
    DZIESIATKI = [None, None, 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']
    SETKI = [None, 'sto', 'dwieście', 'trzysta', 'cztersta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset']
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

    def __init__(self, num):
        '''Argument value: 0<= num < 10**24'''
        if not isinstance(num, int) or num < 0 or  num >= 10**24:
            raise TypeError('A number must be positive integer!')
        self.num = num
        self.num_str = str(self.num)

    @staticmethod
    def odmien_rzeczownik(n, odmiany:Union[tuple[str, str, str], list[str, str, str]]):
        if not isinstance(odmiany, (tuple, list)) or len(odmiany) != 3:
            raise TypeError('Param "odmiany" must be tuple/list and must have 3 items!')
        if n == 0:
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
            return 'Zero'
        num_str_len = len(self.num_str)
        loop = -(-num_str_len//3)
        i = 1
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
        return str_res.capitalize()


if __name__ == "__main__":
    print(LiczbaSlownie(9010071172).slownie())
    print(LiczbaSlownie(901001172).slownie())
    print(LiczbaSlownie(10001011).slownie())
    print(LiczbaSlownie(10000011).slownie())
    

        

