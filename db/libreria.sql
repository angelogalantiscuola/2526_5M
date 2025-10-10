CREATE TABLE Autori (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cognome TEXT NOT NULL
        );
CREATE TABLE Libri (
            id INTEGER PRIMARY KEY,
            titolo TEXT NOT NULL,
            autore_id INTEGER,
            anno INTEGER,
            genere TEXT,
            FOREIGN KEY (autore_id) REFERENCES Autori(id)
        );
CREATE TABLE Prestiti (
            id INTEGER PRIMARY KEY,
            libro_id INTEGER,
            utente TEXT NOT NULL,
            data_prestito TEXT,
            data_restituzione TEXT,
            FOREIGN KEY (libro_id) REFERENCES Libri(id)
        );
