"""
@author: meylan
Question 9 TP2
execution
"""

from Q11 import racine

calc = racine()
print("ax² + bx + c = 0")
calc.get_data(float(input('a = ')),float(input('b = ')),float(input('c = ')))
print(f"Delta {calc.calc_delta()}")
calc.trait_delta()