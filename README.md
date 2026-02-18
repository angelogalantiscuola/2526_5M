# 2526_5M

Repository centralizzato con esercizi e template per il corso 5M.

## Struttura

Gli esercizi sono organizzati per categoria:
- `sql-exercises/` - Esercizi SQL
- `python-sqlite-exercises/` - Esercizi Python + SQLite
- `python-api-exercises/` - Esercizi API REST
- `flask-exercises/` - Esercizi Flask
- `database-design-exercises/` - Esercizi di design database

## Git Subtree

I template dei classroom repos sono importati via `git subtree`:

```bash
# Aggiungere un nuovo template
git subtree add --prefix=flask-exercises/board-games-app \
  https://github.com/isissmorciano/2526-5m-board-games-app-board-games-app.git main

# Aggiornare un template esistente
git subtree pull --prefix=flask-exercises/board-games-app \
  https://github.com/isissmorciano/2526-5m-board-games-app-board-games-app.git main
```

**Nota**: Nel repo template, i file di configurazione (README.md, .gitignore) devono trovarsi dentro una subdirectory con lo stesso nome per evitare conflitti.