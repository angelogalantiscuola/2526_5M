-- Aggiungi questa tabella a schema.sql

CREATE TABLE bookmark (
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, post_id),
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (post_id) REFERENCES post (id)
);

-- Nota: i post ora hanno date diverse per testare meglio il filtro per mese/anno:
-- - 2024-01-15 (Gennaio 2024)
-- - 2024-03-20 (Marzo 2024)
-- - 2024-11-10 (Novembre 2024)
-- - 2025-05-05 (Maggio 2025)
-- - 2026-01-27 (Gennaio 2026)
