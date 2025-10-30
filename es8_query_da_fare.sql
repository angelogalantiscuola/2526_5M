-- Query di complessità crescente per il database Music Store


-- Use the ▷ button in the top right corner to run the entire file.
-- QUERY 1: Selezione semplice
-- Recuperare tutti gli album di Vasco Rossi ordinati per prezzo
SELECT AV.titolo, AV.prezzo, A.nome, A.cognome
FROM AlbumVirtuale AV
JOIN Artisti A
ON A.id = AV.artista_id
WHERE A.nome = "Vasco" AND A.cognome = "Rossi";

-- QUERY 2: Join semplice
-- Elencare tutti gli album con il nome e cognome dell'artista
SELECT AV.titolo, A.nome, A.cognome
FROM AlbumVirtuale AV
JOIN Artisti A
ON A.id = AV.artista_id;

-- QUERY 3: Aggregazione con GROUP BY
-- Contare il numero di album per ogni artista e il prezzo medio
SELECT A.nome, A.cognome, COUNT(A.id) AS numero_album, AVG(AV.prezzo) AS prezzo_medio
FROM AlbumVirtuale AV
JOIN Artisti A
ON A.id = AV.artista_id
WHERE A.cognome = "Ramazzotti"
GROUP BY A.id, A.cognome
HAVING numero_album >= 2 AND prezzo_medio > 16;

-- QUERY 4: Query annidata (subquery)
-- Trovare tutti gli album il cui prezzo è superiore alla media dei prezzi degli album di tutti gli artisti

-- 1. media dei prezzi degli album di tutti gli artisti
SELECT AVG(AV.prezzo) AS prezzo_medio
FROM AlbumVirtuale AV;
-- 16.22

-- 2. Trovare tutti gli album il cui prezzo è superiore a 16.22
SELECT AV.titolo, AV.prezzo
FROM AlbumVirtuale AV
WHERE AV.prezzo > 16.22;

-- Trovare tutti gli album il cui prezzo è superiore alla media dei prezzi degli album di tutti gli artisti
SELECT AV.titolo, AV.prezzo
FROM AlbumVirtuale AV
WHERE AV.prezzo > 
    (SELECT AVG(AV.prezzo) AS prezzo_medio
    FROM AlbumVirtuale AV);


-- QUERY 5: Join con aggregazione
-- Calcolare il totale delle vendite per ogni artista


-- QUERY 6: Query con wildcards (LIKE)
-- Trovare album con 'a' nel titolo


-- QUERY 7: LEFT JOIN con aggregazione
-- Elencare tutti gli artisti e il numero di album venduti (incluso 0 se non hanno vendite)

