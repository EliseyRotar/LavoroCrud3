# Training Scheduler 🏋️♂️

Un programma Python per creare e gestire schede di allenamento personalizzate con timer integrato. Ideale per organizzare esercizi, superset e allenamenti completi con facilità.

# Caratteristiche Principali ✨

- **Crea e Gestisci Esercizi**: Definisci esercizi con o senza timer, serie e tempi di recupero.
- **Costruisci Allenamenti**: Combina esercizi in allenamenti, specifica gruppi muscolari e tempo di riscaldamento.
- **Superset**: Crea superset con due esercizi consecutivi e gestisci parametri individuali.
- **Timer Intelligente**: Avvia sessioni con countdown, avvisi sonori e promemoria motivazionali.
- **Gestione Schede**: Salva, modifica o elimina schede di allenamento complete.

# Installazione ⚙️

1. **Python**: Assicurati di avere Python 3 installato.
2. **Esegui il programma**:
   python training_scheduler.py

# Utilizzo 🚀
Menu Principale: Segui le opzioni numerate per:

Creare nuovi esercizi/allenamenti/superset (Opzioni 1-3).

Visualizzare o modificare elementi esistenti (Opzioni 4-9).

Rimuovere elementi o intere schede (Opzioni 10-12).

Avviare un allenamento con timer (Opzione 13).

Esempio - Crea Esercizio:

Copy
Nome: Push-up
Timer: 1 (30 secondi)
Serie: 3
Recupero: 60 secondi
Avvia Allenamento:

Inserisci il nome dell'allenamento.

Il timer parte con riscaldamento, seguito da esercizi con avvisi sonori.

# Struttura del Codice 📂
Dati: Memorizzati in dizionari (esercizi, allenamenti, superset) e liste (Schede).

Funzioni Principali:

creaEsercizio(), creaAllenamento(), creaSuperSet() per l'input.

timer() e timerSuperset() per la gestione del tempo.

Funzioni di modifica/rimozione con validazione degli input.

# Dipendenze 📦
Librerie standard: os, time, winsound (Windows).

# Problemi Noti 🐞
I numeri devono essere inseriti come cifre (non in parole).

Alcune funzioni superset potrebbero essere in sviluppo.

Gestione errori migliorabile per input complessi.

# Crediti 👏
Poli/Verde: Gestione errori e superset.

Elisey: Sistema di menu.

Valente: Core del programma e timer.
