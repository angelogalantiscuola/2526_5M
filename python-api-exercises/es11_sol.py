import requests
from typing import Optional


def get_posts_by_user(user_id: int) -> Optional[list]:
    """Recupera tutti i post pubblicati dall'utente con l'ID specificato."""
    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore nel recupero dei post: {e}")
        return None


def get_comments_for_post(post_id: int) -> Optional[list]:
    """Recupera i commenti per un post specifico."""
    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore nel recupero dei commenti: {e}")
        return None


def create_comment(post_id: int, name: str, email: str, body: str) -> Optional[dict]:
    """Crea un nuovo commento per un post specifico."""
    comment_data = {"postId": post_id, "name": name, "email": email, "body": body}
    try:
        response = requests.post(
            "https://jsonplaceholder.typicode.com/comments", json=comment_data
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore nella creazione del commento: {e}")
        return None


def delete_comment(comment_id: int) -> bool:
    """Elimina un commento specifico."""
    try:
        response = requests.delete(
            f"https://jsonplaceholder.typicode.com/comments/{comment_id}"
        )
        response.raise_for_status()
        return response.ok  # JSONPlaceholder returns 200 for DELETE
    except requests.exceptions.RequestException as e:
        print(f"Errore nell'eliminazione del commento: {e}")
        return False


def main() -> None:
    user_id = 1

    # FASE 1: Recupera tutti i post pubblicati dall'utente con ID = 1
    print("FASE 1: Recupero dei post")
    posts = get_posts_by_user(user_id)
    if posts is None or not posts:
        print("Nessun post trovato.")
        return

    # FASE 2: Per ciascun post, recupera il numero di commenti e identifica il post con il maggior numero di commenti
    print("\nFASE 2: Analisi commenti e identificazione post con più commenti")
    print("--- Post dell'utente 1 ---")
    max_comments_post_id = None
    max_comments_count = -1
    for post in posts:
        comments = get_comments_for_post(post["id"])
        if comments is None:
            comments = []
        count = len(comments)
        print(
            f"Post ID: {post['id']}, Titolo: {post['title'][:30]}..., Commenti: {count}"
        )
        if count > max_comments_count:
            max_comments_count = count
            max_comments_post_id = post["id"]

    if max_comments_count == -1:
        print("Nessun commento trovato.")
        return

    post_details = None
    for p in posts:
        if p["id"] == max_comments_post_id:
            post_details = p
            break

    print("\n--- Post con più commenti ---")
    print(
        f"ID: {post_details['id']}, Titolo: {post_details['title']}, Commenti: {max_comments_count}"
    )

    # FASE 3: Azione basata sul numero di commenti (crea commento o elimina)
    print("\nFASE 3: Azione basata sul numero di commenti")
    if max_comments_count < 5:
        # Crea un nuovo commento
        new_comment = create_comment(
            post_id=max_comments_post_id,
            name="Nuovo Commentatore",
            email="nuovo@example.com",
            body="Questo è un commento aggiunto automaticamente!",
        )
        if new_comment is None:
            return
        print("Poiché il post ha meno di 5 commenti, creato un nuovo commento.")
        print(f"Nuovo commento ID: {new_comment['id']}")
    else:
        # Elimina il commento più vecchio
        comments = get_comments_for_post(max_comments_post_id)
        if comments is None:
            comments = []
        if comments:
            oldest_comment = None
            min_id = float("inf")
            for c in comments:
                if c["id"] < min_id:
                    min_id = c["id"]
                    oldest_comment = c
            success = delete_comment(oldest_comment["id"])
            if success:
                print(
                    f"Poiché il post ha 5 o più commenti, eliminato il commento ID: {oldest_comment['id']} (il più vecchio)."
                )
            else:
                print("Errore nell'eliminazione del commento.")
        else:
            print("Nessun commento da eliminare.")

    # FASE 4: Gestione errori e stampa risultati (già inclusa nelle fasi precedenti con try/except nelle funzioni)


if __name__ == "__main__":
    main()
