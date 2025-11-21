# Esercizio 10: Gestione dei Todos per un Utente su JSONPlaceholder

Usa la libreria `requests` per interagire con l'API JSONPlaceholder. Implementa uno script Python che esegua le seguenti operazioni:

1. Recupera tutti i todos pubblicati dall'utente con ID = 1.
2. Trova il primo todo incompleto (ovvero con `completed: false`).
3. Se trovato, marca quel todo come completato utilizzando una richiesta PUT. Altrimenti, segnala che non ci sono todos incompleti.

Utilizza l'endpoint `https://jsonplaceholder.typicode.com/todos?userId=1` per recuperare i todos e `https://jsonplaceholder.typicode.com/todos/{todo_id}` per aggiornare un todo specifico.

Assicurati di gestire gli errori HTTP e di stampare i risultati in modo leggibile.

### Esempio di Output

```
--- Todos dell'utente 1 ---
Todos totali: 20
Completati: 11
Incompleti: 9

--- Primo todo incompleto trovato ---
ID: 2, Titolo: quis ut nam facilis et officia qui, Completato: False

--- Todo aggiornato ---
ID: 2, Titolo: quis ut nam facilis et officia qui, Completato: True
```

Oppure, se non ci sono incompleti:

```
--- Todos dell'utente 1 ---
Todos totali: 20
Completati: 20
Incompleti: 0

Nessun todo incompleto trovato.
```