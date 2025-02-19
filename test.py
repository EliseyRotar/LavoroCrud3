import os
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
    "TempoRipresa":0 #secondi
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

def creaAllenamento(allenamento):
    allenamento = {
        "GruppoAllenante":gruppoAllenante,
        "NumEsercizi":nEsercizi,
        "TipoAllenamento":tipoAllenamento,  
        "TempoRiscaldamento":tempoRiscaldamento, 
        "TempoRiposo":tempoRiposo
    }
    gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
    nEsercizi = int(input("Inserisci il numero di esercizi contenuti in questo allenamento: "))
    tipoAllenamento = input("Inserire 1 se è un allenamento contenente solo esercizi con timer, inserire 2 se non vuoi i timer, inserire 3 se è un allenamento sia con timer che senza.")
    tempoRiscaldamento = int(input("Inserire quanto tempo bisogna riservare per il riscaldamento: "))
    tempoRiposo = int(input("Inserisci il tempo di riposo tra ogni serie"))

def creaSuperSet(superset):
    set1 = input("Inserisci il nome del primo set: ")
    set2 = input("Inserisci il nome del secondo set: ")
    superset = [set1, set2]
    creaEsercizio(set1)
    creaEsercizio(set2)

def vediEsercizio(esercizio):
    #print(f'{"Tipologia:":<15}{"Durata:":<15}{"N° serie:":<15}')
    print(f'{esercizio["TipologiaEsercizio"]:<15}{esercizio["TempoAllenamento"]:<15}{esercizio["Serie"]:<15}')

def vediScheda(scheda):
    print(scheda["GruppoAllenante"]) #nome !!!
    print(f'{"Tipologia:":<15}{"Durata:":<15}{"N° serie:":<15}')
    count = 0
    while count < len(scheda):
        vediEsercizio(scheda[count])
        count+=1