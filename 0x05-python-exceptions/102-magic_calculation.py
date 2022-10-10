#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
<<<<<<< HEAD
        except Exeption:
=======
        except Exception:
>>>>>>> a6f1ca018c316ede420daa1d523c3abeb0e47d71
            result = b + a
            break
    return result
