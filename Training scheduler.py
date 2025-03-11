from os import system
import time
import winsound 
#Programma crea la tua scheda allenamento (timer)
#PROBLEMI: (numeri scritti in parole, maiuscole) far funzionare tutto, timer SuperSet, cambiare nome variabili, problemi con le liste
#PARTI:
#POLI: Funzioni di Superset
#VERDE: Gestione eccezzioni e controlli
#ELISEY: Il menu, ReadME, aggiunte varie
#VALENTE: Il resto + correzione errori degli altri e aggiunte varie
allenamento1 = {
    "NomeAllenamento":"crazy",
    "GruppoAllenante":"Schiena",
    "TempoRiscaldamento":0, #secondi
}

esercizio1 = {
    "NomeEsercizio":"Push-up",
    "TempoAllenamento":10,
    "Serie":2,
    "TempoRiposo":2
}

superset1 = {
    "NomeEsercizio":"Push-up",
    "NomeEsercizio2":"curl",
    "TempoAllenamento1":10,
    "TempoAllenamento2":23,
    "Serie":2,
    "TempoRiposo1":2,
    "TempoRiposo2": 6
}

esercizio2 = {
    "NomeEsercizio":"Tiger push-up",
    "TempoAllenamento":50,
    "Serie":1,
    "TempoRiposo":2
}
esercizi = [esercizio1,esercizio2]
allenamenti = [allenamento1]
scheda1= [allenamento1, esercizio1, esercizio2, superset1]

schede = [scheda1]
def creaEsercizio(esercizio):
    try:
        nomeEsercizio = input("Inserire il nome dell'esercizio: ")
        tempoAllenamento = int(input("Inserisci il tempo richiesto per questo esercizio: "))
        numeroSerie = int(input("Inserire il numero di serie: "))
        tempoRiposo = int(input("Inserire il tempo di riposo tra le serie: "))
        esercizio = {
            "NomeEsercizio":nomeEsercizio,
            "TempoAllenamento":tempoAllenamento,
            "Serie":numeroSerie,
            "TempoRiposo":tempoRiposo
        }
    except ValueError:
        print("errore")
    return esercizio

def creaAllenamento(allenamento):
    try:
        nomeAllenamento = input("Inserire il nuovo nome dell'allenamento: ")
        gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
        
        try:
            tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
            if tempoRiscaldamento < 0:
                raise ValueError("Il tempo di riscaldamento non può essere negativo.")
            
        except ValueError as e:
            print(f"Errore di input: {e}")
            return None
        
        allenamento = {
            "NomeAllenamento": nomeAllenamento,
            "GruppoAllenante": gruppoAllenante,
            "TempoRiscaldamento": tempoRiscaldamento
        }
        
        return allenamento
    
    except Exception as e:
        print(f"Errore: {e}")
        return None
    
def creaSuperSet(superset):
    if superset is None:
        raise ValueError("Il superset non esiste.")

    NomeEsercizio1 = input("Inserire il nome del primo esercizio: ")
    NomeEsercizio2 = input("Inserisci il nome del secondo esercizio: ")
    TempoAllenamento1 = int(input("Inserisci il tempo del primo esercizio: "))
    TempoAllenamento2 = int(input("Inserisci il tempo del secondo esercizio: "))
    Serie = int(input("Inserisci il numero di serie: "))
    TempoRiposo1 = int(input("Inserisci il tempo di recupero del primo esercizio: "))
    TempoRiposo2 = int(input("Inserisci il tempo di recupero del secondo esercizio: "))

    if TempoAllenamento1 <= 0 and TempoAllenamento2 <= 0 and Serie <= 0 and TempoRiposo1 < 0 and TempoRiposo2 < 0:
            raise ValueError("Il tempo degli esercizi deve essere maggiore di zero.")
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
        

def vediEsercizio(esercizio):
    print(f'{esercizio["nomeEsercizio"]:<15}|{esercizio["TempoAllenamento"]:<15}|{esercizio["TempoRiposo"]:<15}|{esercizio["Serie"]:<15}')

def vediScheda(nomeScheda: dict):
    try:
        # Controllo se la scheda esiste
        if nomeScheda is None or not nomeScheda:
            raise ValueError("La scheda non esiste o è vuota.")
        
        print(nomeScheda["GruppoAllenante"])
        print(f'{"Tipologia:":<15}{"Durata:":<15}{"N° serie:":<15}')
        
        count = 0
        while count < len(nomeScheda):
            vediEsercizio(nomeScheda[count])
            count += 1
    
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
        
        count = 0
        print("Ecco l'elenco delle schede esistenti:")
        while count < len(Schede):
            try:
                print(f'{Schede[count][0]["NomeAllenamento"]}: {Schede[count][0]["GruppoAllenante"]}')
            except KeyError as e:
                print(f"Errore: La chiave {e} non esiste nella scheda.")
            count += 1
    
    except ValueError as e:
        print(f"Errore: {e}")
        
def modificaEsercizio(scheda: list, esercizio: dict):
    try:
        # Controllo se l'esercizio esiste
        if esercizio is not esercizio:
            raise ValueError("L'esercizio non esiste o è vuoto.")
        
        # Inserimento dei dati con controllo try/except
        try:
            nomeEsercizio = input("Inserisci il nome dell'esercizio: ")
            tempoAllenamento = int(input("Inserisci il tempo richiesto per questo esercizio: "))
            numeroSerie = int(input("Inserire il numero di serie: "))
            if numeroSerie <= 0:
                raise ValueError("Il numero di serie deve essere maggiore di zero.")
            
            tempoRiposo = int(input("Inserire il tempo di riposo tra le serie: "))
            if tempoRiposo < 0:
                raise ValueError("Il tempo di riposo non può essere negativo.")
            
            esercizio = {
                "NomeEsercizio": nomeEsercizio,
                "TempoAllenamento": tempoAllenamento,
                "Serie": numeroSerie,
                "TempoRiposo": tempoRiposo
            }
            
            return esercizio
        
        except ValueError as e:
            print(f"Errore di input: {e}")
            return None
    
    except ValueError as e:
        print(f"Errore: {e}")
        return None


def modificaScheda(scheda):
    try:
        if scheda is None:
            raise ValueError("La scheda non esiste.")
        try:
            gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
            
            nEsercizi = int(input("Inserisci il numero di esercizi contenuti in questo allenamento: "))
            if nEsercizi <= 0:
                raise ValueError("Il numero di esercizi deve essere maggiore di zero.")
            
            tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
            if tempoRiscaldamento < 0:
                raise ValueError("Il tempo di riscaldamento non può essere negativo.")
            
            allenamento = {
                "GruppoAllenante": gruppoAllenante,
                "NumEsercizi": nEsercizi,
                "TempoRiscaldamento": tempoRiscaldamento
            }
            
            scheda.update(allenamento)
            print("Scheda aggiornata con successo.")
        
        except ValueError as e:
            print(f"Errore di input: {e}")
    
    except ValueError as e:
        print(f"Errore: {e}")
        return scheda

def modificaSuperSet(superset):
    try:
        # Controllo se il superset esiste
        if superset is None:
            raise ValueError("Il superset non esiste.")
        #  controllo con il try/except
        try:
            NomeEsercizio1 = input("Inserire il nome del primo esercizio: ")
            NomeEsercizio2 = input("Inserisci il nome del secondo esercizio: ")
            if TempoAllenamento1 <= 0 and TempoAllenamento2 <= 0 and Serie <= 0 and TempoRiposo1 < 0 and TempoRiposo2 < 0:
                TempoAllenamento1 = int(input("Inserisci il tempo del primo esercizio: "))
                TempoAllenamento2 = int(input("Inserisci il tempo del secondo esercizio: "))
                Serie = int(input("Inserisci il numero di serie: "))
                TempoRiposo1 = int(input("Inserisci il tempo di recupero del primo esercizio: "))
                TempoRiposo2 = int(input("Inserisci il tempo di recupero del secondo esercizio: "))
            
                raise ValueError("Il tempo del primo esercizio deve essere maggiore di zero.")
            
            TempoRiposo1 = int(input("Inserisci il tempo di recupero del primo esercizio: "))
            if TempoRiposo1 < 0:
                raise ValueError("Il tempo di recupero del primo esercizio non può essere negativo.")
            
            TempoRiposo2 = int(input("Inserisci il tempo di recupero del secondo esercizio: "))
            if TempoRiposo2 < 0:
                raise ValueError("Il tempo di recupero del secondo esercizio non può essere negativo.")
            
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
    
    except ValueError as e:
        print(f"Errore: {e}")
        return None

def rimuoviEsercizio(lista: list, esercizio: dict):
    try:
        # Controllo S L ALLENAMENT O ESISTE 
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

def rimuoviScheda(lista: list): #CONTROLLO VECCHIA VERSIONE
    try:
        # Controllo se la scheda esiste
        if not lista:
            raise ValueError("La lista delle schede è vuota.")
        
        scelta = input("Sei sicuro di eliminare la tua scheda di allenamento? (Si/No): ")
        if scelta.lower() == "si":
            del lista[:]
            print("La scheda è stata eliminata.")
        else:
            print("Eliminazione della scheda annullata.")
        
        return 0
    
    except ValueError as e:
        print(f"Errore: {e}")


#def timerSuperset(superSet: dict): non funzionante

    

def timer(n):
    t = n
    while n:
        if n==t:
            print(n)
            n-=1          
            winsound.Beep(1000,1000)
        elif n==5:
            print("Mancano 5 secondi SPINGI UOMO")
            n-=1          
            winsound.Beep(600,1000)
        elif n==3 or n==1:
            print(n)
            n-=1
            winsound.Beep(600,1000)
        else:
            print(n)
            time.sleep(1) 
            n -= 1
        system('cls')   

def timerEsercizio(esercizio:dict):
    count=1
    while count < esercizio["NumeroSerie"]:
        if count == esercizio["NumeroSerie"]:
            print("Inizio serie")
            timer(esercizio["TempoAllenamento"])
        else:
            print("Inizio serie")
            timer(esercizio["TempoAllenamento"])
            print("Inizio riposo")
            timer(esercizio["TempoRiposo"])
        count +=1
 

def start(Scheda:list):
     #Scheda[count] == dict #volevo specificare che Scheda è una lista contenente dizionari okokkkk tranqui
     print("Inizio riscaldamento!")
     timer(Scheda[0]["tempoRiscaldamento"])
     count = 1
     while count < len(Scheda):
        timerEsercizio(Scheda[count])
        count+=1
         
         #VALENTE continiuoamo ora?? io continuo un po'
 


def menu():
    #menu fatto molto bene con degli astetics
    
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
    print("12. Rimuovi superset") #Funziona con rimuovi esercizio 
    print("13. Avvia timer allenamento") 
    print("14. Gestisci schede") #??? BROOO
    print("15. Esci")
    print("\n" + "-" * 50)
    scelta = input("Inserisci il numero corrispondente all'azione che vuoi eseguire: ")
    
    if scelta == "1":
            esercizio = creaEsercizio({})
            if esercizio:
                esercizi.append(esercizio)
                print("Esercizio creato con successo")
                menu()
    elif scelta == "2":
            allenamento = creaAllenamento({})
            if allenamento:
                allenamenti.append(allenamento)
                print("Allenamento creato con successo")
    elif scelta == "3":
            superset = creaSuperSet({})
            if superset:
                superset.append(superset)
                print("Superset creato con successo")
    elif scelta == "4":
            for esercizio in esercizi:
                print(f'{"Tipologia:":<15}{"Durata:":<15}{"N° serie:":<15}')
    elif scelta == "5":
            for allenamento in allenamenti:
                vediScheda(allenamento)
    elif scelta == "6":
            for superset in superset:
                print(superset)
    elif scelta == "7":
            nome = input("Inserisci il nome dell'esercizio da modificare: ")
            for i, esercizio in (esercizi):
                if esercizio["NomeEsercizio"] == nome:
                    nuovo_esercizio = modificaEsercizio(esercizi, esercizio)
                    if nuovo_esercizio:
                        esercizi[i] = nuovo_esercizio
                        print("Esercizio modificato con successo")
                    break
            else:
                print("Esercizio non trovato")
    elif scelta == "8":
            nome = input("Inserisci il nome dell'allenamento da modificare: ")
            for i, allenamento in (allenamenti):
                if allenamento["NomeAllenamento"] == nome:
                    modificaScheda(allenamento)
                    print("Allenamento modificato ")
                    break
            else:
                print("Allenamento non trovato")
    elif scelta == "9":
            nome = input("Inserisci il nome del superset da modificare: ")
            for i, superset in (superset):
                if superset["NomeEsercizio1"] == nome or superset["NomeEsercizio2"] == nome:
                    nuovo_superset = modificaSuperSet(superset)
                    if nuovo_superset:
                        superset[i] = nuovo_superset
                        print("Superset modificato ")
                    break
            else:
                print("Superset non c'è")
    elif scelta == "10":
            rimuoviEsercizio(esercizi)
    elif scelta == "11":
            nome = input("Inserisci il nome dell'allenamento da eliminare: ")
            for i, allenamento in (allenamenti):
                if allenamento["NomeAllenamento"] == nome:
                    conferma = input("Sei sicuro? si no ")
                    if conferma.lower() == 'si':
                        allenamenti.pop(i)
                        print("Allenamento tolto")
                    break
            else:
                print("Allenamento non c'è")
    #elif scelta == "12":
    #        rimuoviSuperSet(superset)
    elif scelta == "13":
            nome = input("Inserisci il nome dell'allenamento da iniziare ")
            for scheda in Schede:
                if scheda and scheda[0]["NomeAllenamento"] == nome:
                    start(scheda)
                    break
            else:
                print("Allenamento non trovato.")
    elif scelta == "14":
            vediSchede(Schede)
    elif scelta == "15":
            print("exit test")
            return
    else:
            print("Scelta non valida")
        
#print(f'{"Tipologia:":<15}{"Durata:":<15}{"N° serie:":<15}') funzione vediEsercizio <--DEVI ANCORA IMPLEMENTARE QUESTA 
#Nel menù manca la parte del:
#creare la lista che contiene le dict (allenamento più esercizi)
#va implementata nella parte del menù crea allenamento
#Che cos'è .update?
menu() 


