# Aggiungi queste funzioni a post_repository.py


def get_posts_by_author(author_id):
    """Recupera tutti i post di un autore specifico."""
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        WHERE p.author_id = ?
        ORDER BY p.created DESC
    """
    posts = db.execute(query, (author_id,)).fetchall()
    result = []
    for post in posts:
        post_dict = dict(post)
        post_dict["created"] = datetime.fromisoformat(post_dict["created"])
        result.append(post_dict)
    return result


def get_posts_by_month(year, month):
    """Recupera i post filtrati per anno e mese."""
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        WHERE strftime('%Y', p.created) = ? AND strftime('%m', p.created) = ?
        ORDER BY p.created DESC
    """
    # Formatta anno e mese come stringhe (mese con zero iniziale)
    year_str = str(year)
    month_str = str(month).zfill(2)
    posts = db.execute(query, (year_str, month_str)).fetchall()
    result = []
    for post in posts:
        post_dict = dict(post)
        post_dict["created"] = datetime.fromisoformat(post_dict["created"])
        result.append(post_dict)
    return result
