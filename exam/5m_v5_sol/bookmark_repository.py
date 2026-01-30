from app.db import get_db
from datetime import datetime


def add_bookmark(user_id, post_id):
    """Aggiunge un post ai preferiti dell'utente."""
    db = get_db()
    db.execute("INSERT INTO bookmark (user_id, post_id) VALUES (?, ?)", (user_id, post_id))
    db.commit()


def remove_bookmark(user_id, post_id):
    """Rimuove un post dai preferiti dell'utente."""
    db = get_db()
    db.execute("DELETE FROM bookmark WHERE user_id = ? AND post_id = ?", (user_id, post_id))
    db.commit()


def get_user_bookmarks(user_id):
    """Recupera tutti i post salvati dall'utente con info complete."""
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username, b.created as bookmarked_at
        FROM bookmark b
        JOIN post p ON b.post_id = p.id
        JOIN user u ON p.author_id = u.id
        WHERE b.user_id = ?
        ORDER BY b.created DESC
    """
    bookmarks = db.execute(query, (user_id,)).fetchall()
    result = []
    for bookmark in bookmarks:
        bookmark_dict = dict(bookmark)
        bookmark_dict["created"] = datetime.fromisoformat(bookmark_dict["created"])
        bookmark_dict["bookmarked_at"] = datetime.fromisoformat(bookmark_dict["bookmarked_at"])
        result.append(bookmark_dict)
    return result


def is_bookmarked(user_id, post_id):
    """Verifica se un post è nei preferiti dell'utente."""
    db = get_db()
    bookmark = db.execute("SELECT 1 FROM bookmark WHERE user_id = ? AND post_id = ?", (user_id, post_id)).fetchone()
    return bookmark is not None
