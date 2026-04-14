import os
from flask import Flask
from app.db import init_db


def create_app(test_config=None):
    """Application factory."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "ristorante.db"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # Crea cartella instance se non esiste
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Registra il comando init-db
    @app.cli.command()
    def init_db_command():
        init_db()
        print("Database inizializzato.")

    # Registra la funzione di chiusura DB
    from app.db import close_db

    app.teardown_appcontext(close_db)

    # Registra il blueprint main
    from app import main

    app.register_blueprint(main.bp)

    return app
