from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuración
    app.config['SECRET_KEY'] = 'clave-super-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/proyectoflask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    # Importar rutas
    from .routes import auth
    app.register_blueprint(auth)

    return app
