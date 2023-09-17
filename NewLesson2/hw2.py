from fractions import Fraction

def fract_add(f1, f2):
    a, b = f1.split('/')
    c, d = f2.split('/')
    return str(Fraction(int(a), int(b)) + Fraction(int(c), int(d)))

def fract_mult(f1, f2):
    a, b = f1.split('/') 
    c, d = f2.split('/')
    return str(Fraction(int(a), int(b)) * Fraction(int(c), int(d)))
    
f1 = input("Введите дробь f1 в формате 'a/b': ")
f2 = input("Введите дробь f2 в формате 'c/d': ")

print(fract_add(f1, f2))
print(fract_mult(f1, f2))

# проверка 
f1 = Fraction(f1)
f2 = Fraction(f2)
print(f1 + f2)
print(f1 * f2)