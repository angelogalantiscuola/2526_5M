from app.db import get_db


def get_all_games():
    """
    Recupera tutti i giochi.
    """
    db = get_db()
    query = """
        SELECT id, nome, numero_giocatori_massimo, durata_media, categoria
        FROM giochi
        ORDER BY nome
    """
    games = db.execute(query).fetchall()
    return [dict(game) for game in games]


def get_game_by_id(game_id):
    """Recupera un singolo gioco per ID."""
    db = get_db()
    query = """
        SELECT id, nome, numero_giocatori_massimo, durata_media, categoria
        FROM giochi
        WHERE id = ?
    """
    game = db.execute(query, (game_id,)).fetchone()
    if game:
        return dict(game)
    return None


def create_game(nome, numero_giocatori_massimo, durata_media, categoria):
    """Crea un nuovo gioco."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES (?, ?, ?, ?)", 
        (nome, numero_giocatori_massimo, durata_media, categoria)
    )
    db.commit()
    return cursor.lastrowid