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


def main() -> None:
    user_id = 1

    # 1. Recupera tutti i post pubblicati dall'utente con ID = 1
    posts = get_posts_by_user(user_id)
    if posts is None:
        return

    print("--- Post dell'utente 1 ---")
    for post in posts:
        print(f"ID Post: {post['id']}, Titolo: {post['title']}")

    if not posts:
        print("Nessun post trovato.")
        return

    # Ottieni l'ID del primo post
    first_post_id = posts[0]["id"]

    # 2. Recupera i commenti per il primo post
    comments = get_comments_for_post(first_post_id)
    if comments is None:
        return

    print("\n--- Commenti per il primo post ---")
    for comment in comments:
        print(f"- {comment['name']}: {comment['body']}")

    # 3. Crea un nuovo commento per il primo post
    new_comment = create_comment(
        post_id=first_post_id,
        name="Nuovo Commentatore",
        email="nuovo@example.com",
        body="Questo è un commento aggiunto tramite API!",
    )
    if new_comment is None:
        return

    print("\n--- Nuovo Commento Creato ---")
    print(new_comment)


if __name__ == "__main__":
    main()
