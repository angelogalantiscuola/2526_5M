# Esercizio 5: Database libreria in Python

**Nota:** Questo esercizio deve essere svolto utilizzando Python e il modulo `sqlite3` per interagire con il database SQLite. Crea un database chiamato "libreria.db" con le seguenti tabelle:

- **Autori**: id (INTEGER PRIMARY KEY), nome (TEXT NOT NULL), cognome (TEXT NOT NULL)
- **Libri**: id (INTEGER PRIMARY KEY), titolo (TEXT NOT NULL), autore_id (INTEGER, FOREIGN KEY REFERENCES Autori(id)), anno (INTEGER), genere (TEXT)
- **Prestiti**: id (INTEGER PRIMARY KEY), libro_id (INTEGER, FOREIGN KEY REFERENCES Libri(id)), utente (TEXT NOT NULL), data_prestito (TEXT), data_restituzione (TEXT)

Implementa le seguenti funzioni:

1. `create_tables()`: Crea le tabelle se non esistono.
2. `insert_data()`: Inserisci i seguenti dati di esempio:
   - **Autori**:
     - id: 1, nome: 'Mario', cognome: 'Rossi'
     - id: 2, nome: 'Lucia', cognome: 'Bianchi'
     - id: 3, nome: 'Alessandro', cognome: 'Verdi'
   - **Libri**:
     - id: 1, titolo: 'Il mistero del castello', autore_id: 1, anno: 2020, genere: 'Giallo'
     - id: 2, titolo: 'Viaggio nel tempo', autore_id: 1, anno: 2018, genere: 'Fantascienza'
     - id: 3, titolo: 'La cucina italiana', autore_id: 2, anno: 2019, genere: 'Cucina'
     - id: 4, titolo: 'Storia antica', autore_id: 3, anno: 2021, genere: 'Storia'
     - id: 5, titolo: 'Romanzo moderno', autore_id: 3, anno: 2022, genere: 'Narrativa'
     - id: 6, titolo: 'Il ritorno del castello', autore_id: 1, anno: 2023, genere: 'Giallo'
   - **Prestiti**:
     - id: 1, libro_id: 1, utente: 'Mario Rossi', data_prestito: '2023-01-01', data_restituzione: '2023-01-15'
     - id: 2, libro_id: 2, utente: 'Lucia Bianchi', data_prestito: '2023-02-01', data_restituzione: NULL
     - id: 3, libro_id: 3, utente: 'Alessandro Verdi', data_prestito: '2023-03-01', data_restituzione: '2023-03-10'
     - id: 4, libro_id: 4, utente: 'Mario Rossi', data_prestito: '2023-04-01', data_restituzione: NULL
3. `query_libri_per_autore(autore_id)`: Restituisce tutti i libri di un autore specifico (usa JOIN).
4. `query_prestiti_per_utente(utente)`: Restituisce i prestiti di un utente (usa JOIN).
5. `query_libri_per_genere()`: Restituisce il numero di libri per genere (usa GROUP BY). Assicurati di avere almeno un genere con due libri nell'esempio (per esempio "Giallo" con 2 libri) in modo che la query mostri valori maggiori di 1.
6. `query_autori_con_piu_libri()`: Restituisce gli autori ordinati per numero di libri (usa JOIN, GROUP BY, ORDER BY).
7. `query_prestiti_non_restituiti()`: Restituisce i prestiti non ancora restituiti (data_restituzione IS NULL).

Nel codice principale, chiama le funzioni e stampa i risultati delle query.

Consulta l'esempio precedente per la struttura del codice Python.