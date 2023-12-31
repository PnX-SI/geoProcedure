from flask import Flask

# from flask_sqlalchemy_app.env import db
# from .config.config import config

from geoprocedure.config.config import config

from geoprocedure.env import APP_DIR, db, ma, migrate


def create_app():
    app = Flask(__name__)
    app.config.update(config)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from geoprocedure.blueprint import routes

    app.register_blueprint(routes)
    return app
