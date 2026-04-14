-- Creazione tabelle

CREATE TABLE Prodotto (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    prezzo REAL NOT NULL
);

CREATE TABLE Ordine (
    id INTEGER PRIMARY KEY,
    data DATE NOT NULL,
    cliente_nome TEXT NOT NULL
);

CREATE TABLE OrdineProdotto (
    id INTEGER PRIMARY KEY,
    ordine_id INTEGER NOT NULL,
    prodotto_id INTEGER NOT NULL,
    quantita INTEGER NOT NULL,
    FOREIGN KEY (ordine_id) REFERENCES Ordine(id),
    FOREIGN KEY (prodotto_id) REFERENCES Prodotto(id)
);

-- Inserimento dati

INSERT INTO Prodotto (id, nome, prezzo) VALUES
(1, 'Notebook', 12.5),
(2, 'Penna a sfera', 1.2),
(3, 'Zaino', 28.0),
(4, 'Agenda', 7.5),
(5, 'Quaderno', 5.0);

INSERT INTO Ordine (id, data, cliente_nome) VALUES
(1, '2025-10-01', 'Anna Verdi'),
(2, '2025-10-02', 'Marco Neri'),
(3, '2025-10-03', 'Anna Verdi');

INSERT INTO OrdineProdotto (id, ordine_id, prodotto_id, quantita) VALUES
(1, 1, 1, 2),
(2, 1, 2, 5),
(3, 2, 3, 1),
(4, 3, 4, 2),
(5, 3, 2, 3);

-- Query di esempio (5 query semplici)

-- 1. Elenco dei prodotti che costano meno di 10
SELECT id, nome, prezzo
FROM Prodotto
WHERE prezzo < 10;

-- 2. Elenco dei prodotti ordinati in un determinato ordine (id ordine = 1)
SELECT p.nome, op.quantita
FROM OrdineProdotto op
JOIN Prodotto p ON p.id = op.prodotto_id
WHERE op.ordine_id = 1;

-- 3. Numero di ordini per ogni cliente
SELECT cliente_nome, COUNT(*) AS numero_ordini
FROM Ordine
GROUP BY cliente_nome;

-- 4. Media dei prezzi dei prodotti
SELECT AVG(prezzo) AS media_prezzi
FROM Prodotto;

-- 5. Totale speso per ogni cliente
SELECT o.cliente_nome, SUM(p.prezzo * op.quantita) AS totale_speso
FROM Ordine o
JOIN OrdineProdotto op ON op.ordine_id = o.id
JOIN Prodotto p ON p.id = op.prodotto_id
GROUP BY o.cliente_nome;
