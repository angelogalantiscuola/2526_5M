# ESERCIZIO: SISTEMA DI GESTIONE BIBLIOTECA

## Scenario
Sei uno sviluppatore che lavora per una biblioteca comunale. Il sistema utilizza un'API interna per gestire il catalogo. Il server è disponibile localmente all'indirizzo `http://localhost:3001`.

## Il Modello Dati (Documentazione API)

- **Endpoint `/authors`**: Restituisce la lista degli autori.
  - Campi: `id`, `name`, `country`.

- **Endpoint `/genres`**: Restituisce la lista dei generi letterari.
  - Campi: `id`, `name`.

- **Endpoint `/books`**: Restituisce la lista dei libri.
  - Campi: `id`, `author_id` (collegamento all'autore), `genre_id` (collegamento al genere), `title`, `pages`, `available` (bool).
  - Supporta filtri: `?author_id=X`, `?genre_id=X`, ecc.

## Obiettivi
Scrivi uno script Python (`esercizio.py`) che utilizzi la libreria `requests` per svolgere le seguenti operazioni in sequenza.

### 1. Cerca Libri di un Autore
- Recupera tutti i libri dell'autore con **ID = 1**.
- Stampa il titolo e il numero di pagine di ogni libro.

**Output atteso:**
```
Libri di Daniele Pennac:
  - La Storia Infinita (400 pagine)
  - Il Giuramento dei Tre (350 pagine)
```

### 2. Filtra per Disponibilità
- Tra i libri trovati al punto 1, mostra solo quelli con `available: true`.
- Stampa il titolo di questi libri.

**Output atteso:**
```
Libri disponibili:
  - La Storia Infinita
```

### 3. Conta Pagine Totali
- Calcola la somma delle pagine dei libri disponibili (trovati al punto 2).
- Stampa il totale.

**Output atteso:**
```
Pagine totali disponibili: 400
```

### 4. Libri per Genere
- Recupera tutti i libri del genere **Fantasy** (ID = 101).
- Stampa il nome del genere e quanti libri appartengono a quel genere.

**Output atteso:**
```
Genere: Fantasy
Numero di libri: 2
```

## Preparazione dell'Ambiente

### Step 1: Assicurati di avere `requests` installato
Apri un terminale e installa la libreria richiesta:
```bash
pip install requests
```

### Step 2: Avvia il Server (TERMINALE 1)
Il server deve rimanere **sempre acceso** durante l'esercizio.

Apri un primo terminale e esegui:
```bash
python server_biblioteca.py
```

Vedrai questo messaggio:
```
--- SERVER BIBLIOTECA ATTIVO SU PORTA 3001 ---
Risorse disponibili: authors, genres, books
Premi Ctrl+C per interrompere
```

**⚠️ IMPORTANTE:** Non chiudere questo terminale! Lascialo aperto per tutto l'esercizio.

### Step 3: Esegui il tuo Script (TERMINALE 2)
Apri un **secondo terminale** nella stessa cartella e esegui il tuo script:
```bash
python esercizio.py
```

### Step 4: Quando hai finito
Torna al primo terminale e premi **Ctrl+C** per fermare il server.

---

## Note Tecniche
- **URL Base**: `http://localhost:3001`
- Usa `try/except` per gestire `requests.exceptions.RequestException`.
- Il server gira in locale.

## Suggerimenti per la Soluzione
1. Usa `requests.get()` per recuperare i dati
2. Filtra con list comprehension: `[libro for libro in libri if libro['available']]`
3. Usa `sum()` per calcolare le pagine totali
4. Cerca il genere con `next()` oppure con un ciclo `for`

## Cosa fare se il server non si avvia
Se vedi l'errore `OSError: [Errno 98] Address already in use`, significa che la porta 3001 è già occupata da un altro processo.

### Su Linux/Mac:
1. Trova il processo che sta usando la porta:
```bash
lsof -ti:3001
```

2. Se il comando non restituisce alcun PID, la porta potrebbe essere ancora in stato TIME_WAIT (dopo la chiusura di un processo precedente). In questo caso:
   - Aspetta qualche minuto e riprova ad avviare il server.
   - Oppure, riavvia il sistema se necessario.

3. Se viene restituito un PID, uccidi il processo (sostituisci `PID` con il numero ottenuto):
```bash
kill -9 PID
```

4. Riprova ad avviare il server.

### Su Windows:
1. Apri PowerShell come amministratore e trova il processo che sta usando la porta:
```powershell
netstat -ano | findstr :3001
```
   Questo mostrerà il PID nella colonna più a destra.

2. Uccidi il processo (sostituisci `PID` con il numero trovato):
```powershell
taskkill /PID PID /F
```

3. Riprova ad avviare il server.

In alternativa, puoi attendere che il processo termini naturalmente o riavviare il sistema se necessario.
