# SOLUZIONE VERIFICA 5M_V4 - Blog Flask

## Struttura dei file

I file in questa cartella contengono **solo le modifiche/aggiunte** rispetto a `blog_scolastico`:

### File da aggiungere/modificare:

1. **schema_changes.sql**
   - Aggiungi la tabella `comment` al file `app/schema.sql`

2. **comment_repository.py** ← NUOVO FILE
   - Copia in `app/repositories/comment_repository.py`

3. **post_repository_changes.py**
   - Aggiungi le funzioni `get_post_by_id()` e `search_posts_by_title()` a `app/repositories/post_repository.py`

4. **main_changes.py**
   - Aggiungi le route `post_detail()`, `search()`, `add_comment()` a `app/main.py`
   - Mantieni tutte le route esistenti (index, about, create, update, delete)

5. **detail.html** ← NUOVO FILE
   - Copia in `app/templates/blog/detail.html`

6. **search_results.html** ← NUOVO FILE
   - Copia in `app/templates/search_results.html`

7. **index_changes_note.txt**
   - Leggi le istruzioni per modificare `index.html` (aggiungi link "Leggi tutto")

## Step di applicazione:

```bash
# 1. Aggiorna schema
cat schema_changes.sql >> app/schema.sql

# 2. Aggiungi comment_repository.py
cp comment_repository.py app/repositories/comment_repository.py

# 3. Aggiungi templates
cp detail.html app/templates/blog/detail.html
cp search_results.html app/templates/search_results.html

# 4. Manualmente: aggiungi le funzioni da post_repository_changes.py a post_repository.py
# 5. Manualmente: aggiungi le route da main_changes.py a main.py
# 6. Manualmente: modifica index.html secondo index_changes_note.txt

# 7. Reinizializza DB
python setup_db.py

# 8. Testa
python run.py
```

## Note

- **Attenzione:** Ricorda che in SQLite le colonne di `post` devono rimanere come sono, solo la tabella `comment` è nuova
- Importa `comment_repository` in `main.py`
- Verifica che `get_post()` sia disponibile come funzione helper già nel codice base
