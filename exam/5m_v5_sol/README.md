# SOLUZIONE VERIFICA 5M_V5 - Blog Flask (Preferiti)

## Struttura dei file

I file in questa cartella contengono **solo le modifiche/aggiunte** rispetto a `blog_scolastico`:

### File da aggiungere/modificare:

1. **schema_changes.sql**
   - Aggiungi la tabella `bookmark` al file `app/schema.sql`

2. **bookmark_repository.py** ← NUOVO FILE
   - Copia in `app/repositories/bookmark_repository.py`

3. **post_repository_changes.py**
   - Aggiungi le funzioni `get_posts_by_author()` e `get_posts_by_month()` a `app/repositories/post_repository.py`

4. **user_repository_changes.py**
   - Aggiungi la funzione `get_user_by_id()` a `app/repositories/user_repository.py`

5. **main_changes.py**
   - Aggiungi le route `user_profile()`, `archive()`, `toggle_bookmark()`, `bookmarks()` a `app/main.py`
   - Mantieni tutte le route esistenti (index, about, create, update, delete)

6. **user_profile.html** ← NUOVO FILE
   - Copia in `app/templates/user_profile.html`

7. **archive.html** ← NUOVO FILE
   - Copia in `app/templates/archive.html`

8. **bookmarks.html** ← NUOVO FILE
   - Copia in `app/templates/bookmarks.html`

9. **index_changes.html**
   - Modifica `index.html` aggiungendo il bottone preferiti

## Step di applicazione:

```bash
# 1. Aggiorna schema
cat schema_changes.sql >> app/schema.sql

# 2. Aggiungi bookmark_repository.py
cp bookmark_repository.py app/repositories/bookmark_repository.py

# 3. Aggiungi templates
cp user_profile.html app/templates/user_profile.html
cp archive.html app/templates/archive.html
cp bookmarks.html app/templates/bookmarks.html

# 4. Manualmente: aggiungi le funzioni da post_repository_changes.py a post_repository.py
# 5. Manualmente: aggiungi la funzione da user_repository_changes.py a user_repository.py
# 6. Manualmente: aggiungi le route da main_changes.py a main.py
# 7. Manualmente: modifica index.html secondo index_changes.html

# 8. Reinizializza DB
python setup_db.py

# 9. Testa
python run.py
```

## Note

- Importa `bookmark_repository` e `user_repository` in `main.py`
- La PRIMARY KEY composta su (user_id, post_id) impedisce duplicati
- La route bookmark usa toggle: se esiste rimuove, altrimenti aggiunge
