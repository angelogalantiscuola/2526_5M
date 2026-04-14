DROP TABLE IF EXISTS piatti;
DROP TABLE IF EXISTS categorie;

CREATE TABLE categorie (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL
);

CREATE TABLE piatti (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  categoria_id INTEGER NOT NULL,
  nome TEXT NOT NULL,
  prezzo REAL NOT NULL,
  FOREIGN KEY (categoria_id) REFERENCES categorie (id)
);

-- Dati di esempio
INSERT INTO categorie (nome) VALUES ('Antipasti');
INSERT INTO categorie (nome) VALUES ('Primi');
INSERT INTO categorie (nome) VALUES ('Secondi');
INSERT INTO categorie (nome) VALUES ('Dolci');

INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (1, 'Bruschetta al Pomodoro', 5.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (1, 'Camarones al Ajillo', 8.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (2, 'Lasagne della Nonna', 12.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (2, 'Pappardelle al Cinghiale', 14.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (3, 'Branzino al Forno', 18.99);
INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (4, 'Tiramisu', 6.99);
