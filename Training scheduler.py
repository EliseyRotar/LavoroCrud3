from os import system
import time
import winsound
 
# Programma crea la tua scheda allenamento (timer)
 
allenamento1 = {
    "NomeAllenamento": "crazy",
    "GruppoAllenante": "Schiena",
    "TempoRiscaldamento": 0,  # secondi
}
 
esercizio1 = {
    "NomeEsercizio": "Push-up",
    "TempoAllenamento": 10,
    "Serie": 2,
    "TempoRiposo": 2
}
 
superset1 = {
    "NomeEsercizio1": "Push-up",
    "NomeEsercizio2": "curl",
    "TempoAllenamento1": 10,
    "TempoAllenamento2": 23,
    "Serie": 2,
    "TempoRiposo1": 2,
    "TempoRiposo2": 6
}
 
esercizio2 = {
    "NomeEsercizio": "Tiger push-up",
    "TempoAllenamento":20,
    "Serie": 1,
    "TempoRiposo": 2
}
 
esercizi = [esercizio1, esercizio2]
allenamenti = [allenamento1]
supersett = [superset1]
scheda1 = [allenamento1, esercizio1, esercizio2, superset1]
 
schede = [scheda1]
 
def creaEsercizio():
    try:
        nomeEsercizio = input("Inserire il nome dell'esercizio: ")
        tempoAllenamento = int(input("Inserisci il tempo richiesto per questo esercizio: "))
        numeroSerie = int(input("Inserire il numero di serie: "))
        tempoRiposo = int(input("Inserire il tempo di riposo tra le serie: "))
        esercizio = {
            "NomeEsercizio": nomeEsercizio,
            "TempoAllenamento": tempoAllenamento,
            "Serie": numeroSerie,
            "TempoRiposo": tempoRiposo
        }
        return esercizio
    except ValueError:
        print("Errore: inserisci un valore valido.")
        return None
 
def creaAllenamento():
    try:
        nomeAllenamento = input("Inserire il nuovo nome dell'allenamento: ")
        gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
        tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
        if tempoRiscaldamento < 0:
            raise ValueError("Il tempo di riscaldamento non può essere negativo.")
       
        allenamento = {
            "NomeAllenamento": nomeAllenamento,
            "GruppoAllenante": gruppoAllenante,
            "TempoRiscaldamento": tempoRiscaldamento
        }
        return allenamento
    except ValueError as e:
        print(f"Errore di input: {e}")
        return None
 
def creaSuperSet():
    try:
        NomeEsercizio1 = input("Inserire il nome del primo esercizio: ")
        NomeEsercizio2 = input("Inserisci il nome del secondo esercizio: ")
        TempoAllenamento1 = int(input("Inserisci il tempo del primo esercizio: "))
        TempoAllenamento2 = int(input("Inserisci il tempo del secondo esercizio: "))
        Serie = int(input("Inserisci il numero di serie: "))
        TempoRiposo1 = int(input("Inserisci il tempo di recupero del primo esercizio: "))
        TempoRiposo2 = int(input("Inserisci il tempo di recupero del secondo esercizio: "))
 
        if TempoAllenamento1 <= 0 or TempoAllenamento2 <= 0 or Serie <= 0 or TempoRiposo1 < 0 or TempoRiposo2 < 0:
            raise ValueError("I tempi e le serie devono essere maggiori di zero.")
       
        superSet = {
            "NomeEsercizio1": NomeEsercizio1,
            "NomeEsercizio2": NomeEsercizio2,
            "TempoAllenamento1": TempoAllenamento1,
            "TempoAllenamento2": TempoAllenamento2,
            "Serie": Serie,
            "TempoRiposo1": TempoRiposo1,
            "TempoRiposo2": TempoRiposo2
        }
        return superSet
    except ValueError as e:
        print(f"Errore di input: {e}")
        return None
 
def vediEsercizio(esercizio):
    print(f'{esercizio["NomeEsercizio"]:<15}|{esercizio["TempoAllenamento"]:<15}|{esercizio["TempoRiposo"]:<15}|{esercizio["Serie"]:<15}')
 
def vediScheda(nomeScheda: dict):
    try:
        if nomeScheda is None or not nomeScheda:
            raise ValueError("La scheda non esiste o è vuota.")
       
        print(f'{"NomeAllenamento: " + nomeScheda["NomeAllenamento"]:<15} - {"GruppoAllenante: " + nomeScheda["GruppoAllenante"]:<15} - {"TempoRiscaldamento: "+ str(nomeScheda["TempoRiscaldamento"]):<15}')
   
    except ValueError as e:
        print(f"Errore: {e}")
    except KeyError:
        print("Errore: La chiave 'GruppoAllenante' non esiste nella scheda.")
    except Exception as e:
        print(f"Errore imprevisto: {e}")
 
def vediSchede(Schede: list):
    try:
        if not Schede:
            raise ValueError("Non ci sono schede disponibili.")
       
        print("Ecco l'elenco delle schede esistenti:")
        for scheda in Schede:
            vediScheda(scheda[0])
   
    except ValueError as e:
        print(f"Errore: {e}")
 
def modificaEsercizio(esercizio: dict):
    try:
        if esercizio is None:
            raise ValueError("L'esercizio non esiste o è vuoto.")
       
        nomeEsercizio = input("Inserisci il nome dell'esercizio: ")
        tempoAllenamento = int(input("Inserisci il tempo richiesto per questo esercizio: "))
        numeroSerie = int(input("Inserire il numero di serie: "))
        if numeroSerie <= 0:
            raise ValueError("Il numero di serie deve essere maggiore di zero.")
       
        tempoRiposo = int(input("Inserire il tempo di riposo tra le serie: "))
        if tempoRiposo < 0:
            raise ValueError("Il tempo di riposo non può essere negativo.")
       
        esercizio.update({
            "NomeEsercizio": nomeEsercizio,
            "TempoAllenamento": tempoAllenamento,
            "Serie": numeroSerie,
            "TempoRiposo": tempoRiposo
        })
        return esercizio
    except ValueError as e:
        print(f"Errore di input: {e}")
        return None
 
def modificaScheda(scheda):
    try:
        if scheda is None:
            raise ValueError("La scheda non esiste.")
       
        gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
        tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
        if tempoRiscaldamento < 0:
            raise ValueError("Il tempo di riscaldamento non può essere negativo.")
       
        scheda["GruppoAllenante"] = gruppoAllenante
        scheda["TempoRiscaldamento"] = tempoRiscaldamento
        print("Scheda aggiornata con successo.")
   
    except ValueError as e:
        print(f"Errore di input: {e}")
 
def modificaSuperSet(superset):
    try:
        if superset is None:
            raise ValueError("Il superset non esiste.")
       
        NomeEsercizio1 = input("Inserire il nome del primo esercizio: ")
        NomeEsercizio2 = input("Inserisci il nome del secondo esercizio: ")
        TempoAllenamento1 = int(input("Inserisci il tempo del primo esercizio: "))
        TempoAllenamento2 = int(input("Inserisci il tempo del secondo esercizio: "))
        Serie = int(input("Inserisci il numero di serie: "))
        TempoRiposo1 = int(input("Inserisci il tempo di recupero del primo esercizio: "))
        TempoRiposo2 = int(input("Inserisci il tempo di recupero del secondo esercizio: "))
 
        if TempoAllenamento1 <= 0 or TempoAllenamento2 <= 0 or Serie <= 0 or TempoRiposo1 < 0 or TempoRiposo2 < 0:
            raise ValueError("I tempi e le serie devono essere maggiori di zero.")
       
        superset.update({
            "NomeEsercizio1": NomeEsercizio1,
            "NomeEsercizio2": NomeEsercizio2,
            "TempoAllenamento1": TempoAllenamento1,
            "TempoAllenamento2": TempoAllenamento2,
            "Serie": Serie,
            "TempoRiposo1": TempoRiposo1,
            "TempoRiposo2": TempoRiposo2
        })
        return superset
    except ValueError as e:
        print(f"Errore di input: {e}")
        return None
 
def rimuoviEsercizio(lista: list):
    try:
        if not lista:
            raise ValueError("La lista degli esercizi è vuota.")
       
        vediScheda(lista)
       
        try:
            indice = int(input("Inserisci l'indice dell'esercizio da eliminare: "))
            if indice < 0 or indice >= len(lista):
                raise IndexError("Indice fuori dai limiti. Inserisci un indice valido.")
           
            lista.pop(indice)
            print("L'esercizio è stato rimosso con successo.")
       
        except ValueError:
            print("Errore: L'indice deve essere un numero intero.")
        except IndexError as e:
            print(f"Errore: {e}")
   
    except ValueError as e:
        print(f"Errore: {e}")
 
def rimuoviScheda(lista: list):
    try:
        if not lista:
            raise ValueError("La lista delle schede è vuota.")
       
        scelta = input("Sei sicuro di eliminare la tua scheda di allenamento? (Si/No): ")
        if scelta.lower() == "si":
            del lista[:]
            print("La scheda è stata eliminata.")
        else:
            print("Eliminazione della scheda annullata.")
   
    except ValueError as e:
        print(f"Errore: {e}")
 
def timer(n):
    t = n
    while n:
        if n == t:
            print(n)
            n -= 1          
            winsound.Beep(1000, 1000)
        elif n == 5:
            print("Mancano 5 secondi SPINGI UOMO")
            n -= 1          
            winsound.Beep(600, 1000)
        elif n == 3 or n == 1:
            print(n)
            n -= 1
            winsound.Beep(600, 1000)
        elif n == 0:
            break
        else:
            print(n)
            time.sleep(1)
            n -= 1
        system('cls')  
 
def timerEsercizio(esercizio: dict):
    for count in range(1, esercizio["Serie"] + 1):
        print(f"Inizio serie {count}")
        timer(esercizio["TempoAllenamento"])
        if count < esercizio["Serie"]:
            print("Inizio riposo")
            timer(esercizio["TempoRiposo"])
 
def start(Scheda: list):
    print("Inizio riscaldamento!")
    timer(Scheda[0]["TempoRiscaldamento"])
    for esercizio in Scheda[1:]:
        timerEsercizio(esercizio)
 
def menu():
    while True:
        print("\n" + "*" * 50)
        print("*" + " " * 48 + "*")
        print("*    BENVENUTO IN TRAINING SCHEDULER             *")
        print("*" + " " * 48 + "*")
        print("*" * 50)
        print("\n" + "-" * 20 + " MENU PRINCIPALE " + "-" * 20)
        print("01.  Crea nuovo esercizio")
        print("02.  Crea nuovo allenamento")
        print("03.  Crea nuovo superset")
        print("04.  Visualizza esercizi")
        print("05.  Visualizza allenamenti")
        print("06.  Visualizza superset")
        print("07.  Modifica esercizio")
        print("08.  Modifica allenamento")
        print("09.  Modifica superset")
        print("10. Rimuovi esercizio")
        print("11. Rimuovi allenamento")
        print("12. Rimuovi superset")
        print("13. Avvia timer allenamento")
        print("14. Gestisci schede")
        print("15. Esci")
        print("\n" + "-" * 50)
        scelta = input("Inserisci il numero corrispondente all'azione che vuoi eseguire: ")
       
        if scelta == "1":
            esercizio = creaEsercizio()
            if esercizio:
                esercizi.append(esercizio)
                print("Esercizio creato con successo")
                   
        elif scelta == "2":
            allenamento = creaAllenamento()
            if allenamento:
                allenamenti.append(allenamento)
                print("Allenamento creato con successo")
                   
        elif scelta == "3":
            s = creaSuperSet()
            if s:
                supersett.append(s)
                print("Superset creato con successo")
                   
        elif scelta == "4":
            for esercizio in esercizi:
                print(f'{"NomeEsercizio: " + esercizio["NomeEsercizio"]:<15} - {"TempoAllenamento: " + str(esercizio["TempoAllenamento"]):<15} - {"Serie: "+ str(esercizio["Serie"]):<15}')
       
        elif scelta == "5":
            for allenamento in allenamenti:
                vediScheda(allenamento)
       
        elif scelta == "6":
            for s in supersett:
                print(s)
       
        elif scelta == "7":
            nome = input("Inserisci il nome dell'esercizio da modificare: ")
            for esercizio in esercizi:
                if esercizio["NomeEsercizio"] == nome:
                    modificaEsercizio(esercizio)
                    print("Esercizio modificato con successo")
                    break
            else:
                print("Esercizio non trovato")
       
        elif scelta == "8":
            nome = input("Inserisci il nome dell'allenamento da modificare: ")
            for allenamento in allenamenti:
                if allenamento["NomeAllenamento"] == nome:
                    modificaScheda(allenamento)
                    print("Allenamento modificato ")
                    break
            else:
                print("Allenamento non trovato")
       
        elif scelta == "9":
            nome = input("Inserisci il nome del superset da modificare: ")
            for superset in supersett:
                if superset["NomeEsercizio1"] == nome or superset["NomeEsercizio2"] == nome:
                    modificaSuperSet(superset)
                    print("Superset modificato ")
                    break
            else:
                print("Superset non trovato")
       
        elif scelta == "10":
            rimuoviEsercizio(esercizi)
       
        elif scelta == "11":
            nome = input("Inserisci il nome dell'allenamento da eliminare: ")
            for i, allenamento in enumerate(allenamenti):  
                if allenamento["NomeAllenamento"] == nome:
                    conferma = input("Sei sicuro? si no ")
                    if conferma.lower() == 'si':
                        allenamenti.pop(i)
                        print("Allenamento rimosso")
                    break
            else:
                print("Allenamento non trovato")
       
        elif scelta == "12":
            # Funzione per rimuovere superset non implementata
            print("Funzione di rimozione superset non implementata.")
       
        elif scelta == "13":
            nome = input("Inserisci il nome dell'allenamento da iniziare: ")
            for scheda in schede:
                if scheda and scheda[0]["NomeAllenamento"] == nome:
                    start(scheda)
                    break
            else:
                print("Allenamento non trovato.")
       
        elif scelta == "14":
            vediSchede(schede)
       
        elif scelta == "15":
            print("Uscita dal programma.")
            return
       
        else:
            print("Scelta non valida")
 
menu()
 
#bubblesort = In informatica il Bubble sort o ordinamento a bolla è un semplice algoritmo di ordinamento di liste
# di dati. In esso l'insieme di dati viene scansionato, ogni coppia di elementi adiacenti viene comparata ed i due
# elementi vengono invertiti di posizione se sono nell'ordine sbagliato
 
 
# dizioanrio info = Un dizionario è una struttura dati che permette di gestire un insieme dinamico di dati,
# che di norma è un insieme totalmente ordinato, tramite queste tre sole operazioni:
# insert: si inserisce un elemento; • search: si ricerca un elemento; • delete: si elimina un elemento.
 
 
#dizionario python = al fine di creare e gestire collezioni ordinate di oggetti in modo efficiente.
# I dizionari ( dict ) sono un tipo built-in,
# mutabile e non ordinato che contiene elementi (items) formati da una chiave (key) e un valore (value).
 
 
 
# La funzione enumerate() prende un oggetto iterabile (come una lista) e restituisce un oggetto enumerato.
#  Questo oggetto enumerato produce coppie di valori,
# dove il primo valore è l'indice (a partire da 0) e il secondo valore è l'elemento corrispondente dell'iterabile.
