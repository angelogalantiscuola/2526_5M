
La catena di negozi di musica "Melodia" vende dischi, CD e vinili di artisti italiani e internazionali. L'azienda è organizzata con una sede centrale e molteplici negozi distribuiti in varie città. Ogni negozio gestisce l'inventario e le vendite al dettaglio.

Ogni **negozio** è identificato da un codice numerico e dispone di un indirizzo e della città in cui si trova. Nei negozi `lavorano` più **dipendenti**: ogni dipendente è impiegato in un negozio specifico. Gli **artisti** `producono` **album** musicali, che sono identificati da un codice e hanno un titolo e un prezzo di vendita.

Le **vendite** vengono registrate giornalmente: per ogni vendita si conserva la data, il negozio che `ha effettuato` la vendita e l'importo totale. Per dettagliare i contenuti di una vendita si usano le righe di vendita che indicano, per ogni album venduto, la quantità e il prezzo unitario applicato.

```sql
-- Query di complessità crescente per il database Music Store


-- Use the ▷ button in the top right corner to run the entire file.
-- QUERY 1: Selezione semplice
-- Recuperare tutti gli album di Vasco Rossi ordinati per prezzo

-- QUERY 2: Join semplice
-- Elencare tutti gli album con il nome e cognome dell'artista

-- QUERY 3: Aggregazione con GROUP BY
-- Contare il numero di album per ogni artista e il prezzo medio

-- QUERY 4: Query annidata (subquery)
-- Trovare tutti gli album il cui prezzo è superiore alla media dei prezzi degli album di tutti gli artisti

-- QUERY 5: Join con aggregazione
-- Calcolare il totale delle vendite per ogni artista

-- QUERY 6: Query con wildcards (LIKE)
-- Trovare album con 'a' nel titolo

-- QUERY 7: LEFT JOIN con aggregazione
-- Elencare tutti gli artisti e il numero di album venduti (incluso 0 se non hanno vendite)
```