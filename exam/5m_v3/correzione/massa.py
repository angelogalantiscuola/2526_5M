import requests

BASE_URL = "http://localhost:3000"

# ... (Parte 1 OK) ...

# 2. Calcolo
# ... recupero task ...
    ore_non_finite = 0
    for t in tasks:
        is_done = t.get("is_done", False)
        if not is_done:
            # ERRORE CHIAVE: "ore stimate" non esiste. Usa "hours_estimated".
            ore = t.get("hours_estimated", 0)
            # ERRORE BUG: Stavi facendo += 0!
            # ore_non_finite += 0
            # CORREZIONE:
            ore_non_finite += ore

# 3. Post (OK)

# 4. Delete
# ...
    task_id = tasks_finito["id"]
    try: 
        # ERRORE SINTASSI: Stai cercando di cancellare la stringa "task_id"
        # url_del = BASE_URL + "/tasks/task_id"
        # CORREZIONE: Usa f-string per inserire il valore della variabile
        url_del = f"{BASE_URL}/tasks/{task_id}"
        
        res_del = requests.delete(url_del)
    except Exception as e:
        print("errore", e)