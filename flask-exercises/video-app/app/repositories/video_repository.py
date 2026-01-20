from app.db import get_db


def get_videos_by_channel(channel_id):
    """
    Recupera tutti i video di un canale.
    """
    db = get_db()
    query = """
        SELECT id, canale_id, titolo, durata, immagine
        FROM video
        WHERE canale_id = ?
        ORDER BY titolo
    """
    videos = db.execute(query, (channel_id,)).fetchall()
    return [dict(video) for video in videos]


def get_video_by_id(video_id):
    """Recupera un singolo video per ID."""
    db = get_db()
    query = """
        SELECT id, canale_id, titolo, durata, immagine
        FROM video
        WHERE id = ?
    """
    video = db.execute(query, (video_id,)).fetchone()
    if video:
        return dict(video)
    return None


def create_video(canale_id, titolo, durata, immagine):
    """Crea un nuovo video."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (?, ?, ?, ?)",
        (canale_id, titolo, durata, immagine),
    )
    db.commit()
    return cursor.lastrowid
