from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import categoria_repository, piatto_repository

bp = Blueprint("main", __name__)


# ===== ESERCIZIO 1: CRUD =====


@bp.route("/")
def index():
    """Pagina principale: lista categorie."""
    categories = categoria_repository.get_all_categories()
    return render_template("index.html", categories=categories)


@bp.route("/categoria/<int:id>")
def categoria_detail(id):
    """Dettaglio categoria con lista piatti."""
    category = categoria_repository.get_category_by_id(id)
    if category is None:
        abort(404, "Categoria non trovata.")

    piatti = piatto_repository.get_piatti_by_category(id)
    return render_template("categoria_detail.html", category=category, piatti=piatti)


@bp.route("/crea_categoria", methods=("GET", "POST"))
def crea_categoria():
    """Crea una nuova categoria."""
    if request.method == "POST":
        nome = request.form["nome"]
        error = None

        if not nome:
            error = "Il nome della categoria è obbligatorio."

        if error is not None:
            flash(error)
        else:
            categoria_repository.create_category(nome)
            return redirect(url_for("main.index"))

    return render_template("crea_categoria.html")


@bp.route("/crea_piatto", methods=("GET", "POST"))
def crea_piatto():
    """Crea un nuovo piatto."""
    categories = categoria_repository.get_all_categories()

    if request.method == "POST":
        categoria_id = request.form.get("categoria_id", type=int)
        nome = request.form["nome"]
        prezzo = request.form.get("prezzo", type=float)
        error = None

        if categoria_id is None:
            error = "Seleziona una categoria."
        if not nome:
            error = "Il nome del piatto è obbligatorio."
        if prezzo is None or prezzo < 0:
            error = "Il prezzo deve essere un numero positivo."

        if error is not None:
            flash(error)
        else:
            piatto_repository.create_piatto(categoria_id, nome, prezzo)
            return redirect(url_for("main.index"))

    return render_template("crea_piatto.html", categories=categories)


# ===== ESERCIZIO 2: RICERCA =====


@bp.route("/ricerca", methods=("GET", "POST"))
def ricerca():
    """Ricerca piatti per nome."""
    search_term = None
    piatti = []

    if request.method == "POST":
        search_term = request.form.get("search_term", "").strip()

        if search_term:
            piatti = piatto_repository.find_piatti_by_name(search_term)

    return render_template("ricerca.html", search_term=search_term, piatti=piatti)
