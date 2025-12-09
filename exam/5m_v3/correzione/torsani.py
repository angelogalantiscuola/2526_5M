# CORREZIONE TOTALE RICHIESTA
import requests

# 1. Porta sbagliata (3001 invece di 3000)
# 2. Sintassi URL sbagliata (?dev_id{id} invece di ?dev_id={id})
# 3. utils non esiste o non è stato consegnato.
# 4. Manca il 90% del compito.


def sviluppatore(id):
    url = f"http://localhost:3000/projects?dev_id={id}"
    res = requests.get(url)
    print(res.json())
