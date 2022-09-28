"""
@author: meylan
Question 7 TP2
Execution
"""

from TempCelFar import Temp


def test():
    T1 = Temp()
    T1.farheneit = 68
    T1.far()
    assert T1.celsius == 20

    T2 = Temp()
    T2.celsius = 20
    T2.cel()
    assert T2.farheneit == 68


    T3 = Temp()
    T3.celsius = 0
    T3.cel()
    assert T3.farheneit == 32

    print("all test ok")


def main():
    T = Temp()
    temp = input("C ou F : ").upper()

    if temp == "C":
        T.farheneit = eval(input("Temperature a convertir en Celsius : "))
        T.far()
        print(T.celsius, "°C")

    elif temp == "F":
        T.celsius = eval(input("Temperature a convertir en farheneit : "))
        T.cel()
        print(T.farheneit, "°F")

    else:
        print("Wrong Input")
        exit(1)

if __name__ == '__main__':
    test()
