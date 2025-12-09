import requests


# 1. Analisi (Funzione OK)
def progetti_assegnati_sviluppatore(dev_id):
    # ... codice ok ...
    pass


# Funzioni definite ma MAI usate correttamente nel main per gli scopi richiesti.


def main():
    # 1. OK
    progetti_sviluppatore = progetti_assegnati_sviluppatore(1)

    # 2. Calcolo
    # ERRORE: La variabile 'progetti' non esiste qui. Si chiama 'progetti_sviluppatore'.
    # for progetto in progetti:
    for progetto in progetti_sviluppatore:
        # ERRORE: 'active' non è una chiave. Devi controllare lo status.
        # if progetto['active']:
        if progetto["status"] == "active":
            print(f"Progetto attivo: {progetto['name']}")
            # QUI MANCA TUTTO IL CODICE per scaricare i task e sommare le ore.

    # 3. Post
    # Hai preparato il dizionario 'nuova_task', ma non hai mai chiamato
    # la funzione 'aggiungi__nuova_task(nuova_task)'!
    # Il codice prepara i dati ma non fa nulla.

    # 4. Delete
    # Idem. Hai definito la funzione delete_task, ma non l'hai mai chiamata.
