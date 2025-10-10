# Esercizio 6: Query aggiuntive sul database libreria

Usando il database "libreria.db" creato nell'esercizio 5 (tabelle Autori, Libri, Prestiti), scrivi le seguenti query SQL. Per ciascuna query, fornisci il risultato atteso (basato sui dati di esempio dell'esercizio 5).

1. Elenco di tutti i libri con titolo, anno e nome dell'autore (usa JOIN).
   **Risultato:**
   - Viaggio nel tempo, 2018, Mario, Rossi
   - La cucina italiana, 2019, Lucia, Bianchi
   - Il mistero del castello, 2020, Mario, Rossi
   - Storia antica, 2021, Alessandro, Verdi
   - Romanzo moderno, 2022, Alessandro, Verdi
   - Il ritorno del castello, 2023, Mario, Rossi

2. Elenco di tutti i prestiti con titolo del libro, utente e data di prestito (usa JOIN).
   **Risultato:**
   - Il mistero del castello, Mario Rossi, 2023-01-01
   - Viaggio nel tempo, Lucia Bianchi, 2023-02-01
   - La cucina italiana, Alessandro Verdi, 2023-03-01
   - Storia antica, Mario Rossi, 2023-04-01

3. Libri pubblicati dopo il 2020.
   **Risultato:**
   - Storia antica, 2021, Storia
   - Romanzo moderno, 2022, Narrativa
   - Il ritorno del castello, 2023, Giallo

4. Numero di prestiti per ciascun utente (usa GROUP BY).
   **Risultato:**
   - Mario Rossi, 2
   - Lucia Bianchi, 1
   - Alessandro Verdi, 1

5. Libri ordinati per genere e poi per anno (usa ORDER BY multiplo).
   **Risultato:**
   - Cucina, La cucina italiana, 2019
   - Fantascienza, Viaggio nel tempo, 2018
   - Giallo, Il mistero del castello, 2020
   - Giallo, Il ritorno del castello, 2023
   - Narrativa, Romanzo moderno, 2022
   - Storia, Storia antica, 2021

6. Prestiti restituiti (dove data_restituzione non è NULL).
   **Risultato:**
   - Il mistero del castello, Mario Rossi, 2023-01-01, 2023-01-15
   - La cucina italiana, Alessandro Verdi, 2023-03-01, 2023-03-10

7. Autori e numero di libri, inclusi quelli senza libri (usa [LEFT JOIN](https://www.w3schools.com/sql/sql_join_left.asp) e GROUP BY).
   **Risultato:**
   - Mario, Rossi, 3
   - Alessandro, Verdi, 2
   - Lucia, Bianchi, 1
