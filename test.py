#Programma crea la tua scheda allenamento (timer)
#Crea tipo allenamento
#Numero di esercizi 
#Numero serie
#Tipi esercizi e il loro nome
#Tempo esercizi "timer"/"No timer"
#PROBLEMI: eccezzioni, numeri scritti in parole, maiuscole
allenamento1 = {
    "GruppoAllenante":"Schiena",
    "N°Esercizi":0,
    "TipoAllenamento":"Timer", #timer/senza timer/misto
    "TempoRiscaldamento":0, #secondi
    "TempoRipresa":0 #secondi

}

allenamenti = [allenamento1]

esercizio1 = {
    "TipologiaEsercizio":"Timer", #timer/senza timer
    "TempoAllenamento":10,
    "Serie":0
}

esercizi = [esercizio1]

def creaEsercizio(esercizio):
    esercizio = {
        "TipologiaEsercizio":tipoEsercizio,
        "TempoAllenamento":tempoAllenamento,
        "Serie": numeroSerie
    }
    tipoEsercizio = input("Inserire la parola timer se si vuole avere un timer per questo esercizio inserire la parola  ")
    tempoAllenamento = int(input("Inserisci il tempo richiesto per questo esercizio: "))
    numeroSerie = int(input("Inserire il numero di serie: "))

def creaAllenamento(allenamento):
    allenamento = {
        "GruppoAllenante":gruppoAllenante,
        "N°Esercizi":nEsercizi,
        "TipoAllenamento":"Timer",  
        "TempoRiscaldamento":0, 
        "TempoRipresa":0 
    }
    gruppoAllenante = input("Inserire il gruppo o i gruppi muscolari che si vogliono allenare: ")
    nEsercizi = int(input("Inserisci il numero di esercizi contenuti in questo allenamento: "))
    tipoAllenamento = (input("Inserire il numero di serie: "))