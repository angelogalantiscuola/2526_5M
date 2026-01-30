# VERIFICA: Estensione Blog Flask

## Scenario
L'applicazione blog fornita è incompleta. Devi aggiungere tre funzionalità principali per permettere ai visitatori di vedere il profilo degli autori, consultare l'archivio per data, e salvare i post preferiti.

## Flusso dell'Applicazione
1. **Profilo Utente** (`/user/<id>`) → pagina con info utente + lista dei suoi post
2. **Archivio** (`/archive`) → form per filtrare post per mese/anno → risultati
3. **Preferiti** → salva/rimuovi post, pagina con lista preferiti

---

## Esercizi

### 1. Profilo Utente
**Cosa fare:**
- Aggiungi funzione `get_posts_by_author(author_id)` in `post_repository.py`
  - Restituisce lista di post di un autore specifico (ordine: più recenti prima)
- Aggiungi funzione `get_user_by_id(user_id)` in `user_repository.py`
  - Restituisce i dati dell'utente (id, username)
- Crea route `/user/<int:id>` in `main.py`
- Crea template `user_profile.html` che mostra:
  - Username dell'utente
  - Numero totale di post scritti
  - Lista dei suoi post (titolo, data, link al dettaglio)
- Se l'utente non esiste, mostra errore 404

---

### 2. Archivio Post per Data
**Cosa fare:**
- Aggiungi funzione `get_posts_by_month(year, month)` in `post_repository.py`
  - Filtra i post per anno e mese di creazione
  - Restituisce lista di post con autore
- Crea route `/archive` (GET + POST) in `main.py`
  - GET: mostra form di selezione data
  - POST: recupera anno/mese, chiama la funzione, passa risultati al template
- Crea template `archive.html` che mostra:
  - Form di selezione (sempre visibile)
  - Lista risultati
  - Messaggio "nessun post trovato" se vuota

**Hint SQL:** Per filtrare per anno e mese in SQLite usa `strftime`:
```sql
WHERE strftime('%Y', p.created) = '2026' AND strftime('%m', p.created) = '01'
```

---

### 3. Sistema Preferiti
**Cosa fare:**
- Modifica `schema.sql`: aggiungi tabella `bookmark` per memorizzare i preferiti
  - Ogni preferito collega un utente a un post
  - Non permettere duplicati (stessa coppia utente-post)
  - Memorizza anche la data di salvataggio
  - Scegli i nomi e i tipi di colonna appropriati

- Crea file `app/repositories/bookmark_repository.py` con:
  - `add_bookmark(user_id, post_id)` → aggiunge preferito
  - `remove_bookmark(user_id, post_id)` → rimuove preferito
  - `get_user_bookmarks(user_id)` → lista post salvati dall'utente (con info post)
  - `is_bookmarked(user_id, post_id)` → restituisce True/False

- Aggiungi route POST `/post/<int:id>/bookmark` in `main.py`:
  - Verifica che l'utente sia loggato
  - Se già salvato → rimuovi, altrimenti → aggiungi (toggle)
  - Redirect alla home

- Crea route GET `/bookmarks` in `main.py`:
  - Verifica che l'utente sia loggato
  - Mostra lista dei post salvati

- Crea template `bookmarks.html`:
  - Lista dei post preferiti (titolo, autore, data)
  - Link per rimuovere ogni preferito
  - Messaggio "nessun preferito" se lista vuota

- Modifica template `index.html`:
  - Per ogni post, aggiungi icona/bottone "Salva" o "Salvato" (solo se loggato)
  - Il bottone deve essere un form che fa POST a `/post/<id>/bookmark`

**Importante:** La funzionalità toggle (aggiungi/rimuovi) usa la stessa route!
