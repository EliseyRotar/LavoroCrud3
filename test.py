from os import system
import time
import winsound
#Programma crea la tua scheda allenamento (timer)
#Crea tipo allenamento
#Numero di esercizi 
#Numero serie
#Tipi esercizi e il loro nome
#Tempo esercizi "timer"/"No timer"
#PROBLEMI: eccezzioni, numeri scritti in parole, maiuscole
allenamento1 = {
    "NomeAllenamento":"crazu",
    "GruppoAllenante":"Schiena",
    "NumEsercizi":0,
    "TipoAllenamento":"Timer", #timer/senza timer/misto
    "TempoRiscaldamento":0, #secondi
}

esercizio1 = {
    "TipologiaEsercizio":"Timer", #timer/senza timer
    "TempoAllenamento":10,
    "Serie":2
    "TempoRiposo":2
}

esercizio2 = {
    "TipologiaEsercizio":"Timer", #timer/senza timer
    "TempoAllenamento":50,
    "Serie":1,
    "TempoRiposo":2
}
esercizi = [esercizio1,esercizio2]
allenamenti = [allenamento1]
Scheda2 = []
Scheda1= [allenamento1, esercizio1, esercizio2]

Schede = [Scheda1,Scheda2]
def creaEsercizio(esercizio):
    #controllo (try/except inserire valori accettabili)
    tipoEsercizio = int(input("Inserire 1 se si vuole avere un timer per questo esercizio, invece inserire qualsiasi altra cosa se non si vuole avere un timer: "))
    if tipoEsercizio == 1:
        tempoAllenamento = int(input("Inserisci il tempo richiesto per questo esercizio: "))
    numeroSerie = int(input("Inserire il numero di serie: "))
    tempoRiposo = int(input("Inserire il tempo di riposo tra le serie: "))
    esercizio = {
        "TipologiaEsercizio":tipoEsercizio,
        "TempoAllenamento":tempoAllenamento,
        "Serie":numeroSerie,
        "TempoRiposo":tempoRiposo
    }
    return esercizio

def creaAllenamento(allenamento):
    #controllo (try/except inserire valori accettabili)
    nomeAllenamento = input("Inserire il nuovo nome dell'allenamento: ")
    gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
    nEsercizi = int(input("Inserisci il numero di esercizi contenuti in questo allenamento: "))
    tipoAllenamento = input("Inserire 1 se è un allenamento contenente solo esercizi con timer, inserire 2 se non vuoi i timer, inserire 3 se è un allenamento sia con timer che senza.")
    tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
    allenamento = {
        "NomeAllenamento":nomeAllenamento,
        "GruppoAllenante":gruppoAllenante,
        "NumEsercizi":nEsercizi,
        "TipoAllenamento":tipoAllenamento,  
        "TempoRiscaldamento":tempoRiscaldamento, 
    }
    return allenamento

def creaSuperSet(superset):
    #controllo (try/except inserire valori accettabili)
    #DA RIFARE
    set1 = input("Inserisci il nome del primo set: ")
    set2 = input("Inserisci il nome del secondo set: ")
    superset = [set1, set2]
    creaEsercizio(set1)
    creaEsercizio(set2)
    return superset

def vediEsercizio(lista,nomeEsercizio):
    #controllo (try/except se esistenza esercizio)
    #print(f'{"Tipologia:":<15}{"Durata:":<15}{"N° serie:":<15}')
    print(f'{esercizio["TipologiaEsercizio"]:<15}{esercizio["TempoAllenamento"]:<15}{esercizio["Serie"]:<15}')

def vediScheda(nomeScheda):
    #controllo (try/except se esistenza scheda)
    print(nomeScheda["GruppoAllenante"])
    print(f'{"Tipologia:":<15}{"Durata:":<15}{"N° serie:":<15}')
    count = 0
    while count < len(scheda):
        vediEsercizio(scheda[count])
        count+=1
def vediSchede(Schede):
    #controllo (try/except se c'è almeno una scheda)
    count = 0
    while count < len(Schede:list):
        print(f"{Schede[count][""]")
        count+=1
def modificaAllenamento(nomeAllenamento):
    #controllo (try/except se esiste l'allenamento)
    #controllo (try/except inserire valori accettabili)
    momeAllenamento = {
        "NomeAllenamento":nomeAllenamento,
        "GruppoAllenante":gruppoAllenante,
        "NumEsercizi":nEsercizi,
        "TipoAllenamento":tipoAllenamento,  
        "TempoRiscaldamento":tempoRiscaldamento, 
    }
    nomeAllenamento = input("Inserire il nuovo nome dell'allenamento: ")
    gruppoAllenante = input("Inserire il nuovo gruppo o i nuovi gruppi muscolari che si vogliono allenare: ")
    nEsercizi = int(input("Inserisci il numero di esercizi contenuti in questo allenamento: "))
    tipoAllenamento = input("Inserire 1 se è un allenamento contenente solo esercizi con timer, inserire 2 se non vuoi i timer, inserire 3 se è un allenamento sia con timer che senza.")
    tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
    return nomeAllenamento
    

def modificaEsercizio(scheda:list,esercizio):
    #controllo (try/except controllo se l'esercizio esiste)
    #controllo (try/except inserire valori accettabili)
    tipoEsercizio = int(input("Inserire 1 se si vuole avere un timer per questo esercizio, invece inserire qualsiasi altra cosa se non si vuole avere un timer: "))
    if tipoEsercizio == 1:
        tempoAllenamento = int(input("Inserisci il tempo richiesto per questo esercizio: "))
    numeroSerie = int(input("Inserire il numero di serie: "))
    tempoRiposo = int(input("Inserire il tempo di riposo tra le serie: "))
    esercizio = {
        "TipologiaEsercizio":tipoEsercizio,
        "TempoAllenamento":tempoAllenamento,
        "Serie":numeroSerie,
        "TempoRiposo":tempoRiposo,
        
    }
    return esercizio

def modificaScheda(scheda):
    #controllo (try/except controllo se la scheda esiste)
    #controllo (try/except inserire valori accettabili)
    gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
    nEsercizi = int(input("Inserisci il numero di esercizi contenuti in questo allenamento: "))
    tipoAllenamento = input("Inserire 1 se è un allenamento contenente solo esercizi con timer, inserire 2 se non vuoi i timer, inserire 3 se è un allenamento sia con timer che senza.")
    tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
    allenamento = {
        "GruppoAllenante":gruppoAllenante,
        "NumEsercizi":nEsercizi,
        "TipoAllenamento":tipoAllenamento,  
        "TempoRiscaldamento":tempoRiscaldamento, 
    }
    return scheda

def modificaSuperSet(superset):
    #controllo (try/except controllo esistenza superset)
    set1 = input("Inserisci il nuovo nome del primo set: ")
    set2 = input("Inserisci il nuovo nome del secondo set: ")
    superset = [set1, set2]
    modificaEsercizio(set1)
    modificaEsercizio(set2)

    return superset

def rimuoviEsercizio(lista:list,esercizio):
    #controllo (try/except controllo se l'allenamento esiste)
    indice =0
    vediScheda()
    while indice < 1 and indice > len(lista)
        indice=int(input("Inserisci l'indice dell'esercizio da eliminare
        system('cls')
    lista.pop(indice)
    print("L'esercizio è stato rimosso con successo")

def rimuoviScheda(lista:list):
    #controllo (try/except controllo se la scheda esiste)
    scelta=input("Sei sicuro di eliminare la tua scheda di allenamento?")
    if scelta==Si:
        del lista
        print("La scheda è stata eliminata")
    return 0 

def timer(nomeEsercizio):
    
def start(Scheda:list):
    Scheda
    count=1
    while count < len(Scheda):
        timer(Scheda[count])
              count+=1
        
    
def menu():
    
#ELISEY
#per la funzione creaAllenamento lasciatela a me(Valente)
#Elisey se vuoi prendi spunto da questo menu che avevo fatto io
#Per ogni punto del menù fare attenzione se serve inserirlo in una lista
print("\4--------------------------------------------------\4")
print("|               Timer x allenamenti                |")
print("\4 Benvenuto Andrea,buona sessione di allenamento!! \4")
print("                     Inserire: \n  1)Per iniziare la sessione\n  2)Modificare il piano di allenamento\n  3)Modificare numero serie/superset\n  4)Exit")
scelta=int(input("   -> "))
os.system('cls')   





#NON ELIMINARE (prendere da riferimento)
allenamento=50
pausa=180
intervallo=15
inizio = 10
serie=5
superset=4
count=0
n=0
t=0
resto=n%2
def timer(n):
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
    os.system('cls')
t=inizio
timer(t)
for i in range(0,serie):
    for i in range(0,superset):
        print("Inizio serie!")
        t=allenamento
        timer(t)
        print("Fra poco si ricomincia!")
        t=intervallo
        timer(t)
        print("Inizio serie!")
        t=allenamento
        timer(t)
        print("Fra poco si ricomincia")
        t=pausa
        timer(t)
