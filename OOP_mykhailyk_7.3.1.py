import math

class RationalError(ZeroDivisionError):
    def __init__(self, message="Denominator cannot be zero."):
        super().__init__(message)

class Rational:
    def __reduce(self, a, b):
        k = math.gcd(a, b)
        self.a = a // k
        self.b = b // k

    def __init__(self, a, b=None):
        if isinstance(a, Rational):
            self.a = a.a
            self.b = a.b
        elif isinstance(a, int) and isinstance(b, int):
            if b == 0:
                raise RationalError()  # використання власного винятку
            self.a = a
            self.b = b
        elif isinstance(a, str):
            if '/' in a:
                self.a, self.b = map(int, a.split("/"))
            else:
                self.a = int(a)
                self.b = 1
        else:
            raise RationalValueError("Invalid input for Rational constructor.")

        if self.b == 0:
            raise RationalError()
        self.__reduce(self.a, self.b)

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise RationalValueError("Can only add Rational to Rational.")
        nom = self.a * other.b + self.b * other.a
        den = self.b * other.b
        return Rational(nom, den)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise RationalValueError("Can only subtract Rational from Rational.")
        nom = self.a * other.b - self.b * other.a
        den = self.b * other.b
        return Rational(nom, den)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise RationalValueError("Can only multiply Rational by Rational.")
        nom = self.a * other.a
        den = self.b * other.b
        return Rational(nom, den)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise RationalValueError("Can only divide Rational by Rational.")
        if other.a == 0:
            raise RationalError("Division by zero.")
        nom = self.a * other.b
        den = self.b * other.a
        return Rational(nom, den)

    def __call__(self):
        return self.a / self.b

    def __getitem__(self, key):
        if key == "n":
            return self.a
        elif key == "d":
            return self.b
        else:
            raise KeyError("Only 'n' and 'd' are valid keys.")

def fileopen(filename):
    spisok = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data = line.split()
            result = Rational(0, 1)
            operation = '+'
            for item in data:
                if item == '+':
                    operation = '+'
                elif item == '-':
                    operation = '-'
                elif item == '*':
                    operation = '*'
                else:
                    try:
                        rat_num = Rational(item)
                        if operation == '+':
                            result += rat_num
                        elif operation == '-':
                            result -= rat_num
                        elif operation == '*':
                            result *= rat_num
                    except (RationalError, RationalValueError) as e:
                        print("Error:", e)
            spisok.append(result)
    return spisok

if __name__ = "__main__":
    r1 = Rational(3, 4)  # 3/4
    r2 = Rational("2/5")  # 2/5
    r3 = Rational("7")  # 7/1
    r4 = Rational(r1)  # копія 3/4
    print(r1, r2, r3, r4)  # Виведе: 3/4 2/5 7/1 3/4
