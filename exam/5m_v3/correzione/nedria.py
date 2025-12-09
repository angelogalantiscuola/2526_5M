import requests

BASE_URL = "http://localhost:3000"

try:
    # 1. Progetti (OK)
    response = requests.get(f"{BASE_URL}/projects?dev_id=1")
    projects = response.json()

    # 2. Filtra
    # ERRORE FILTRO: Sintassi errata.
    # active_projects = [p for p in projects if p["'status' == 'active'"]]
    # CORREZIONE:
    active_projects = [p for p in projects if p["status"] == "active"]

    for project in active_projects:
        task_resp = requests.get(f"{BASE_URL}/tasks?project_id={project['id']}")
        tasks = task_resp.json()  # Attenzione all'indentazione!

        hours_needed = 0  # Variabile corretta
        for task in tasks:
            if task["is_done"] is False:
                # ERRORE TYPO: nedded
                # hours_nedded += task ['hours_estimated']
                hours_needed += task["hours_estimated"]

    # 3. Post
    # ...
    new_task_data = {...}  # OK

    # ERRORE SINTASSI PRINT:
    # print("Risposta Server:" post_resp.json() )
    # Manca la virgola o la f-string.
    # print("Risposta Server:", post_r.json())

except:
    pass
