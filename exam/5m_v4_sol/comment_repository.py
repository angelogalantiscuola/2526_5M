# FILE: app/repositories/comment_repository.py
# NUOVO FILE - Crea questa classe

from app.db import get_db  # type: ignore
from datetime import datetime

def get_comments_by_post(post_id):
    """Recupera tutti i commenti di un post con JOIN su user."""
    db = get_db()
    query = """
        SELECT c.id, c.post_id, c.body, c.created, c.author_id, u.username
        FROM comment c
        JOIN user u ON c.author_id = u.id
        WHERE c.post_id = ?
        ORDER BY c.created DESC
    """
    comments = db.execute(query, (post_id,)).fetchall()
    result = []
    for comment in comments:
        comment_dict = dict(comment)
        comment_dict['created'] = datetime.fromisoformat(comment_dict['created'])
        result.append(comment_dict)
    return result

def create_comment(post_id, author_id, body):
    """Crea un nuovo commento."""
    db = get_db()
    db.execute(
        'INSERT INTO comment (post_id, author_id, body) VALUES (?, ?, ?)',
        (post_id, author_id, body)
    )
    db.commit()
