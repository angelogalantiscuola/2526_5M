import requests
from typing import Optional


def get_todos_by_user(user_id: int) -> Optional[list]:
    """Recupera tutti i todos pubblicati dall'utente con l'ID specificato."""
    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore nel recupero dei todos: {e}")
        return None


def update_todo(todo_id: int, updated_data: dict) -> Optional[dict]:
    """Aggiorna un todo specifico con una richiesta PUT."""
    try:
        response = requests.put(
            f"https://jsonplaceholder.typicode.com/todos/{todo_id}", json=updated_data
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore nell'aggiornamento del todo: {e}")
        return None


def main() -> None:
    user_id: int = 1

    # 1. Recupera tutti i todos dell'utente con ID = 1
    lista_delle_cose_da_fare: Optional[list] = get_todos_by_user(user_id)
    if lista_delle_cose_da_fare is None:
        return

    print("--- Todos dell'utente 1 ---")
    total_todos = len(lista_delle_cose_da_fare)
    completed_todos = 0
    for todo in lista_delle_cose_da_fare:
        if todo["completed"]:
            completed_todos += 1
    incomplete_todos = total_todos - completed_todos

    print(f"Todos totali: {total_todos}")
    print(f"Completati: {completed_todos}")
    print(f"Incompleti: {incomplete_todos}")

    # 2. Trova il primo todo incompleto
    first_incomplete = None
    for todo in lista_delle_cose_da_fare:
        if not todo["completed"]:
            first_incomplete = todo
            break

    if first_incomplete is None:
        print("\nNessun todo incompleto trovato.")
        return

    print("\n--- Primo todo incompleto trovato ---")
    print(
        f"ID: {first_incomplete['id']}, Titolo: {first_incomplete['title']}, Completato: {first_incomplete['completed']}"
    )

    # 3. Marca come completato con PUT
    updated_todo = update_todo(first_incomplete["id"], {"completed": True})
    if updated_todo is None:
        return

    print("\n--- Todo aggiornato ---")
    print(
        f"ID: {updated_todo['id']}, Titolo: {first_incomplete['title']}, Completato: {updated_todo['completed']}"
    )


if __name__ == "__main__":
    main()
