#chiedere all- utente quante parole vuole inserire, permettere l'inserimento di un numero di parole
#e stampare la parola più corta senza utilizzare def 


#fallo con il while
i = 0
n = int(input("Quante parole vuoi inserire? "))
parole = []

while i < n:
    parola = input(f"Inserisci la parola {i + 1}: ")
    parole.append(parola)
    i += 1

parola_corta = parole[0]
i = 1

while i < n:
    if len(parole[i]) < len(parola_corta):
        parola_corta = parole[i]
    i += 1

print("La parola più corta è:", parola_corta)
