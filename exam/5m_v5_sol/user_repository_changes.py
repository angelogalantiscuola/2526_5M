# Aggiungi questa funzione a user_repository.py


def get_user_by_id(user_id):
    """Recupera un utente per ID."""
    db = get_db()
    user = db.execute("SELECT id, username FROM user WHERE id = ?", (user_id,)).fetchone()
    return dict(user) if user else None
