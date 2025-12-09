import requests

BASE_URL = "http://localhost:3000"

try:
    # 1. Analisi (BENE)
    response = requests.get(f"{BASE_URL}/projects?dev_id=1")
    response.raise_for_status()
    projects = response.json()

    # 2. Calcolo
    active_projects = [project for project in projects if project["status"] == "active"]

    for project in active_projects:
        response = requests.get(f"{BASE_URL}/tasks?project_id={project['id']}")  # Era id, sintassi f-string corretta
        tasks = response.json()

        # ERRORE: Typo "hours_hestimated" (h di troppo)
        # ERRORE: Sovrascrivi la variabile 'hours' ad ogni giro invece di sommarle?
        # No, qui stai usando sum(), quindi va bene, ma attenzione al typo.
        hours = sum(task["hours_estimated"] for task in tasks if not task["is_done"])
        print(f"Ore progetto {project['name']}: {hours}")

    # 3. Assegnazione (ERRORE CONCETTUALE)
    if active_projects:
        active_project1 = active_projects[0]
        new_task = {
            "project_id": active_project1["id"],
            "description": "Code Review",
            "is_done": False,
            "hours_estimated": 3,
        }

        # ERRORE GRAVE: Stai passando l'intero dizionario DENTRO l'URL!
        # response = requests.post(f"{BASE_URL}/tasks/{new_task}")

        # CORREZIONE: Usa il parametro json=
        response = requests.post(f"{BASE_URL}/tasks", json=new_task)
        response.raise_for_status()

    # 4. Pulizia
    response = requests.get(f"{BASE_URL}/tasks")
    tasks = response.json()
    completed_tasks = [task for task in tasks if task["is_done"]]

    if completed_tasks:
        completed_task1 = completed_tasks[0]
        # ERRORE GRAVE: Stesso errore di prima. Passi tutto l'oggetto nell'URL.
        # response = requests.delete(f"{BASE_URL}/tasks/{completed_task1}")

        # CORREZIONE: Passa solo l'ID
        response = requests.delete(f"{BASE_URL}/tasks/{completed_task1['id']}")

except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
