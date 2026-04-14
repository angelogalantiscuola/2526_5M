from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import categoria_repository, piatto_repository

bp = Blueprint("main", __name__)


# TODO: Implementa le route richieste dall'esercizio 1 e 2
