from flask import Flask, render_template
from app.config import Config
from app.extensions import db, migrate
from flask_mail import Mail


mail = Mail()

from .routes.main_routes import main
from .routes.auth_routes import auth
from .routes.admin_routes import admin


def start_app():
    app = Flask(__name__)

    app.config.from_object("app.config.Config")
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    
    @app.errorhandler(400)
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html")
    

    return app
