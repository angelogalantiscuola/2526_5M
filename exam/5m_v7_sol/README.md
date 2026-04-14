# Soluzione Esercizio 5M v7 - Ristorante

## Panoramica

Soluzione completa dell'app Flask **Ristorante** con:
- **Esercizio 1:** CRUD categorie e piatti (6 route + 4 template)
- **Esercizio 2:** Ricerca piatti per nome (1 route + 1 template)

## Struttura File

```
ristorante/
├── app/
│   ├── __init__.py           → Application factory
│   ├── db.py                 → Gestione database
│   ├── main.py               → Tutte le route (8 totali)
│   ├── schema.sql            → Schema + dati di esempio
│   ├── repositories/
│   │   ├── categoria_repository.py   → CRUD categorie
│   │   └── piatto_repository.py      → CRUD piatti + ricerca
│   └── templates/
│       ├── base.html                 → Layout base
│       ├── index.html                → Lista categorie
│       ├── categoria_detail.html     → Dettaglio categoria
│       ├── crea_categoria.html       → Form creazione categoria
│       ├── crea_piatto.html          → Form creazione piatto
│       └── ricerca.html              → Form ricerca
├── instance/
├── run.py
├── setup_db.py
└── README.md
```

## Esercizio 1: CRUD Completo

### Repository (`categoria_repository.py`, `piatto_repository.py`)

**Categoria:**
- `get_all_categories()` → lista ordinate per nome
- `get_category_by_id(id)` → singola categoria
- `create_category(nome)` → inserisce nuova categoria

**Piatto:**
- `get_all_piatti()` → tutti i piatti con categoria (JOIN)
- `get_piatti_by_category(id)` → piatti di una categoria
- `get_piatto_by_id(id)` → singolo piatto
- `create_piatto(cat_id, nome, prezzo)` → inserisce nuovo piatto

### Route (`main.py`)

| Method | Route | Descrizione |
|--------|-------|------------|
| GET | `/` | Lista categorie |
| GET | `/categoria/<id>` | Dettaglio categoria + lista piatti |
| GET/POST | `/crea_categoria` | Form creazione categoria |
| GET/POST | `/crea_piatto` | Form creazione piatto (con select categoria) |

### Template

- `index.html` → lista categorie come card clickabili
- `categoria_detail.html` → tabella piatti con nome e prezzo
- `crea_categoria.html` → form input nome
- `crea_piatto.html` → form select categoria + input nome/prezzo

---

## Esercizio 2: Ricerca Piatti

### Repository (`piatto_repository.py`)

**Funzione:**
- `find_piatti_by_name(search_term)` 
  - Ricerca CASE-INSENSITIVE con `LOWER(nome) LIKE LOWER(?)`
  - Usa JOIN con categorie
  - Ordina per categoria → nome

### Route (`main.py`)

| Method | Route | Descrizione |
|--------|-------|------------|
| GET/POST | `/ricerca` | Form ricerca (sempre visibile) + risultati |

### Template

- `ricerca.html`
  - Form ricerca sempre visibile
  - Tabella risultati: Nome Piatto | Categoria (link) | Prezzo
  - Messaggio "Nessun piatto trovato" se vuota

---

## Punti Chiave Implementativi

1. **Query con JOIN:** Tutti i piatti includono il nome categoria tramite `JOIN categorie`
2. **Case-insensitive search:** Usa `LOWER()` per ricerche robuste
3. **Validazione input:** Controllo campo obbligatorio + prezzo positivo
4. **404 handling:** `abort(404)` per categoria non trovata
5. **Link navigazione:** Categoria detail è clickabile dalla ricerca
6. **Formattazione prezzo:** `"%.2f"|format()` nei template

---

## Esecuzione

```bash
# Inizializzare il database
python setup_db.py

# Avviare l'app
python run.py
```

Navigare a: `http://localhost:5000`

---

## Dati di Esempio Caricati

**Categorie:** Antipasti, Primi, Secondi, Dolci

**Piatti:**
- Bruschetta al Pomodoro (5.99€) - Antipasti
- Camarones al Ajillo (8.99€) - Antipasti
- Lasagne della Nonna (12.99€) - Primi
- Pappardelle al Cinghiale (14.99€) - Primi
- Branzino al Forno (18.99€) - Secondi
- Tiramisu (6.99€) - Dolci
