from app.config import Config
from flask import Flask
from flask_bootstrap import Bootstrap

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    bootstrap = Bootstrap(app)
    
    return app