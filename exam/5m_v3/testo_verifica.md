# VERIFICA DI PROGRAMMAZIONE: INTERAZIONE CON API REST

## Scenario
Sei stato assunto per creare uno script di automazione per una software house. L'azienda utilizza un'API interna per gestire i propri progetti. Il server è disponibile localmente all'indirizzo `http://localhost:3000`.

## Il Modello Dati (Documentazione API)

- **Endpoint `/developers`**: Restituisce la lista degli sviluppatori.
  - Campi: `id`, `username`, `role`.

- **Endpoint `/projects`**: Restituisce la lista dei progetti.
  - Campi: `id`, `dev_id` (collegamento allo sviluppatore), `name`, `status`, `budget`.
  - Supporta filtri: `?dev_id=X`, `?status=active`, ecc.

- **Endpoint `/tasks`**: Restituisce la lista dei task (attività).
  - Campi: `id`, `project_id` (collegamento al progetto), `description`, `is_done`, `hours_estimated`.
  - Supporta filtri: `?project_id=X`.

## Obiettivi
Scrivi un unico script Python (`verifica.py`) che utilizzi la libreria `requests` per svolgere le seguenti operazioni in sequenza. Gestisci correttamente eventuali errori di connessione.

### 1. Analisi Sviluppatore
- Recupera tutti i progetti assegnati allo sviluppatore con **ID = 1**.
- Stampa a video il nome di questi progetti e il loro budget.

### 2. Calcolo Carico di Lavoro
- Tra i progetti recuperati al punto 1, identifica solo quelli che hanno lo status **"active"**.
- Per ogni progetto attivo, recupera la lista dei suoi **task**.
- Calcola e stampa la somma delle `hours_estimated` dei task *non ancora completati* per quel progetto.

### 3. Assegnazione Nuovo Task
- Scegli (tramite codice) il primo progetto attivo trovato.
- Utilizzando una richiesta **POST**, crea un nuovo task per questo progetto con i seguenti dati:
  - Descrizione: "Code Review Finale"
  - Stato: Non completato (`false`)
  - Ore stimate: 3
- Stampa la risposta del server per confermare la creazione.

### 4. Pulizia
- Trova il primo task completato (`is_done: true`).
- Simula la sua eliminazione tramite una richiesta **DELETE**.
- Stampa l'ID del task eliminato.

## Preparazione dell'Ambiente

### Step 1: Assicurati di avere `requests` installato
Apri un terminale e installa la libreria richiesta:
```bash
pip install requests
```

### Step 2: Avvia il Server (TERMINALE 1)
Il server deve rimanere **sempre acceso** durante la verifica.

Apri un primo terminale e esegui:
```bash
python server_verifica.py
```

Vedrai questo messaggio:
```
--- SERVER VERIFICA ATTIVO SU PORTA 3000 ---
Risorse disponibili: developers, projects, tasks
Premi Ctrl+C per interrompere
```

**⚠️ IMPORTANTE:** Non chiudere questo terminale! Lascialo aperto per tutta la verifica.

### Step 3: Esegui il tuo Script (TERMINALE 2)
Apri un **secondo terminale** nella stessa cartella e esegui il tuo script:
```bash
python verifica.py
```

### Step 4: Quando hai finito
Torna al primo terminale e premi **Ctrl+C** per fermare il server.

---

## Note Tecniche
- **URL Base**: `http://localhost:3000`
- **Dipendenze**: Libreria `requests` per Python
- Il server gira in locale (non hai bisogno di Internet).
- Usa `try/except` per gestire `requests.exceptions.RequestException`.

## Valutazione
- Lettura corretta dello schema dati (relazioni tra tabelle)
- Uso corretto dei filtri GET
- Logica di aggregazione e filtraggio dati
- Gestione corretta degli errori di rete
- Creazione e eliminazione di risorse via POST/DELETE
