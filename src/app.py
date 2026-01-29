from flask import Flask, jsonify, render_template

from src.models import Account, Transaction, db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ledger.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

        @app.route("/")
        def index():
            return render_template("index.html")

        @app.route("/api/status")
        def status():
            accounts_count = Account.query.count()
            return jsonify({"status": "online", "accounts": accounts_count})

        return app
