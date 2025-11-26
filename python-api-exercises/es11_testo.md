# Esercizio 11: Gestione Completa di Post e Commenti per un Utente

Usa la libreria `requests` per interagire con l'API JSONPlaceholder. Implementa uno script Python che esegua le seguenti operazioni:

1. Recupera tutti i post pubblicati dall'utente con ID = 1.
2. Per ciascun post, recupera il numero di commenti e identifica il post con il maggior numero di commenti.
3. Se il post con più commenti ha meno di 5 commenti, crea un nuovo commento per quel post utilizzando una richiesta POST. Altrimenti, elimina il commento più vecchio (se esiste) utilizzando una richiesta DELETE.
4. Gestisci gli errori HTTP e stampa i risultati in modo leggibile, inclusi i dettagli del post selezionato e l'azione intrapresa.

Utilizza gli endpoint: `https://jsonplaceholder.typicode.com/posts?userId=1` per i post, `https://jsonplaceholder.typicode.com/posts/{post_id}/comments` per i commenti, `https://jsonplaceholder.typicode.com/comments` per creare un commento, e `https://jsonplaceholder.typicode.com/comments/{comment_id}` per eliminare un commento.

### Esempio di Output

```
--- Post dell'utente 1 ---
Post ID: 1, Titolo: sunt aut facere repellat..., Commenti: 5
Post ID: 2, Titolo: qui est esse, Commenti: 3
...

--- Post con più commenti ---
ID: 1, Titolo: sunt aut facere repellat..., Commenti: 5

--- Azione intrapresa ---
Poiché il post ha 5 o più commenti, eliminato il commento ID: 1 (il più vecchio).
```