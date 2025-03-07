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
    "GruppoAllenante":"Schiena",
    "NumEsercizi":0,
    "TipoAllenamento":"Timer", #timer/senza timer/misto
    "TempoRiscaldamento":0, #secondi
    "TempoRipresa":0, #secondi
    "ex": [1, 2]
}

esercizio1 = {
    "TipologiaEsercizio":"Timer", #timer/senza timer
    "TempoAllenamento":10,
    "Serie":2
}

esercizio2 = {
    "TipologiaEsercizio":"Timer", #timer/senza timer
    "TempoAllenamento":50,
    "Serie":1
}
esercizi = [esercizio1,esercizio2]
allenamenti = [allenamento1]
Scheda2 = []
Scheda1= [allenamento1, esercizio1, esercizio2]

def creaEsercizio(esercizio):
    
    esercizio = {
        "TipologiaEsercizio":tipoEsercizio,
        "TempoAllenamento":tempoAllenamento,
        "Serie": numeroSerie
    }
    tipoEsercizio = int(input("Inserire 1 se si vuole avere un timer per questo esercizio, invece inserire qualsiasi altra cosa se non si vuole avere un timer: "))
    if tipoEsercizio == 1:
        tempoAllenamento = int(input("Inserisci il tempo richiesto per questo esercizio: "))
    numeroSerie = int(input("Inserire il numero di serie: "))
    return esercizio

def creaAllenamento(allenamento):
    gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
    nEsercizi = int(input("Inserisci il numero di esercizi contenuti in questo allenamento: "))
    tipoAllenamento = input("Inserire 1 se è un allenamento contenente solo esercizi con timer, inserire 2 se non vuoi i timer, inserire 3 se è un allenamento sia con timer che senza.")
    tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
    tempoRiposo = int(input("Inserisci il tempo di riposo tra ogni serie"))
    allenamento = {
        "GruppoAllenante":gruppoAllenante,
        "NumEsercizi":nEsercizi,
        "TipoAllenamento":tipoAllenamento,  
        "TempoRiscaldamento":tempoRiscaldamento, 
        "TempoRiposo":tempoRiposo
    }
    return allenamento

def creaSuperSet(superset):
    set1 = input("Inserisci il nome del primo set: ")
    set2 = input("Inserisci il nome del secondo set: ")
    superset = [set1, set2]
    creaEsercizio(set1)
    creaEsercizio(set2)
    return superset

def vediEsercizio(nomeEsercizio):
    #print(f'{"Tipologia:":<15}{"Durata:":<15}{"N° serie:":<15}')
    print(f'{esercizio["TipologiaEsercizio"]:<15}{esercizio["TempoAllenamento"]:<15}{esercizio["Serie"]:<15}')

def vediScheda(nomeScheda):
    print(scheda["GruppoAllenante"]) #nome !!!
    print(f'{"Tipologia:":<15}{"Durata:":<15}{"N° serie:":<15}')
    count = 0
    while count < len(scheda):
        vediEsercizio(scheda[count])
        count+=1
def vediSchede():
    count = 0
    while count < len(allenamento1):
        print(allenamento1[count], end='|')
        count+=1
def modificaAllenamento(nomeAllenamento):
    momeAllenamento = {
        "GruppoAllenante":gruppoAllenante,
        "NumEsercizi":nEsercizi,
        "TipoAllenamento":tipoAllenamento,  
        "TempoRiscaldamento":tempoRiscaldamento, 
        "TempoRiposo":tempoRiposo
    }
    gruppoAllenante = input("Inserire il nuovo gruppo o i nuovi gruppi muscolari che si vogliono allenare: ")
    nEsercizi = int(input("Inserisci il numero di esercizi contenuti in questo allenamento: "))
    tipoAllenamento = input("Inserire 1 se è un allenamento contenente solo esercizi con timer, inserire 2 se non vuoi i timer, inserire 3 se è un allenamento sia con timer che senza.")
    tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
    tempoRiposo = int(input("Inserisci il tempo di riposo tra ogni serie"))

    

def modificaEsercizio(esercizio):
    tipoEsercizio = int(input("Inserire 1 se si vuole avere un timer per questo esercizio, invece inserire qualsiasi altra cosa se non si vuole avere un timer: "))
    if tipoEsercizio == 1:
        tempoAllenamento = int(input("Inserisci il tempo richiesto per questo esercizio: "))
    numeroSerie = int(input("Inserire il numero di serie: "))
    #fare controllo esistenza variabili
    return esercizio

def modificaScheda(scheda):
 
    gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
    nEsercizi = int(input("Inserisci il numero di esercizi contenuti in questo allenamento: "))
    tipoAllenamento = input("Inserire 1 se è un allenamento contenente solo esercizi con timer, inserire 2 se non vuoi i timer, inserire 3 se è un allenamento sia con timer che senza.")
    tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
    tempoRiposo = int(input("Inserisci il tempo di riposo tra ogni serie"))
    allenamento = {
        "GruppoAllenante":gruppoAllenante,
        "NumEsercizi":nEsercizi,
        "TipoAllenamento":tipoAllenamento,  
        "TempoRiscaldamento":tempoRiscaldamento, 
        "TempoRiposo":tempoRiposo
    }
    #fare controllo esistenza variabili
    return scheda

def modificaSuperSet(superset):
    set1 = input("Inserisci il nuovo nome del primo set: ")
    set2 = input("Inserisci il nuovo nome del secondo set: ")
    superset = [set1, set2]
    modificaEsercizio(set1)
    modificaEsercizio(set2)
    #fare controllo esistenza variabili
    return superset

def rimuoviEsercizio(lista:list,Allenamento,esercizio):
    indice =0
    vediScheda()
    while indice < 1 and indice > len(lista)
        indice=int(input("Inserisci l'indice dell'esercizio da eliminare
        system('cls')
    lista.pop(indice)
    print("L'esercizio è stato rimosso con successo")

def rimuoviScheda(lista:list):
    scelta=input("Sei sicuro di eliminare la tua scheda di allenamento?")
    if scelta==Si
        del lista
        print("La scheda è stata eliminata")
    return 0 #Forse non serve una funzione

def timer(esercizio,esercizio[:
    
def menu():
#ELISEY
#per la funzione creaAllenamento lasciatela a me(Valente)






#NON MODIFICARE (prendere da riferimento)
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

print("\4--------------------------------------------------\4")
print("|               Timer x allenamenti                |")
print("\4 Benvenuto Andrea,buona sessione di allenamento!! \4")
print("                     Inserire: \n  1)Per iniziare la sessione\n  2)Modificare il piano di allenamento\n  3)Modificare numero serie/superset\n  4)Exit")
scelta=int(input("   -> "))
os.system('cls')   

if scelta==2:
    allenamento=int(input("Inserire quanto voler far durate uno dei due super set: "))
    pausa=int(input("Inserire quanto voler far durare la pausa: "))
    intervallo=int(input("Inserisci quanto far durare l'intervallo tra i set"))
    inizio=int(input("Inserisci fra quanti secondi far iniziare il programma"))
    numeroserie=int(input("Inserisci il numero di serie: "))
    numerosuperset=int(input("Inserire il numero di superset: "))
elif scelta==3:
    numeroserie=int(input("Inserisci il numero di serie: "))
    numerosuperset=int(input("Inserire il numero di superset: "))
elif scelta==4:
    exit()
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
