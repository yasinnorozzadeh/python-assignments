class Fraction():
    def __init__ (self, numerator = None, denominator = None):
        self.numerator = numerator
        self.denominator = denominator
    def sum(self, d2):
        sum = Fraction()
        sum.numerator = (self.numerator * d2.denominator) + (d2.numerator * self.denominator)
        sum.denominator = self.denominator * d2.denominator
        return sum
    def sub(self, d2):
        sub = Fraction()
        sub.numerator =  (self.numerator * d2.denominator) - (d2.numerator * self.denominator)
        sub.denominator = self.denominator * d2.denominator
        return sub
    def mul(self, d2):
        mul = Fraction()
        mul.numerator = self.numerator * d2.numerator
        mul.denominator = self.denominator * d2.denominator
        return mul
    def div(self, d2):
        div = Fraction()
        div.numerator = self.numerator * d2.denominator
        div.denominator = self.denominator * d2.numerator
        return div
    def result(self):
        print(self.numerator, "/", self.denominator)
while True:
    d1 = Fraction(int(input("numerator1:\t")), int(input("denominator1:\t")))
    d2 = Fraction(int(input("numerator2:\t")), int(input("denominator2:\t")))
    op = int(input("1: sum\n2: sub\n3: mul\n4: div\n5: exit\nenter operation:\t"))
    if op == 1:
        d1.sum(d2).result()
    elif op == 2:
        d2.sub(d2).result()
    elif op == 3:
        d1.mul(d2).result()
    elif op == 4:
        div = d1.div(d2)
        div.result()
    elif op == 5:
        exit()
    else:
        print("select number from list")
