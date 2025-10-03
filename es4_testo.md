# Esercizio: database studenti

**Nota:** Questo esercizio deve essere svolto utilizzando Python e il modulo `sqlite3` per interagire con il database SQLite. Consulta l'esempio di codice al seguente link per iniziare: [https://github.com/angelogalantiscuola/IT/blob/main/03_Sviluppo_Web_e_Database/01_Database/12_SQL_in_Python.md](https://github.com/angelogalantiscuola/IT/blob/main/03_Sviluppo_Web_e_Database/01_Database/12_SQL_in_Python.md)

- Crea un database SQLite chiamato "scuola.db".
- Crea due tabelle:
  - Studenti: Matricola (INTEGER PRIMARY KEY), Nome (TEXT NOT NULL), Cognome (TEXT NOT NULL).
  - Esami: Id (INTEGER PRIMARY KEY AUTOINCREMENT), Matricola (INTEGER NOT NULL), Corso (TEXT NOT NULL), Voto (INTEGER), con FOREIGN KEY su Studenti(Matricola).
- Inserisci i seguenti dati (tutti gli studenti devono avere gli stessi record di esami):
  - Studenti:
    - Matricola 101, Nome Mario, Cognome Rossi
    - Matricola 102, Nome Lucia, Cognome Bianchi
  - Esami (da inserire per ogni studente: per Matricola 101 e per Matricola 102):
    - Corso "Matematica", Voto 28
    - Corso "Informatica", Voto 30
    - Corso "Fisica", Voto 27
- Esegui tre query semplici:
  1. Elenco di tutti gli studenti (Matricola, Nome, Cognome).
  2. Elenco dei corsi e voti sostenuti da uno studente specifico (usa la matricola 101 come esempio).
  3. Numero di esami sostenuti per ciascuno studente (GROUP BY Matricola).

Suggerimento: usa INSERT OR IGNORE per evitare errori su violazioni di vincoli (es. PRIMARY KEY)