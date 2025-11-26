# Esercizio 9: Interazione Avanzata con JSONPlaceholder

Usa la libreria `requests` per consumare l'API JSONPlaceholder. Implementa uno script Python che esegua le seguenti operazioni:

1. Recupera tutti i post pubblicati dall'utente con ID = 1 e stampali.
2. Recupera i commenti per il primo post e stampali.
3. Crea un nuovo commento per il primo post dell'utente, utilizzando una richiesta POST.

Utilizza la documentazione di JSONPlaceholder per gli endpoint: `https://jsonplaceholder.typicode.com/posts?userId=1` per i post, `https://jsonplaceholder.typicode.com/posts/{post_id}/comments` per i commenti, e `https://jsonplaceholder.typicode.com/comments` per creare un commento.

Assicurati di gestire gli errori HTTP e di stampare i risultati in modo leggibile.

### Esempio di Output

```
--- Post dell'utente 1 ---
ID Post: 1, Titolo: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
ID Post: 2, Titolo: qui est esse
ID Post: 3, Titolo: ea molestias quasi exercitationem repellat qui ipsa sit aut

--- Commenti per il primo post ---
- id labore ex et quam laborum: laudantium enim quasi est quidem magnam voluptate ipsam eos
- quo vero reiciendis velit similique earum: est natus enim nihil est dolore omnis voluptatem numquam

--- Nuovo Commento Creato ---
{
    "postId": 1,
    "id": 501,
    "name": "Nuovo Commentatore",
    "email": "nuovo@example.com",
    "body": "Questo è un commento aggiunto tramite API!"
}
```