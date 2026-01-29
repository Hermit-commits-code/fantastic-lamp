from flask import Flask, jsonify, render_template

from src.models import Account, Transaction, db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ledger.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()

        @app.route("/")
        def index():
            return "<h1>Hermit Ledger v0.5.0</h1>"
