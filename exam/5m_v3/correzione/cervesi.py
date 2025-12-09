import requests

BASE_URL = "http://localhost:3000"

try:
    # 1. Analisi (PERFETTO)
    response = requests.get(f"{BASE_URL}/projects?dev_id=1")
    response.raise_for_status()
    projects = response.json()

    print("Progetti dello sviluppatore con ID = 1:")
    for p in projects:
        print(f"- {p['name']}  (budget:  {p['budget']})")

    # 2. Calcolo (PERFETTO)
    print("\nCarico di lavoro sui progetti attivi:")
    for p in projects:
        if p["status"] == "active":
            # Piccolo typo mancante '=' ma logica corretta
            tasks_resp = requests.get(f"{BASE_URL}/tasks?project_id={p['id']}")
            tasks_resp.raise_for_status()
            tasks = tasks_resp.json()

            # Ottima logica di filtraggio manuale
            total_hours = 0
            for t in tasks:
                if t["is_done"] is False:
                    total_hours += t["hours_estimated"]

            print(f"- {p['name']}:  {total_hours} ore rimanenti")

    # --- PARTI MANCANTI AGGIUNTE PER STUDIO ---

    # 3. Assegnazione
    first_active = None
    for p in projects:
        if p["status"] == "active":
            first_active = p
            break

    if first_active:
        payload = {
            "project_id": first_active["id"],
            "description": "Code Review Finale",
            "is_done": False,
            "hours_estimated": 3,
        }
        # Manca la chiamata POST
        requests.post(f"{BASE_URL}/tasks", json=payload)

    # 4. Pulizia
    all_tasks_resp = requests.get(f"{BASE_URL}/tasks")
    all_tasks = all_tasks_resp.json()

    for t in all_tasks:
        if t["is_done"] is True:
            # Manca la chiamata DELETE
            requests.delete(f"{BASE_URL}/tasks/{t['id']}")
            break

except requests.exceptions.RequestException as e:
    print(f"Errore nella richiesta: {e}")
