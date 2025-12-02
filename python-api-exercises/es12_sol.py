import requests

BASE_URL = "http://localhost:3001"

try:
    # 1. Cerca Libri di un Autore
    response = requests.get(f"{BASE_URL}/books?author_id=1")
    response.raise_for_status()
    books = response.json()

    # Get author name
    author_response = requests.get(f"{BASE_URL}/authors/1")
    author_response.raise_for_status()
    author = author_response.json()

    print(f"Libri di {author['name']}:")
    for book in books:
        print(f"  - {book['title']} ({book['pages']} pagine)")

    # 2. Filtra per Disponibilità
    available_books = [book for book in books if book["available"]]
    print("\nLibri disponibili:")
    for book in available_books:
        print(f"  - {book['title']}")

    # 3. Conta Pagine Totali
    total_pages = sum(book["pages"] for book in available_books)
    print(f"\nPagine totali disponibili: {total_pages}")

    # 4. Libri per Genere
    response = requests.get(f"{BASE_URL}/books?genre_id=101")
    response.raise_for_status()
    fantasy_books = response.json()

    genre_response = requests.get(f"{BASE_URL}/genres/101")
    genre_response.raise_for_status()
    genre = genre_response.json()

    print(f"\nGenere: {genre['name']}")
    print(f"Numero di libri: {len(fantasy_books)}")

except requests.exceptions.RequestException as e:
    print(f"Errore nella richiesta: {e}")
