-- Soluzioni esercizio 3: Query con GROUP BY e funzioni aggregate

-- 1. Seleziona la quantità totale prodotta per anno.
SELECT year, SUM(quantity) AS totale_annuo
FROM Production
GROUP BY year;

-- 2. Seleziona la produzione media per apiario.
SELECT apiary_code, AVG(quantity) AS media_produzione
FROM Production
GROUP BY apiary_code;

-- 3. Seleziona il numero di produzioni e la produzione totale per miele.
SELECT honey_id, COUNT(*) AS num_produzioni, SUM(quantity) AS totale_produzione
FROM Production
GROUP BY honey_id;

-- 4. Seleziona la produzione totale per miele nell'anno 2024.
SELECT honey_id, SUM(quantity) AS totale_2024
FROM Production
WHERE year = 2024
GROUP BY honey_id;

-- 5. Seleziona il valore massimo e minimo di produzione per anno.
SELECT year, MAX(quantity) AS max_produzione, MIN(quantity) AS min_produzione
FROM Production
GROUP BY year;

-- 6. Seleziona gli apiari la cui produzione totale supera 200.
SELECT apiary_code, SUM(quantity) AS totale
FROM Production
GROUP BY apiary_code
HAVING SUM(quantity) > 200;

-- 7. Seleziona la produzione totale per tipologia di miele (typology_id).
SELECT h.typology_id, SUM(p.quantity) AS totale
FROM Production p
JOIN Honey h ON p.honey_id = h.id
GROUP BY h.typology_id;

-- 8. Seleziona il numero di mieli per ciascuna tipologia.
SELECT typology_id, COUNT(*) AS num_mieli
FROM Honey
GROUP BY typology_id;

-- 9. Seleziona la produzione totale per apicoltore (beekeeper_id).
SELECT a.beekeeper_id, SUM(p.quantity) AS totale
FROM Production p
JOIN Apiary a ON p.apiary_code = a.code
GROUP BY a.beekeeper_id;

-- 10. Seleziona la produzione media per arnia (produzione totale divisa per num_hives) per apiario.
SELECT a.code, SUM(p.quantity)/a.num_hives AS media_per_arnia
FROM Production p
JOIN Apiary a ON p.apiary_code = a.code
GROUP BY a.code, a.num_hives;

-- 11. Seleziona per ogni anno il conteggio delle produzioni con quantità maggiore di 100.
SELECT year, COUNT(*) AS produzioni_over_100
FROM Production
WHERE quantity > 100
GROUP BY year;

-- 12. Seleziona per ogni miele e anno la somma delle quantità.
SELECT honey_id, year, SUM(quantity) AS totale
FROM Production
GROUP BY honey_id, year;
