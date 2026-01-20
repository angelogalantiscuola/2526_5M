from app.db import get_db


def get_all_channels():
    """
    Recupera tutti i canali.
    """
    db = get_db()
    query = """
        SELECT id, nome, numero_iscritti, categoria
        FROM canali
        ORDER BY numero_iscritti DESC
    """
    channels = db.execute(query).fetchall()
    return [dict(channel) for channel in channels]


def get_channel_by_id(channel_id):
    """Recupera un singolo canale per ID."""
    db = get_db()
    query = """
        SELECT id, nome, numero_iscritti, categoria
        FROM canali
        WHERE id = ?
    """
    channel = db.execute(query, (channel_id,)).fetchone()
    if channel:
        return dict(channel)
    return None


def create_channel(nome, numero_iscritti, categoria):
    """Crea un nuovo canale."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO canali (nome, numero_iscritti, categoria) VALUES (?, ?, ?)", (nome, numero_iscritti, categoria)
    )
    db.commit()
    return cursor.lastrowid
