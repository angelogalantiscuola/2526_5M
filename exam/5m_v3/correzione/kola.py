import requests

BASE_URL = "http://localhost:3000"

try:
    # 1. Analisi (OK)
    response = requests.get(f"{BASE_URL}/projects?dev_id=1")
    projects = response.json()

    # 2. Calcolo
    active_projects = []
    for p in projects:
        if p["status"] == "active":
            active_projects.append(p)

    for p in active_projects:
        # ERRORE SINTASSI F-STRING: Togli le parentesi tonde e gli apici dentro le graffe sono delicati
        # task_response = requests.get(f"{BASE_URL}/tasks?project_id=(p['id'])")
        # CORREZIONE:
        task_response = requests.get(f"{BASE_URL}/tasks?project_id={p['id']}")
        task = task_response.json()

        ore_totali = 0
        for i in task:
            # ERRORE ALLUCINAZIONE: Non esiste la chiave 'pages'.
            # CORREZIONE: i['hours_estimated']
            if "hours_estimated" in i:
                ore_totali += i["hours_estimated"]

    # 3. Assegnazione
    if len(active_projects) > 0:
        primo_progetto = active_projects[0]

        nuovo_task = {
            # ERRORE: Stavi passando la stringa letterale 'primo_progetto["id"]'
            "project_id": primo_progetto["id"],
            "description": "Code Review Finale",
            "is_done": False,
            "hours_estimated": 3,
        }

        # ERRORE VERBO: Per creare si usa POST, non PUT.
        # PUT serve per aggiornare/sostituire.
        post_response = requests.post(f"{BASE_URL}/tasks", json=nuovo_task)

    # 4. Pulizia
    # ERRORE: Stai provando a cancellare usando una variabile 'id' mai definita.
    # Dovevi trovare prima un task completato.
    # task = requests.delete(f"{BASE_URL}/tasks/{id}")

except Exception as e:
    print(e)
