-- 1. Elenco di tutti i libri con titolo, anno e nome dell'autore (usa JOIN)
SELECT Libri.titolo, Libri.anno, Autori.nome, Autori.cognome
FROM Libri
JOIN Autori ON Libri.autore_id = Autori.id
ORDER BY Libri.anno;

-- 2. Elenco di tutti i prestiti con titolo del libro, utente e data di prestito (usa JOIN)
SELECT Libri.titolo, Prestiti.utente, Prestiti.data_prestito
FROM Prestiti
JOIN Libri ON Prestiti.libro_id = Libri.id
ORDER BY Prestiti.data_prestito;

-- 3. Libri pubblicati dopo il 2020
SELECT titolo, anno, genere
FROM Libri
WHERE anno > 2020
ORDER BY anno;

-- 4. Numero di prestiti per ciascun utente (usa GROUP BY)
SELECT utente, COUNT(*) AS num_prestiti
FROM Prestiti
GROUP BY utente
ORDER BY num_prestiti DESC;

-- 5. Libri ordinati per genere e poi per anno (usa ORDER BY multiplo)
SELECT genere, titolo, anno
FROM Libri
ORDER BY genere, anno;

-- 6. Prestiti restituiti (dove data_restituzione non è NULL)
SELECT Libri.titolo, Prestiti.utente, Prestiti.data_prestito, Prestiti.data_restituzione
FROM Prestiti
JOIN Libri ON Prestiti.libro_id = Libri.id
WHERE Prestiti.data_restituzione IS NOT NULL
ORDER BY Prestiti.data_restituzione;

-- 7. Autori e numero di libri, inclusi quelli senza libri (usa LEFT JOIN e GROUP BY)
SELECT Autori.nome, Autori.cognome, COUNT(Libri.id) AS num_libri
FROM Autori
LEFT JOIN Libri ON Autori.id = Libri.autore_id
GROUP BY Autori.id
ORDER BY num_libri DESC;
