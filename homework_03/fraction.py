from math import gcd

class fraction(object):
    def __init__(self, a:int, b:int) -> object:
        # print("Annotations:",fraction.__init__.__annotations__)
        # print("Arguments:",'numerator' ,'denominator')
        a = a//gcd(a,b)
        b = b//gcd(a,b)
        self.numerator = a #1) self. 而非 fraction.
        self.denominator = b
        # fraction.numerator = a 所有fraction类生成的实例的numerator属性值全置为a
        # fraction.denominator = b 所有fraction类生成的实例的numerator属性值全置为b
    if __name__ == '__main__':
        # 2)对fraction类重载运算符
        def __str__(self):
            if self.denominator == 1:
                return str(self.numerator)
            else:
                return '%s/%s' % (self.numerator, self.denominator)
    
        def __repr__(self):
            return '%s(%s, %s)' % (self.__class__.__name__,
                                   self.numerator, self.denominator)        

        def __add__(self, other):
            fz = self.numerator * other.denominator + self.denominator * other.numerator
            fm = self.denominator * other.denominator
            yue = gcd(fz, fm)
            result = fraction(fz//yue, fm//yue)
            return result

        def __sub__(self, other):
            fz = self.numerator * other.denominator - self.denominator * other.numerator
            fm = self.denominator * other.denominator
            yue = gcd(fz, fm)
            result = fraction(fz//yue, fm//yue)
            return result

        def __mul__(self, other):
            fz = self.numerator * other.numerator
            fm = self.denominator * other.denominator
            yue = gcd(fz, fm)
            result = fraction(fz//yue, fm//yue)
            return result

        def __truediv__(self, other):
            other_ = fraction(other.denominator,other.numerator)
            result = self * other_
            return result
