# Aggiungi queste route a main.py
# Ricorda di importare: from app.repositories import bookmark_repository, user_repository

# --- ROUTE: PROFILO UTENTE ---
@bp.route("/user/<int:id>")
def user_profile(id):
    user = user_repository.get_user_by_id(id)
    if user is None:
        abort(404, f"L'utente id {id} non esiste.")

    posts = post_repository.get_posts_by_author(id)
    return render_template("user_profile.html", user=user, posts=posts)


# --- ROUTE: ARCHIVIO PER DATA ---
@bp.route("/archive", methods=("GET", "POST"))
def archive():
    posts = []
    selected_year = None
    selected_month = None

    if request.method == "POST":
        year_str = request.form.get("year")
        month_str = request.form.get("month")

        if year_str and month_str:
            selected_year = int(year_str)
            selected_month = int(month_str)
            posts = post_repository.get_posts_by_month(selected_year, selected_month)

    return render_template("archive.html", posts=posts, selected_year=selected_year, selected_month=selected_month)


# --- ROUTE: TOGGLE PREFERITO ---
@bp.route("/post/<int:id>/bookmark", methods=("POST",))
def toggle_bookmark(id):
    if g.user is None:
        return redirect(url_for("auth.login"))

    # Toggle: se esiste rimuovi, altrimenti aggiungi
    if bookmark_repository.is_bookmarked(g.user["id"], id):
        bookmark_repository.remove_bookmark(g.user["id"], id)
    else:
        bookmark_repository.add_bookmark(g.user["id"], id)

    return redirect(url_for("main.index"))


# --- ROUTE: LISTA PREFERITI ---
@bp.route("/bookmarks")
def bookmarks():
    if g.user is None:
        return redirect(url_for("auth.login"))

    bookmarks = bookmark_repository.get_user_bookmarks(g.user["id"])
    return render_template("bookmarks.html", bookmarks=bookmarks)
