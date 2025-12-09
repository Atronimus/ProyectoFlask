# ProyectoFlask

Instalacion

Descargar Python version 3.13.7
MySQL / MariaDB (Laragon o XAMPP) version 6.0 en laragon


Ejecutar este comando

python -m venv venv

Luego activarlo

venv\Scripts\activate

Instalar dependencias

pip install -r requirements.txt

Con el entorno activado, abre Python:
Luego dentro de la consola:

from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()

para crear la tabla de user

Luego correr el comando

python run.py
