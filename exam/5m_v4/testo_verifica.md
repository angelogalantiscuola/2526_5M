# VERIFICA: Estensione Blog Flask

## Scenario
L'applicazione blog fornita è incompleta. Devi aggiungere tre funzionalità principali per permettere ai visitatori di vedere i dettagli dei post, cercarli, e commentarli.

## Flusso dell'Applicazione
1. **Dettaglio Post** (`/post/<id>`) → pagina completa del post + sezione commenti
2. **Ricerca** (`/search`) → form di ricerca → risultati
3. **Aggiunta Commento** → form nella pagina di dettaglio (non una pagina separata!)

---

## Esercizi

### 1. Dettaglio Post
**Cosa fare:**
- Crea route `/post/<int:id>` in `main.py`
- Crea nuovo template `blog/detail.html` che mostra:
  - Titolo, autore, data di creazione, corpo completo
  - Link "Torna alla home"
- Recupera il post usando `post_repository.get_post_by_id(id)`
- Se il post non esiste, mostra errore 404

---

### 2. Ricerca Post
**Cosa fare:**
- Aggiungi funzione `search_posts_by_title(search_term)` in `post_repository.py`
  - Cerca per titolo (case-insensitive, usa `LIKE`)
  - Restituisce lista di post con autore
- Crea route `/search` (GET + POST) in `main.py`
  - GET: mostra form di ricerca vuoto
  - POST: recupera il termine, chiama la funzione, passa risultati al template
- Crea template `search_results.html` che mostra:
  - Form di ricerca (sempre visibile)
  - Lista risultati
  - Messaggio "nessun risultato" se vuota

---

### 3. Commenti
**Cosa fare:**
- Modifica `schema.sql`: aggiungi tabella `comment` per memorizzare i commenti
  - Ogni commento ha: un testo e una data di creazione
  - Ogni commento si riferisce a un post specifico e a un autore specifico
  - Scegli i nomi e i tipi di colonna appropriati

- Crea file `app/repositories/comment_repository.py` con:
  - `get_comments_by_post(post_id)` → lista commenti con autore
  - `create_comment(post_id, author_id, body)` → inserisce commento

- Modifica template `detail.html` aggiungendo sezione commenti:
  - **Se loggato:** form textarea per scrivere commento
  - **Se non loggato:** link al login
  - Elenco commenti (autore, data, testo)

- Aggiungi route POST `/post/<int:id>/comment` in `main.py`:
  - Verifica che l'utente sia loggato
  - Recupera il corpo del commento dal form
  - Chiama `create_comment()`
  - Redirect alla pagina del post

**Importante:** Il form per aggiungere commenti è **nella stessa pagina di dettaglio**, non una pagina separata!
