# Codice eccellente e modulare.
# Unico errore sintattico nell'obiettivo 4:


def Pulizia():
    # ...
    prima_task = tasks[0]["id"]

    # ERRORE URL: Hai scritto .../tasks?{prima_task}
    # Questo genera un URL invalido con query string senza chiave.
    # CORREZIONE:
    url = f"http://localhost:3000/tasks/{prima_task}"

    response = requests.delete(url)
