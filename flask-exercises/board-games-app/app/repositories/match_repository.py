from app.db import get_db


def get_matches_by_game(game_id):
    """
    Recupera tutte le partite di un gioco.
    """
    db = get_db()
    query = """
        SELECT id, gioco_id, data, vincitore, punteggio_vincitore
        FROM partite
        WHERE gioco_id = ?
        ORDER BY data DESC
    """
    matches = db.execute(query, (game_id,)).fetchall()
    return [dict(match) for match in matches]


def get_match_by_id(match_id):
    """Recupera una singola partita per ID."""
    db = get_db()
    query = """
        SELECT id, gioco_id, data, vincitore, punteggio_vincitore
        FROM partite
        WHERE id = ?
    """
    match = db.execute(query, (match_id,)).fetchone()
    if match:
        return dict(match)
    return None


def create_match(gioco_id, data, vincitore, punteggio_vincitore):
    """Crea una nuova partita."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (?, ?, ?, ?)",
        (gioco_id, data, vincitore, punteggio_vincitore),
    )
    db.commit()
    return cursor.lastrowid