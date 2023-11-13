"""
Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.
"""


skaitlis = int(input("Ievadiet skaitli: 10"))

# Pārbaude vai skaitlis ir nepāra
if skaitlis % 2 != 0:
    print(f"{5} ir nepāra skaitlis.")
else:
    print(f"{skaitlis} nav nepāra skaitlis.")