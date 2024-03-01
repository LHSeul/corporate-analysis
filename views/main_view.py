from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__, url_prefix='/')

@main_bp.route('/')
def main_page():
    return render_template("index.html")

@main_bp.route('/', methods=["POST"])
def search():
    search_word = request.form.get('search_word')
    
    return render_template("index.html")