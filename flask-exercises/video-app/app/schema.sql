DROP TABLE IF EXISTS video;
DROP TABLE IF EXISTS canali;
DROP TABLE IF EXISTS categoria;

CREATE TABLE categoria (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL UNIQUE
);

CREATE TABLE canali (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  numero_iscritti INTEGER DEFAULT 0,
  categoria_id INTEGER NOT NULL,
  FOREIGN KEY (categoria_id) REFERENCES categoria (id)
);

CREATE TABLE video (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  canale_id INTEGER NOT NULL,
  titolo TEXT NOT NULL,
  durata INTEGER NOT NULL, -- durata in secondi
  immagine TEXT, -- URL o nome file dell'anteprima
  FOREIGN KEY (canale_id) REFERENCES canali (id)
);

-- Insert di esempio per le Categorie
INSERT INTO categoria (nome) VALUES ('Tecnologia');
INSERT INTO categoria (nome) VALUES ('Cucina');
INSERT INTO categoria (nome) VALUES ('Gaming');
INSERT INTO categoria (nome) VALUES ('Musica');

-- Insert di esempio per i Canali
INSERT INTO canali (nome, numero_iscritti, categoria_id) VALUES ('Tech Guru', 1500, 1);
INSERT INTO canali (nome, numero_iscritti, categoria_id) VALUES ('Chef Stellato', 85000, 2);
INSERT INTO canali (nome, numero_iscritti, categoria_id) VALUES ('Gaming Zone', 1200, 3);

-- Insert di esempio per i Video
INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (1, 'Recensione iPhone 15', 600, 'iphone.jpg');
INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (1, 'Come programmare in Python', 1200, 'python.jpg');
INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (2, 'Pasta alla Carbonara perfetta', 450, 'carbonara.jpg');
INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (3, 'Gameplay Minecraft Parte 1', 1800, 'minecraft.jpg');