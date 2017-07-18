#!/usr/bin/python
# Листинг №5
if None or '' or False or int(0) : 
    print(True)    # не вернет True
else: print(False) # вернет False
# Или, что тоже:
X = None
if X or '' or (X != X) or int(0): 
    print(True)    # не вернет True
else: print(False) # вернет False, т.к.
# (X - не сущетвует) = (Х - не равен себе)
# (значение Х - ноль) = (Х - не равен себе)
