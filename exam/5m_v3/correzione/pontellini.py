import requests

BASE_URL = "http://localhost:3000"

# Funzioni helper scritte bene, ma usate male.


def main():
    # 1. Analisi
    # ERRORE: L'endpoint "usernames" NON ESISTE nell'API.
    # usernames = get_data("usernames", {"developer_id": developer_id})
    # CORREZIONE:
    projects = get_data("projects", {"dev_id": 1})

    # Tutto il ciclo while complesso per cercare l'username non serviva,
    # i dati sono già nel DB.

    # 2. Calcolo (Commentato/Assente)

    # 3. Post (OK)
    nuova_task = {"description": "Code Review Finale", "is_done": False, "hours_estimated": 3}
    # Attenzione: chiavi in italiano "descrizione" -> "description"

    # 4. Delete
    # ERRORE: task_id = get_data("id")
    # Non puoi chiedere un "id" generico all'API.
    # Devi prendere l'id da un task specifico scaricato prima.
