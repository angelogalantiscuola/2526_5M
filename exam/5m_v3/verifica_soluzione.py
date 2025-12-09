import requests
import json

BASE_URL = "http://localhost:3000"


def handle_request_error(func_name, exception):
    """Gestisce gli errori di connessione"""
    print(f"❌ Errore in {func_name}: {exception}")
    exit(1)


try:
    # ============================================================
    # 1. ANALISI SVILUPPATORE
    # ============================================================
    print("\n=== 1. ANALISI SVILUPPATORE ===")

    developer_id = 1
    response = requests.get(f"{BASE_URL}/projects?dev_id={developer_id}", timeout=5)
    response.raise_for_status()
    projects = response.json()

    print(f"Progetti dello sviluppatore ID={developer_id}:")
    for project in projects:
        print(f"  - {project['name']}: ${project['budget']}")

    # ============================================================
    # 2. CALCOLO CARICO DI LAVORO
    # ============================================================
    print("\n=== 2. CALCOLO CARICO DI LAVORO ===")

    active_projects = [p for p in projects if p["status"] == "active"]
    print(f"Progetti attivi: {len(active_projects)}")

    for project in active_projects:
        project_id = project["id"]
        project_name = project["name"]

        # Recupera tutti i task del progetto
        response = requests.get(f"{BASE_URL}/tasks?project_id={project_id}", timeout=5)
        response.raise_for_status()
        tasks = response.json()

        # Calcola somma ore per task non completati
        hours_pending = sum(task["hours_estimated"] for task in tasks if not task["is_done"])

        print(f"Progetto '{project_name}': {hours_pending} ore pendenti")

    # ============================================================
    # 3. ASSEGNAZIONE NUOVO TASK
    # ============================================================
    print("\n=== 3. ASSEGNAZIONE NUOVO TASK ===")

    if active_projects:
        first_active = active_projects[0]
        project_id = first_active["id"]
        project_name = first_active["name"]

        new_task = {
            "project_id": project_id,
            "description": "Code Review Finale",
            "is_done": False,
            "hours_estimated": 3,
        }

        response = requests.post(f"{BASE_URL}/tasks", json=new_task, timeout=5)
        response.raise_for_status()
        created_task = response.json()

        print(f"✅ Task creato per '{project_name}':")
        print(f"   ID: {created_task.get('id')}")
        print(f"   Descrizione: {created_task['description']}")
        print(f"   Ore stimate: {created_task['hours_estimated']}")
    else:
        print("❌ Nessun progetto attivo trovato!")

    # ============================================================
    # 4. PULIZIA
    # ============================================================
    print("\n=== 4. PULIZIA ===")

    # Recupera tutti i task
    response = requests.get(f"{BASE_URL}/tasks", timeout=5)
    response.raise_for_status()
    all_tasks = response.json()

    # Trova il primo task completato
    completed_task = None
    for task in all_tasks:
        if task["is_done"]:
            completed_task = task
            break

    if completed_task:
        task_id = completed_task["id"]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}", timeout=5)
        response.raise_for_status()

        print(f"✅ Task ID={task_id} eliminato ({completed_task['description']})")
    else:
        print("❌ Nessun task completato trovato")

except requests.exceptions.RequestException as e:
    handle_request_error("API call", e)
except json.JSONDecodeError as e:
    handle_request_error("JSON parsing", e)
except Exception as e:
    handle_request_error("Unexpected error", e)

print("\n=== VERIFICA COMPLETATA ===\n")
