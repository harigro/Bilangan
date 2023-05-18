# angka romawi
from typing import Union, List, Literal

class Romawi:
    def __init__(self):
        angka = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        simbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        self.romawi = dict(zip(angka, simbol))

class Desimal:
    def __init__(self, des: Union[int, float]):
        self.desimal = des
    
    def to_romawi(self) -> str:
        romawi = Romawi().romawi
        nomor_romawi = ""
        for value, numeral in romawi.items():
            while self.desimal >= value:
                nomor_romawi += numeral
                self.desimal -= value
        return nomor_romawi

class KPK:
    def __init__(self, satu: Union[int, float], dua: Union[int, float]):
        self.satu = satu
        self.dua = dua

    def kpk(self):
        if self.dua == 0:
            return self.satu
        else:
            return KPK(self.dua, self.satu % self.dua).kpk()

class Prima:
    def __init__(self, pp: int):
        self.prima = pp

    def is_prima(self) -> Literal[bool]:
        if self.prima < 2:
            return False
        elif self.prima % 2 == 1:
            return True
        else:
            return False

class Fibo:
    def __init__(self, ff: int):
        self.fib = ff

    def fibo(self) -> List[int]:
        if self.fib <= 0:
            return []
        elif self.fib == 1:
            return [0]
            
        elif self.fib == 2:
            return [0, 1]

        else:
            fibs = [0, 1]
            for x in range(2, self.fib):
                fibs.append(fibs[-1] + fibs[-2])
            return fibs

if __name__=="__main__":
    bb = Prima(4).is_prima()
    print(bb)













