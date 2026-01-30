# FILE: app/repositories/post_repository.py
# Aggiungi queste funzioni al file esistente

def get_post_by_id(post_id):
    """Recupera un singolo post per ID (con JOIN per l'autore)."""
    from app.db import get_db # type: ignore
    from datetime import datetime
    
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        WHERE p.id = ?
    """
    post = db.execute(query, (post_id,)).fetchone()
    if post:
        post_dict = dict(post)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        return post_dict
    return None

def search_posts_by_title(search_term):
    """Cerca post il cui titolo contenga search_term (case-insensitive)."""
    from app.db import get_db # type: ignore
    from datetime import datetime
    
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        WHERE LOWER(p.title) LIKE LOWER(?)
        ORDER BY p.created DESC
    """
    posts = db.execute(query, (f'%{search_term}%',)).fetchall()
    result = []
    for post in posts:
        post_dict = dict(post)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        result.append(post_dict)
    return result
