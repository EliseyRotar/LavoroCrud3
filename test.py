


# Scrivere un programma che chiede all'utente di inserire un numero n e poi chiede all'utente di inserire n parole. Il programma deve stampare la parola più corta tra quelle inserite dall'utente. Se ci sono più parole con la stessa lunghezza minima, il programma deve stampare la prima parola inserita dall'utente tra quelle con lunghezza minima.  

n = int(input("Inserisci un numero: "))
if n < 0:
    print("Errore")
else:
    if n == 0:
        print("Errore")
    else:
        parole = []
        for i in range(n):
            parola = input("Inserisci una parola: ")
            parole.append(parola)
        if len(parole) < n:
            print("Errore")
        else:
            if len(parole) > n:
                print("Errore")
            else:
                lunghezza_minima = len(parole[0])
                parola_minima = parole[0]
                for parola in parole:
                    if len(parola) < lunghezza_minima:
                        lunghezza_minima = len(parola)
                        parola_minima = parola
                print(parola_minima)


