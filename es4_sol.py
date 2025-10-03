import sqlite3
from typing import List, Tuple

# Connessione al database SQLite 'scuola.db'
conn: sqlite3.Connection = sqlite3.connect("scuola.db")
cursor: sqlite3.Cursor = conn.cursor()

try:
    # Creazione delle tabelle se non esistono
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Studenti (
            Matricola INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Cognome TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Esami (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Matricola INTEGER NOT NULL,
            Corso TEXT NOT NULL,
            Voto INTEGER,
            FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
        )
    """)

    # Inserimento dati degli studenti
    cursor.execute(
        "INSERT OR IGNORE INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)", (101, "Mario", "Rossi")
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)", (102, "Lucia", "Bianchi")
    )

    # Inserimento esami per ogni studente
    esami: List[Tuple[int, str, int]] = [
        (101, "Matematica", 28),
        (101, "Informatica", 30),
        (101, "Fisica", 27),
        (102, "Matematica", 28),
        (102, "Informatica", 30),
        (102, "Fisica", 27),
    ]
    cursor.executemany("INSERT INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?)", esami)

    # Conferma delle modifiche
    conn.commit()

    print("Database creato e dati inseriti con successo.\n")

    # Query 1: Elenco di tutti gli studenti (Matricola, Nome, Cognome)
    print("1) Elenco di tutti gli studenti:")
    cursor.execute("SELECT Matricola, Nome, Cognome FROM Studenti")
    studenti: List[Tuple[int, str, str]] = cursor.fetchall()
    for studente in studenti:
        print(f"Matricola: {studente[0]}, Nome: {studente[1]}, Cognome: {studente[2]}")
    print()

    # Query 2: Elenco dei corsi e voti sostenuti da uno studente specifico (matricola 101)
    print("2) Elenco dei corsi e voti sostenuti dallo studente con matricola 101:")
    cursor.execute("SELECT Corso, Voto FROM Esami WHERE Matricola = ?", (101,))
    esami_studente: List[Tuple[str, int]] = cursor.fetchall()
    for esame in esami_studente:
        print(f"Corso: {esame[0]}, Voto: {esame[1]}")
    print()

    # Query 3: Numero di esami sostenuti per ciascuno studente
    print("3) Numero di esami sostenuti per ciascuno studente:")
    cursor.execute("SELECT Matricola, COUNT(*) AS num_esami FROM Esami GROUP BY Matricola")
    conteggi: List[Tuple[int, int]] = cursor.fetchall()
    for conteggio in conteggi:
        print(f"Matricola: {conteggio[0]}, Numero esami: {conteggio[1]}")

finally:
    # Chiusura connessione
    conn.close()

print("\nConnessione chiusa.")
