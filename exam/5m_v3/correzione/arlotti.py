import requests
import json

# CORREZIONE: La porta richiesta era la 3000.
# Usando la 3004 lo script non riusciva a connettersi.
PORT = 3000  # Era 3004


def prendi_dati_link(link):
    try:
        risposta = requests.get(link)
        risposta.raise_for_status()
        lista = risposta.json()
    except Exception as e:
        # CONSIGLIO: Stampa l'errore specifico per capire cosa non va
        print(f"Errore connessione: {e}")
        risposta = False
        lista = False
    return lista


# 1. Analisi Sviluppatore
link_progetti = f"http://localhost:{PORT}/projects/?dev_id=1"
lista_progetti = prendi_dati_link(link_progetti)

print("")
# Controllo di sicurezza: se lista_progetti è False, il loop crasha
if lista_progetti:
    for progetto in lista_progetti:
        print(f"NOME: {progetto['name']}")
        print(f"BUDGET: {progetto['budget']}")

# 2. Calcolo Carico di Lavoro
if lista_progetti:
    for progetto in lista_progetti:
        # ERRORE LOGICO: `if progetto['status']:` controlla solo se la stringa non è vuota.
        # Anche "completed" è True in Python.
        # CORREZIONE: if progetto['status'] == 'active':
        if progetto["status"] == "active":
            link_tasks = f"http://localhost:{PORT}/tasks/?project_id={progetto['id']}"
            lista_tasks = prendi_dati_link(link_tasks)

            # MANCANZA: Il testo chiedeva la SOMMA delle ore.
            # Tu hai solo stampato i task.
            somma_ore = 0  # Inizializzazione accumulatore

            if lista_tasks:
                for task in lista_tasks:
                    # Filtra solo i non completati
                    if not task["is_done"]:
                        somma_ore += task["hours_estimated"]

            print(f"Progetto {progetto['name']} - Ore Totali Pendenti: {somma_ore}")

# 3. Assegnazione Nuovo Task
link_primo_progetto = f"http://localhost:{PORT}/projects"
lista_primo = prendi_dati_link(link_primo_progetto)

primo_progetto = None
if lista_primo:
    for i in lista_primo:
        if i["status"] == "active":
            primo_progetto = i
            break

if primo_progetto:
    link_task_nuovo = f"http://localhost:{PORT}/tasks/"
    id_trovato = primo_progetto["id"]

    dizionario_nuovo = {
        "project_id": id_trovato,
        "description": "Code Review Finale",
        "is_done": False,
        "hours_estimated": 3,
    }

    # BENE: Chiamata corretta
    response = requests.post(link_task_nuovo, json=dizionario_nuovo)
    print("Task creato:", response.status_code)

# 4. Pulizia
link_primo_tasks = f"http://localhost:{PORT}/tasks"
lista_primo_tasks = prendi_dati_link(link_primo_tasks)

primo_task = None
if lista_primo_tasks:
    for i in lista_primo_tasks:
        if i["is_done"]:
            primo_task = i
            break

if primo_task:
    # NOTA REST: L'ID per la cancellazione va nel PATH, non come query param.
    # TUO CODICE: .../tasks/?id=501
    # STANDARD:   .../tasks/501
    link_eliminare = f"http://localhost:{PORT}/tasks/{primo_task['id']}"

    response = requests.delete(link_eliminare)
    print("Task eliminato:", response.status_code)
