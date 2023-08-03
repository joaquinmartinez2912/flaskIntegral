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
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://BD2021:BD2021itec@143.198.156.171/db_joaquinppp"

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


class Categorias(db.Model):
    __tablename__ = "categoria"
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(50),nullable = False)

    def __str__(self):
        return self.nombre


class Entrada(db.Model):
    __tablename__ = "entrada"
    id = db.Column(db.Integer,primary_key = True)
    titulo = db.Column(db.String(50),nullable = False)
    contenido = db.Column(db.String(140),nullable = False)
    fecha = db.Column(db.String(50),nullable = False)
    autor = db.Column(
                    db.Integer,
                    ForeignKey("usuarios.id"),
                    nullable=False )
    etiqueta = db.Column(
                    db.Integer,
                    ForeignKey("categoria.id"),
                    nullable=False )

    def __str__(self):
        return self.titulo


class Comentarios(db.Model):
    __tablename__ = "comentario"
    id = db.Column(db.Integer,primary_key = True)
    contenido = db.Column(db.String(140),nullable = False)
    fecha = db.Column(db.String(50),nullable = False)
    autor = db.Column(
                    db.Integer,
                    ForeignKey("usuarios.id"),
                    nullable=False )
    etiqueta = db.Column(
                    db.Integer,
                    ForeignKey("entrada.id"),
                    nullable=False )

    def __str__(self):
        return self.titulo


# Rutas

@app.context_processor
def inject_paises():
    cat = db.session.query(Categorias).all()   
    return dict(
        listaCategorias=cat
    )


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/principal")
def main():
    # posteos = levanto los posteos de la base de datos.
    # Lo paso como parametro en el render_template
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


