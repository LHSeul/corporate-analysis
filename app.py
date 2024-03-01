from flask import Flask
import config

def create_app():
    app = Flask(__name__)

    from views import main_view
    app.register_blueprint(main_view.main_bp)
    
    return app
