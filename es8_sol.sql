-- database: :memory:
-- Creazione tabelle

CREATE TABLE Negozi (
    codice INTEGER PRIMARY KEY,
    indirizzo TEXT NOT NULL,
    citta TEXT NOT NULL
);

CREATE TABLE Dipendenti (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    negozio_id INTEGER,
    FOREIGN KEY (negozio_id) REFERENCES Negozi(codice)
);

CREATE TABLE Artisti (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL
);

CREATE TABLE AlbumVirtuale (
    codice INTEGER PRIMARY KEY,
    titolo TEXT NOT NULL,
    prezzo REAL NOT NULL,
    prezzo_unitario REAL NOT NULL,
    artista_id INTEGER,
    FOREIGN KEY (artista_id) REFERENCES Artisti(id)
);

CREATE TABLE Scontrino (
    id INTEGER PRIMARY KEY,
    data DATE NOT NULL,
    negozio_id INTEGER,
    importo_totale REAL NOT NULL,
    FOREIGN KEY (negozio_id) REFERENCES Negozi(codice)
);

CREATE TABLE RigheScontrino (
    id INTEGER PRIMARY KEY,
    scontrino_id INTEGER,
    album_id INTEGER,
    quantita INTEGER NOT NULL,
    FOREIGN KEY (scontrino_id) REFERENCES Scontrino(id),
    FOREIGN KEY (album_id) REFERENCES AlbumVirtuale(codice)
);

-- Inserimento dati

-- Negozi
INSERT INTO Negozi (codice, indirizzo, citta) VALUES 
(1, 'Via Roma 10', 'Milano'),
(2, 'Corso Italia 25', 'Roma'),
(3, 'Via Garibaldi 5', 'Torino'),
(4, 'Piazza Duomo 3', 'Firenze'),
(5, 'Viale Europa 18', 'Napoli');

-- Dipendenti
INSERT INTO Dipendenti (id, nome, cognome, negozio_id) VALUES 
(1, 'Mario', 'Rossi', 1),
(2, 'Giulia', 'Bianchi', 1),
(3, 'Luca', 'Verdi', 2),
(4, 'Anna', 'Neri', 3),
(5, 'Paolo', 'Gialli', 4),
(6, 'Laura', 'Blu', 1),
(7, 'Marco', 'Viola', 2),
(8, 'Sara', 'Marroni', 5);

-- Artisti
INSERT INTO Artisti (id, nome, cognome) VALUES 
(1, 'Lucio', 'Battisti'),
(2, 'Fabrizio', 'De André'),
(3, 'Vasco', 'Rossi'),
(4, 'Luciano', 'Ligabue'),
(5, 'Eros', 'Ramazzotti');

-- AlbumVirtuale (più album per artista)
INSERT INTO AlbumVirtuale (codice, titolo, prezzo, prezzo_unitario, artista_id) VALUES 
(1, 'Emozioni', 15.99, 15.99, 1),
(2, 'Anima latina', 14.50, 14.50, 1),
(3, 'Il mio canto libero', 16.99, 16.99, 1),
(4, 'Creuza de mä', 18.50, 18.50, 2),
(5, 'Fabrizio De André', 17.99, 17.99, 2),
(6, 'Albachiara', 14.99, 14.99, 3),
(7, 'Bollicine', 13.99, 13.99, 3),
(8, 'Colpa d''Alfredo', 15.50, 15.50, 3),
(9, 'Vivere', 16.99, 16.99, 3),
(10, 'Buon compleanno Elvis', 16.99, 16.99, 4),
(11, 'Lambrusco coltelli rose e pop corn', 14.99, 14.99, 4),
(12, 'Tutte storie', 17.50, 17.50, 5),
(13, 'Dove c''è musica', 15.99, 15.99, 5);

-- Scontrino
INSERT INTO Scontrino (id, data, negozio_id, importo_totale) VALUES 
(1, '2025-10-15', 1, 46.48),
(2, '2025-10-16', 2, 18.50),
(3, '2025-10-17', 1, 44.97),
(4, '2025-10-18', 3, 50.97),
(5, '2025-10-19', 4, 35.00),
(6, '2025-10-20', 1, 62.94),
(7, '2025-10-21', 2, 31.98),
(8, '2025-10-22', 1, 33.98),
(9, '2025-10-23', 5, 27.98),
(10, '2025-10-24', 3, 45.48);

-- RigheScontrino (più righe per scontrino)
INSERT INTO RigheScontrino (id, scontrino_id, album_id, quantita) VALUES 
(1, 1, 1, 1),
(2, 1, 2, 1),
(3, 1, 3, 1),
(4, 2, 4, 1),
(5, 3, 6, 3),
(6, 4, 10, 3),
(7, 5, 12, 2),
(8, 6, 7, 2),
(9, 6, 8, 2),
(10, 7, 11, 2),
(11, 8, 5, 1),
(12, 8, 3, 1),
(13, 9, 13, 1),
(14, 9, 12, 1),
(15, 10, 1, 1),
(16, 10, 9, 2);

-- QUERY 1: Selezione semplice
-- Recuperare tutti gli album di Vasco Rossi ordinati per prezzo
SELECT AV.titolo, AV.prezzo
FROM AlbumVirtuale AV
JOIN Artisti A ON AV.artista_id = A.id
WHERE A.nome = 'Vasco' AND A.cognome = 'Rossi'
ORDER BY AV.prezzo;

-- QUERY 2: Join semplice
-- Elencare tutti gli album con il nome e cognome dell'artista
SELECT AV.titolo, A.nome, A.cognome
FROM AlbumVirtuale AV
JOIN Artisti A ON AV.artista_id = A.id;

-- QUERY 3: Aggregazione con GROUP BY
-- Contare il numero di album per ogni artista e il prezzo medio
SELECT A.nome, A.cognome, COUNT(RS.id) AS numero_album, AVG(AV.prezzo) AS prezzo_medio
FROM AlbumVirtuale AV
JOIN Artisti A ON AV.artista_id = A.id
JOIN RigheScontrino RS ON AV.codice = RS.album_id
GROUP BY A.id;

-- QUERY 4: Query annidata (subquery)
-- Trovare tutti gli album il cui prezzo è superiore alla media dei prezzi degli album di tutti gli artisti
SELECT AV.titolo, AV.prezzo
FROM AlbumVirtuale AV
JOIN Artisti A ON AV.artista_id = A.id
WHERE AV.prezzo > (SELECT AVG(prezzo) FROM AlbumVirtuale);

-- QUERY 5: Join con aggregazione
-- Calcolare il totale delle vendite per ogni artista
SELECT A.nome, A.cognome, SUM(RS.quantita * AV.prezzo_unitario) AS totale_vendite
FROM RigheScontrino RS
JOIN AlbumVirtuale AV ON RS.album_id = AV.codice
JOIN Artisti A ON AV.artista_id = A.id
GROUP BY A.id;

-- QUERY 6: Query con wildcards (LIKE)
-- Trovare album con 'a' nel titolo
SELECT *
FROM AlbumVirtuale
WHERE titolo LIKE '%a%';

-- QUERY 7: LEFT JOIN con aggregazione
-- Elencare tutti gli artisti e il numero di album venduti (incluso 0 se non hanno vendite)
SELECT A.nome, A.cognome, COUNT(RS.id) AS numero_album_venduti
FROM Artisti A
LEFT JOIN AlbumVirtuale AV ON A.id = AV.artista_id
LEFT JOIN RigheScontrino RS ON AV.codice = RS.album_id 
GROUP BY A.id;
