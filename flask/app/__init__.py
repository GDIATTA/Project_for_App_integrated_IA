from flask import Flask
from app.routes.ai import ai_bp
from app.routes.items import items_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(items_bp)
    app.register_blueprint(ai_bp)

    return app
