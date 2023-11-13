# Izvēlēties sveicienu atkarībā no stundas
if 6 <= pašreizējā_stunda < 12:
    sveiciens = "Labrīt!"
elif 12 <= pašreizējā_stunda < 18:
    sveiciens = "Labdien!"
else:
    sveiciens = "Labvakar!"

# Izvadīt rezultātu
print(sveiciens)