"""
Izveidojiet Python programmu, kas izmanto while ciklu, lai atrastu pirmo skaitli, kura kvadrāts ir lielāks par 1000.]
"""
# Sākuma skaitlis
skaitlis = 1

# while cikls, kamēr kvadrāts nav lielāks par 1000
while skaitlis**2 <= 1000:
    skaitlis += 1

print(f"Pirmais skaitlis, kura kvadrāts ir lielāks par 1000, ir: {skaitlis}")