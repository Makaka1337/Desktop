class fraction:
    def __init__(self,num:int=0,den:int=1):
        if type(num) != int or type(den) != int or den== 0:
            raise TypeError
        self.__numerator = num
        self.__denumerator = den
    def __str__(self):
        return str(self.__numerator)+'/'+str(self.__denumerator)
    def __gt__(self,right):
        return self.__numerator *right.__denumerator > right.__numerator *self.__denumerator
    def __lt__(self,right):
        return self.__numerator  * right.__denumerator  <  right.__numerator  * self.__denumerator
    def __le__(self,right):
        return self.__numerator  * right.__denumerator <= right.__numerator  * self.__denumerator
    def __ge__(self,right):
        return self.__numerator  * right.__denumerator  >= right.__numerator  * self.__denumerator
    def __ne__(self,right):
        return self.__numerator  * right.__denumerator != right.__numerator * self.__denumerator
    def __eq__(self,right):
        return self.__numerator  * right.__denumerator == right.__numerator  * self.__denumerator
    def __add__(self,right):
        return Fraction(self.__numerator * right.__denumerator + right.__numerator * self.__denumerator,right__denumerator*right.__denumerator)

#aasd
#asda

f1 = fraction(1,3)
f2 = fraction(1,4)

print(f1 > f2)
print(f1 < f2)
print(f1 <= f2)
print(f1 <= f2)
print(f1 != f2)
print(f1 == f2)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
