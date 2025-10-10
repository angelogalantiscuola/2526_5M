CREATE TABLE Studenti (
            Matricola INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Cognome TEXT NOT NULL
        );
CREATE TABLE Esami (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Matricola INTEGER NOT NULL,
            Corso TEXT NOT NULL,
            Voto INTEGER,
            FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
        );
CREATE TABLE sqlite_sequence(name,seq);
