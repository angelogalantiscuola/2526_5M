# App Flask per Giochi da Tavolo e Partite

Implementa un'applicazione Flask per gestire Giochi da Tavolo e le loro Partite.

## Descrizione delle Entità

- **Giochi**: nome, numero_giocatori_massimo, durata_media (in minuti), categoria
- **Partite**: data, vincitore (nome del giocatore), punteggio_vincitore

Relazione: Un gioco può avere più partite, ogni partita appartiene a un gioco specifico.

## Funzionalità Richieste

L'app deve permettere di:

1. Creare nuovi giochi da tavolo
2. Registrare partite per un gioco esistente
3. Visualizzare la lista dei giochi
4. Visualizzare la lista delle partite di un gioco

Non è richiesta la modifica o la cancellazione dei contenuti.

## Schema del Database

```sql
DROP TABLE IF EXISTS partite;
DROP TABLE IF EXISTS giochi;

CREATE TABLE giochi (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  numero_giocatori_massimo INTEGER NOT NULL,
  durata_media INTEGER NOT NULL, -- durata in minuti
  categoria TEXT NOT NULL
);

CREATE TABLE partite (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  gioco_id INTEGER NOT NULL,
  data DATE NOT NULL,
  vincitore TEXT NOT NULL,
  punteggio_vincitore INTEGER NOT NULL,
  FOREIGN KEY (gioco_id) REFERENCES giochi (id)
);

-- Insert di esempio per i Giochi
INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES ('Catan', 4, 90, 'Strategia');
INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES ('Dixit', 6, 30, 'Party');
INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES ('Ticket to Ride', 5, 60, 'Strategia');

-- Insert di esempio per le Partite
INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (1, '2023-10-15', 'Alice', 10);
INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (1, '2023-10-22', 'Bob', 12);
INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (2, '2023-11-05', 'Charlie', 25);
INSERT INTO partite (gioco_id, data, vincitore, punteggio_vincitore) VALUES (3, '2023-11-10', 'Alice', 8);
```