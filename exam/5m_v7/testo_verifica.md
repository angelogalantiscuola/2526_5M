# VERIFICA RECUPERO: Ristorante - Flask App

## Istruzioni Iniziali

### Setup
```bash
python setup_db.py
python run.py
```
Visita: `http://localhost:5000`

### File da Completare
- `app/repositories/categoria_repository.py` → funzioni CRUD categorie
- `app/repositories/piatto_repository.py` → funzioni CRUD piatti + ricerca
- `app/main.py` → tutte le route Flask
- `app/templates/index.html`, `categoria_detail.html`, `crea_categoria.html`, `crea_piatto.html`, `ricerca.html`

### Suggerimenti
1. Usa `negozio_online` come riferimento - stessa struttura!
2. Usa `JOIN categorie` nelle query per il nome della categoria
3. Usa `LOWER()` nella ricerca per case-insensitive
4. Valida input: campi obbligatori e prezzo positivo
5. La ricerca deve avere link alle categorie

---

## Scenario
Devi creare un'applicazione Flask per gestire un **ristorante online** con categorie di portate e i relativi piatti. L'applicazione deve permettere di visualizzare i dati, crearli e fornire funzionalità di ricerca.

## Relazione Dati
- **Categoria**: id, nome → es. Antipasti, Primi, Secondi, Dolci
- **Piatto**: id, categoria_id, nome, prezzo
- Relazione: Una categoria ha molti piatti

---

## Schema del Database (Fornito)

```sql
DROP TABLE IF EXISTS piatti;
DROP TABLE IF EXISTS categorie;

CREATE TABLE categorie (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL
);

CREATE TABLE piatti (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  categoria_id INTEGER NOT NULL,
  nome TEXT NOT NULL,
  prezzo REAL NOT NULL,
  FOREIGN KEY (categoria_id) REFERENCES categorie (id)
);

-- Dati di esempio
INSERT INTO categorie (nome) VALUES ('Antipasti');
INSERT INTO categorie (nome) VALUES ('Primi');
INSERT INTO categorie (nome) VALUES ('Secondi');
INSERT INTO categorie (nome) VALUES ('Dolci');

INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (1, 'Bruschetta al Pomodoro', 5.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (1, 'Camarones al Ajillo', 8.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (2, 'Lasagne della Nonna', 12.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (2, 'Pappardelle al Cinghiale', 14.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (3, 'Branzino al Forno', 18.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (4, 'Tiramisu', 6.99);
```

---

## Esercizio 1: CRUD Categorie e Piatti

**Struttura richiesta:**

1. **File `app/repositories/categoria_repository.py`:**
   - `get_all_categories()` → lista categorie ordinate per nome
   - `get_category_by_id(category_id)` → una singola categoria
   - `create_category(nome)` → inserisce nuova categoria

2. **File `app/repositories/piatto_repository.py`:**
   - `get_all_piatti()` → lista di tutti i piatti (con nome categoria)
   - `get_piatti_by_category(category_id)` → piatti di una categoria specifica
   - `get_piatto_by_id(piatto_id)` → un singolo piatto
   - `create_piatto(category_id, nome, prezzo)` → inserisce nuovo piatto

3. **Route in `main.py`:**
   - `GET /` → lista categorie (index)
   - `GET /categoria/<id>` → dettaglio categoria con lista piatti
   - `GET /crea_categoria` → form per nuova categoria
   - `POST /crea_categoria` → salva categoria nel DB
   - `GET /crea_piatto` → form per nuovo piatto (select categoria)
   - `POST /crea_piatto` → salva piatto nel DB

4. **Template:**
   - `index.html` → lista categorie (link a dettagli)
   - `categoria_detail.html` → nome categoria + lista piatti (nome, prezzo)
   - `crea_categoria.html` → form con input nome
   - `crea_piatto.html` → form con select categoria, input nome/prezzo

**Checklist:**
- [ ] Due repository creati con funzioni CRUD
- [ ] 6 route implementate
- [ ] 4 template creati
- [ ] Navigazione funzionante tra categorie e dettagli
- [ ] Creazione di categorie e piatti operativa

---

## Esercizio 2: Ricerca Piatti

**Cosa fare:**

- **Funzione in `piatto_repository.py`:**
  - `find_piatti_by_name(search_term)` → cerca per nome piatto (case-insensitive, LIKE)
  - Restituisce piatti con nome categoria (tramite JOIN)
  - Ordina per categoria, poi per nome

- **Route in `main.py`:**
  - `GET /ricerca` → mostra form ricerca vuoto
  - `POST /ricerca` → recupera termine, chiama funzione, passa risultati

- **Template `ricerca.html`:**
  - Form di ricerca (sempre visibile)
  - Lista risultati: nome piatto | categoria | prezzo
  - Messaggio "Nessun piatto trovato" se vuota
  - Link al dettaglio categoria per ogni risultato

**Checklist:**
- [ ] Funzione `find_piatti_by_name()` in piatto_repository
- [ ] Route GET `/ricerca` (form vuoto)
- [ ] Route POST `/ricerca` (risultati)
- [ ] Template `ricerca.html` creato
- [ ] Ricerca case-insensitive funzionante

---

## Struttura Progetto Attesa

```
ristorante/
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── main.py
│   ├── schema.sql
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── categoria_repository.py
│   │   └── piatto_repository.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── categoria_detail.html
│       ├── crea_categoria.html
│       ├── crea_piatto.html
│       └── ricerca.html
├── instance/
├── run.py
├── setup_db.py
└── README.md
```

---

## Note Importanti

- Lo scheletro Flask è fornito: esegui `python setup_db.py` per inizializzare il DB
- Parti dal tuo progetto precedente (es. negozio_online) come riferimento
- I template usano `base.html` fornito con nav bar e style
- Usa sempre sanitizzazione/validazione su input
- Gestisci gli errori con `abort(404)` quando necessario
