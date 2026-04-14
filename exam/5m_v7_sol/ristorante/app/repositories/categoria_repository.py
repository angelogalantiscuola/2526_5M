from app.db import get_db


def get_all_categories():
    """Ottiene tutte le categorie ordinate per nome."""
    db = get_db()
    categories = db.execute("SELECT id, nome FROM categorie ORDER BY nome").fetchall()
    return categories


def get_category_by_id(category_id):
    """Ottiene una categoria per ID."""
    db = get_db()
    category = db.execute("SELECT id, nome FROM categorie WHERE id = ?", (category_id,)).fetchone()
    return category


def create_category(nome):
    """Crea una nuova categoria."""
    db = get_db()
    db.execute("INSERT INTO categorie (nome) VALUES (?)", (nome,))
    db.commit()
