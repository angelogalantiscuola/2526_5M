from app.db import get_db


def get_all_piatti():
    """Ottiene tutti i piatti con il nome della categoria."""
    db = get_db()
    piatti = db.execute(
        """SELECT p.id, p.nome, p.prezzo, p.categoria_id, c.nome as categoria_nome
           FROM piatti p
           JOIN categorie c ON p.categoria_id = c.id
           ORDER BY c.nome, p.nome"""
    ).fetchall()
    return piatti


def get_piatti_by_category(category_id):
    """Ottiene i piatti di una categoria specifica."""
    db = get_db()
    piatti = db.execute(
        """SELECT p.id, p.nome, p.prezzo, p.categoria_id, c.nome as categoria_nome
           FROM piatti p
           JOIN categorie c ON p.categoria_id = c.id
           WHERE p.categoria_id = ?
           ORDER BY p.nome""",
        (category_id,),
    ).fetchall()
    return piatti


def get_piatto_by_id(piatto_id):
    """Ottiene un piatto per ID."""
    db = get_db()
    piatto = db.execute(
        """SELECT p.id, p.nome, p.prezzo, p.categoria_id, c.nome as categoria_nome
           FROM piatti p
           JOIN categorie c ON p.categoria_id = c.id
           WHERE p.id = ?""",
        (piatto_id,),
    ).fetchone()
    return piatto


def create_piatto(category_id, nome, prezzo):
    """Crea un nuovo piatto."""
    db = get_db()
    db.execute("INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (?, ?, ?)", (category_id, nome, prezzo))
    db.commit()


def find_piatti_by_name(search_term):
    """Cerca piatti per nome (case-insensitive, LIKE)."""
    db = get_db()
    piatti = db.execute(
        """SELECT p.id, p.nome, p.prezzo, p.categoria_id, c.nome as categoria_nome
           FROM piatti p
           JOIN categorie c ON p.categoria_id = c.id
           WHERE LOWER(p.nome) LIKE LOWER(?)
           ORDER BY c.nome, p.nome""",
        (f"%{search_term}%",),
    ).fetchall()
    return piatti
