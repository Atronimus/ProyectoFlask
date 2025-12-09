from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuración
    app.config['SECRET_KEY'] = '317fa9ea388016ac94c3b441b9c75236778a35964c889f31b51c688d06d24bf8'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:S4wmizry6irgtCn+@127.0.0.1:3306/proyectoflask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    # Importar rutas
    from .routes import auth
    app.register_blueprint(auth)

    return app
