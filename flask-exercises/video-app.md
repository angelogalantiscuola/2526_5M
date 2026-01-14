# App Flask per Video e Canali

Implementa un'applicazione Flask simile a YouTube con Canali e Video.

## Descrizione delle Entità

- **Canali**: nome, numero_iscritti, categoria
- **Video**: titolo, durata (in secondi), immagine (URL o nome file)

Relazione: Un canale può avere più video, ogni video appartiene a un canale specifico.

## Funzionalità Richieste

L'app deve permettere di:

1. Creare nuovi canali
2. Inserire video in un canale
3. Visualizzare la lista dei canali
4. Visualizzare la lista dei video di un canale

Non è richiesta la modifica o la cancellazione dei contenuti.

## Schema del Database

```sql
DROP TABLE IF EXISTS video;
DROP TABLE IF EXISTS canali;

CREATE TABLE canali (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  numero_iscritti INTEGER DEFAULT 0,
  categoria TEXT NOT NULL
);

CREATE TABLE video (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  canale_id INTEGER NOT NULL,
  titolo TEXT NOT NULL,
  durata INTEGER NOT NULL, -- durata in secondi
  immagine TEXT, -- URL o nome file dell'anteprima
  FOREIGN KEY (canale_id) REFERENCES canali (id)
);

-- Insert di esempio per i Canali
INSERT INTO canali (nome, numero_iscritti, categoria) VALUES ('Tech Guru', 1500, 'Tecnologia');
INSERT INTO canali (nome, numero_iscritti, categoria) VALUES ('Chef Stellato', 85000, 'Cucina');
INSERT INTO canali (nome, numero_iscritti, categoria) VALUES ('Gaming Zone', 1200, 'Gaming');

-- Insert di esempio per i Video
INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (1, 'Recensione iPhone 15', 600, 'iphone.jpg');
INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (1, 'Come programmare in Python', 1200, 'python.jpg');
INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (2, 'Pasta alla Carbonara perfetta', 450, 'carbonara.jpg');
INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (3, 'Gameplay Minecraft Parte 1', 1800, 'minecraft.jpg');
```