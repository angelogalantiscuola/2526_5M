import sqlite3

import click
from flask import current_app, g


def get_db():
    """Ottiene la connessione al database."""
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """Chiude la connessione al database."""
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Inizializza il database con lo schema SQL."""
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


def init_app(app):
    """Registra i comandi di chiusura con l'app Flask."""
    app.teardown_appcontext(close_db)
