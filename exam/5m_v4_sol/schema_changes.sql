-- FILE: app/schema.sql
-- Aggiungi questa tabella al file esistente

CREATE TABLE comment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  post_id INTEGER NOT NULL,
  author_id INTEGER NOT NULL,
  body TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (post_id) REFERENCES post (id),
  FOREIGN KEY (author_id) REFERENCES user (id)
);
