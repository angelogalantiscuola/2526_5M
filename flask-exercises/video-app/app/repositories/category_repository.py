from app.db import get_db



def create_category(nome: str):
    """Crea una nuova categoria."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO categoria (nome) VALUES (?)", (nome,)
    )
    db.commit()
    return cursor.lastrowid
