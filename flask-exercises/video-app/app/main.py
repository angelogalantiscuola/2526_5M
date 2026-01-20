from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import channel_repository, video_repository

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint("main", __name__)


@bp.route("/")
def index():


    # 1. Prendiamo i canali dal database
    channels: list[dict] = channel_repository.get_all_channels()

    # 2. Passiamo la variabile 'channels' al template
    return render_template("index.html", channels=channels)

@bp.route("/channel/<int:id>")
def channel_detail(id):
    # 1. Prendiamo il canale
    channel = channel_repository.get_channel_by_id(id)
    if channel is None:
        abort(404, "Canale non trovato.")

    # 2. Prendiamo i video del canale
    videos = video_repository.get_videos_by_channel(id)

    # 3. Passiamo al template
    return render_template("channel_detail.html", channel=channel, videos=videos)


@bp.route("/url_crea", methods=("GET", "POST"))
def create_channel():
    if request.method == "POST":
        nome = request.form["nome"]
        numero_iscritti = request.form.get("numero_iscritti", 0, type=int)
        categoria = request.form["categoria"]
        error = None

        if not nome:
            error = "Il nome è obbligatorio."
        if not categoria:
            error = "La categoria è obbligatoria."

        if error is not None:
            flash(error)
        else:
            # Creiamo il canale
            channel_repository.create_channel(nome, numero_iscritti, categoria)
            return redirect(url_for("main.index"))

    return render_template("create_channel.html")


@bp.route("/create_video", methods=("GET", "POST"))
def create_video():
    if request.method == "POST":
        canale_id = request.form.get("canale_id", type=int)
        titolo = request.form["titolo"]
        durata = request.form.get("durata", type=int)
        immagine = request.form.get("immagine", "")
        error = None

        if not titolo:
            error = "Il titolo è obbligatorio."
        if durata is None or durata <= 0:
            error = "La durata deve essere un numero positivo."
        if canale_id is None:
            error = "Seleziona un canale."

        if error is not None:
            flash(error)
        else:
            # Creiamo il video
            video_repository.create_video(canale_id, titolo, durata, immagine)
            return redirect(url_for("main.channel_detail", id=canale_id))

    # Per GET, passiamo i canali per il select
    channels = channel_repository.get_all_channels()
    return render_template("create_video.html", channels=channels)
