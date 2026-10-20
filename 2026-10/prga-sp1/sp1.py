# IT2-04
# 20. 10. 2026
# Program nechá kuličku jet doprava a zpět a pak vypíše tabulku čísel, jejich druhých mocnin a odmocnin.

import time
import math

pocet = 8

print("Kulička jede.")

for i in range(pocet):
    print(" " * i + "O")
    time.sleep(0.1)

for i in range(pocet):
    print(" " * (pocet - i) + "O")
    time.sleep(0.1)

print("Tabulka")

for i in range(1, pocet + 1):
    print(i, i * i, math.sqrt(i))
