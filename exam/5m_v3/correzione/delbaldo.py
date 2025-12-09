# Nessuna correzione sostanziale necessaria. Codice Eccellente.
# Unico appunto:
# Nella DELETE hai usato un query param:
# requests.delete(f"{BASE_URL}/tasks?id={n_task}")
#
# Lo standard REST preferisce l'ID nel percorso:
# requests.delete(f"{BASE_URL}/tasks/{n_task}")
