from flask import (Flask,
    render_template,
    redirect,
    request,    
    url_for)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)

#mysql+pymysql://usuario:contraseña@ip/nombre_db
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/miniblog"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Clases:

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(50),nullable = False)
    correo = db.Column(db.String(50),nullable = False)
    contrasena = db.Column(db.String(50),nullable = False)

    def __str__(self):
        return self.nombre

# Rutas

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/principal")
def main():
    return render_template("main.html")

@app.route("/usuarios")
def user():
    return render_template("users.html")

@app.route("/agregarUsuario",methods=["POST"])
def agregarUsuario():
    if request.method == "POST":
        nombreUsuario = request.form["usuario"]
        correoUsuario = request.form["correo"]
        contrasenaUsuario = request.form["contra"]

        nuevoUsuario = Usuario(nombre=nombreUsuario, correo=correoUsuario, contrasena=contrasenaUsuario)
        db.session.add(nuevoUsuario)
        db.session.commit()

        return redirect(url_for("index"))


