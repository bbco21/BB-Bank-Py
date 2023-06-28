import random
import os
while True:
    dobas1 = random.randint(1, 6)
    dobas2 = random.randint(1, 6)
    print(f"{dobas1}, {dobas2}")
    input("Nyomj entert a folytatashoz.")
    os.system("clear")
