-- Schema for beekeeping database
CREATE TABLE Typology (
    id INT PRIMARY KEY,
    typology_name VARCHAR(50) NOT NULL,
    typology_description VARCHAR(300)
);

CREATE TABLE Honey (
    id INT PRIMARY KEY,
    denomination VARCHAR(50) NOT NULL,
    typology_id INT,
    FOREIGN KEY (typology_id) REFERENCES Typology(id)
);

CREATE TABLE Beekeeper (
    id INT PRIMARY KEY,
    beekeeper_name VARCHAR(50) NOT NULL
);

CREATE TABLE Apiary (
    code INT PRIMARY KEY,
    num_hives INT NOT NULL,
    locality VARCHAR(300) NOT NULL,
    comune VARCHAR(300) NOT NULL,
    province VARCHAR(300) NOT NULL,
    region VARCHAR(300) NOT NULL,
    beekeeper_id INT,
    FOREIGN KEY (beekeeper_id) REFERENCES Beekeeper(id)
);

CREATE TABLE Production (
    id INT PRIMARY KEY,
    year INT,
    quantity FLOAT,
    apiary_code INT,
    honey_id INT,
    FOREIGN KEY (apiary_code) REFERENCES Apiary(code),
    FOREIGN KEY (honey_id) REFERENCES Honey(id)
);

-- Insert sample data
INSERT INTO Typology (id, typology_name, typology_description) VALUES
(1, 'Monofloral', 'Miele prodotto prevalentemente da un unico fiore'),
(2, 'Polyfloral', 'Miele di millefiori, raccolto da più specie floreali'),
(3, 'Honeydew', 'Miele prodotto a partire dal melato (secrezioni di insetti)');

INSERT INTO Beekeeper (id, beekeeper_name) VALUES
(1, 'Marco Rossi'),
(2, 'Lucia Bianchi'),
(3, 'Alessandro Verdi');

INSERT INTO Honey (id, denomination, typology_id) VALUES
(1, 'Acacia', 1),
(2, 'Castagno', 1),
(3, 'Millefiori', 2),
(4, 'Eucalipto', 2),
(5, 'Melata di Bosco', 3);

INSERT INTO Apiary (code, num_hives, locality, comune, province, region, beekeeper_id) VALUES
(100, 12, 'Fattoria Le Rose', 'San Pietro', 'Pisa', 'Toscana', 1),
(101, 8, 'Colle Verde', 'Montevarchi', 'Arezzo', 'Toscana', 2),
(102, 20, 'Bosco Alto', 'Vercelli', 'Vercelli', 'Piemonte', 3),
(103, 5, 'Terrazza Sud', 'Verona', 'Verona', 'Veneto', 1);

INSERT INTO Production (id, year, quantity, apiary_code, honey_id) VALUES
(1, 2022, 120.5, 100, 1),
(2, 2022, 95.2, 101, 3),
(3, 2023, 210.0, 102, 5),
(4, 2023, 34.7, 103, 2),
(5, 2024, 150.0, 100, 3),
(6, 2024, 78.3, 101, 4);

-- Queries

-- 1) Seleziona tutti gli apicoltori.
SELECT *
FROM Beekeeper;

-- 2) Seleziona il nome dell'apicoltore con id = 1.
SELECT beekeeper_name
FROM Beekeeper
WHERE id = 1;

-- 3) Seleziona tutti gli apiari nella regione 'Lombardia'.
SELECT *
FROM Apiary
WHERE region = 'Lombardia';

-- 4) Seleziona codice e numero_arnie degli apiari con più di 10 arnie.
SELECT code, num_hives
FROM Apiary
WHERE num_hives > 10;

-- 5) Seleziona codice e località degli apiari posseduti dall'apicoltore con id = 2.
SELECT code, locality
FROM Apiary
WHERE beekeeper_id = 2;

-- 6) Seleziona tutti i mieli appartenenti alla tipologia con id = 3.
SELECT *
FROM Honey
WHERE typology_id = 3;

-- 7) Seleziona la denominazione del miele con id = 5.
SELECT denomination
FROM Honey
WHERE id = 5;

-- 8) Seleziona tutte le produzioni dell'anno 2024.
SELECT *
FROM Production
WHERE year = 2024;

-- 9) Seleziona tutte le produzioni per l'apiario con codice = 102.
SELECT *
FROM Production
WHERE apiary_code = 102;

-- 10) Seleziona le produzioni per il miele con id = 3 nell'anno 2023.
SELECT *
FROM Production
WHERE honey_id = 3
AND year = 2023;