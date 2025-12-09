import requests

BASE_URL = "http://localhost:3000"


def projects():
    # ERRORE ENDPOINT: /projects/tasks non esiste.
    # I task sono su /tasks.
    pass


def delete_task():
    # ERRORE LOGICO:
    # Stai iterando su 'lista_attivi' (che sono progetti)
    # e provi a cancellare task usando l'ID del progetto?
    # response = requests.delete(f".../tasks?project_id={i['id']}")
    #
    # La logica corretta era:
    # 1. Scarica i task (/tasks)
    # 2. Trova quello con is_done=True
    # 3. Usa il SUO id per fare DELETE /tasks/{id}
    pass
