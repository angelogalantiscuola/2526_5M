import requests

BASE_URL = "http://localhost:3000"

# ERRORE: Chiavi in italiano! L'API non capisce l'italiano.
# CORREZIONE: Usa le chiavi inglesi come da documentazione.
nuova_task = {
    "project_id": 103,
    "description": "Code review finale",  # Era "descrizione"
    "is_done": False,  # Era stringa "false"
    "hours_estimated": 3,  # Era "ore_stimate"
}

try:
    # 1. Analisi
    response = requests.get(f"{BASE_URL}/projects?dev_id=1")
    response.raise_for_status()
    projects = response.json()

    # 2. Calcolo (HARDCODING)
    active_projects = []
    for p in projects:
        # ERRORE: La chiave 'active' non esiste. L'API ritorna "status": "active".
        if p["status"] == "active":  # Era if p["active"]
            active_projects.append(p)

    # ERRORE GRAVE: Hai scritto codice specifico per ID 101, 102, 103.
    # Devi usare un ciclo generico!
    for progetto in active_projects:
        # Typo: "progect_id" -> "project_id"
        res = requests.get(f"{BASE_URL}/tasks?project_id={progetto['id']}")
        tasks = res.json()

        # Logica somma corretta qui sotto
        somma = 0
        for t in tasks:
            # Calcolo somma ore
            if not t["is_done"]:
                somma += t["hours_estimated"]
        print(f"Progetto {progetto['id']} ore mancanti: {somma}")

    # 3. Post
    # ERRORE: Stavi mandando la richiesta a BASE_URL (root) invece che a /tasks
    response = requests.post(f"{BASE_URL}/tasks", json=nuova_task)

    # 4. Delete
    response = requests.get(f"{BASE_URL}/tasks?is_done=True")
    task_completate = response.json()

    if task_completate:
        prima_task_trovata = task_completate[0]
        # ERRORE: Delete richiede l'ID nell'URL, non il json body.
        # response = requests.delete(BASE_URL, json=prima_task_trovata)

        id_da_cancellare = prima_task_trovata["id"]
        requests.delete(f"{BASE_URL}/tasks/{id_da_cancellare}")

except requests.exceptions.RequestException as e:
    print(f"Errore nella richiesta: {e}")
