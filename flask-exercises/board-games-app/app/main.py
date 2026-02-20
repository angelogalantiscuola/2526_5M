from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import game_repository, match_repository

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    # 1. Prendiamo i giochi dal database
    games = game_repository.get_all_games()

    # 2. Passiamo la variabile 'games' al template
    return render_template("index.html", games=games)


@bp.route("/game/<int:id>")
def game_detail(id):
    # 1. Prendiamo il gioco
    game = game_repository.get_game_by_id(id)
    if game is None:
        abort(404, "Gioco non trovato.")

    # 2. Prendiamo le partite del gioco
    matches = match_repository.get_matches_by_game(id)

    # 3. Passiamo al template
    return render_template("game_detail.html", game=game, matches=matches)


@bp.route("/create_game", methods=("GET", "POST"))
def create_game():
    if request.method == "POST":
        nome = request.form["nome"]
        numero_giocatori_massimo = request.form.get("numero_giocatori_massimo", type=int)
        durata_media = request.form.get("durata_media", type=int)
        categoria = request.form["categoria"]
        error = None

        if not nome:
            error = "Il nome è obbligatorio."
        if numero_giocatori_massimo is None or numero_giocatori_massimo <= 0:
            error = "Il numero di giocatori massimo deve essere un numero positivo."
        if durata_media is None or durata_media <= 0:
            error = "La durata media deve essere un numero positivo."
        if not categoria:
            error = "La categoria è obbligatoria."

        if error is not None:
            flash(error)
        else:
            # Creiamo il gioco
            game_repository.create_game(nome, numero_giocatori_massimo, durata_media, categoria)
            return redirect(url_for("main.index"))

    return render_template("create_game.html")


@bp.route("/create_match", methods=("GET", "POST"))
def create_match():
    if request.method == "POST":
        gioco_id = request.form.get("gioco_id", type=int)
        data = request.form["data"]
        vincitore = request.form["vincitore"]
        punteggio_vincitore = request.form.get("punteggio_vincitore", type=int)
        error = None

        if gioco_id is None:
            error = "Seleziona un gioco."
        if not data:
            error = "La data è obbligatoria."
        if not vincitore:
            error = "Il vincitore è obbligatorio."
        if punteggio_vincitore is None or punteggio_vincitore < 0:
            error = "Il punteggio vincitore deve essere un numero non negativo."

        if error is not None:
            flash(error)
        else:
            # Creiamo la partita
            match_repository.create_match(gioco_id, data, vincitore, punteggio_vincitore)
            return redirect(url_for("main.game_detail", id=gioco_id))

    # Per GET, passiamo i giochi per il select
    games = game_repository.get_all_games()
    return render_template("create_match.html", games=games)