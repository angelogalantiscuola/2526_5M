# FILE: app/main.py
# Aggiungi queste route al file esistente

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import post_repository, comment_repository # type: ignore

bp = Blueprint('main', __name__)

# ... [Mantieni le route esistenti: index(), about(), create(), update(), delete()] ...

def get_post(id, check_author=True):
    """Recupera un post e verifica autorizzazione."""
    post = post_repository.get_post_by_id(id)
    if post is None:
        abort(404, f"Il post id {id} non esiste.")
    if check_author and post['author_id'] != g.user['id']:
        abort(403)
    return post

# NUOVA ROUTE: Dettaglio Post
@bp.route('/post/<int:id>')
def post_detail(id):
    """Mostra i dettagli di un singolo post con commenti."""
    post = post_repository.get_post_by_id(id)
    if post is None:
        abort(404)
    comments = comment_repository.get_comments_by_post(id)
    return render_template('blog/detail.html', post=post, comments=comments)

# NUOVA ROUTE: Ricerca Post
@bp.route('/search', methods=('GET', 'POST'))
def search():
    """Ricerca post per titolo."""
    posts = []
    search_term = ''
    
    if request.method == 'POST':
        search_term = request.form.get('search_term', '')
        if search_term:
            posts = post_repository.search_posts_by_title(search_term)
    
    return render_template('search_results.html', posts=posts, search_term=search_term)

# NUOVA ROUTE: Aggiungi Commento
@bp.route('/post/<int:id>/comment', methods=('POST',))
def add_comment(id):
    """Aggiungi un commento a un post."""
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    # Verifica che il post esista
    post = post_repository.get_post_by_id(id)
    if post is None:
        abort(404)
    
    body = request.form.get('body', '').strip()
    
    if not body:
        flash('Il commento non può essere vuoto.')
    else:
        comment_repository.create_comment(id, g.user['id'], body)
        flash('Commento aggiunto!')
    
    return redirect(url_for('main.post_detail', id=id))
