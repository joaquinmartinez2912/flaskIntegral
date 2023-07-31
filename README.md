# flaskIntegral
Trabajo integral de flask - PPI ITEC 2023.
## Tabla de contenidos
- [Entorno Virtual e Inicio](#Entorno-Virtual-e-Inicio)
- [Templates](#Templates)
***

## *Entorno Virtual e Inicio*

**Paso 1.**

Crear entorno virtual de python en Linux.

```
python3 -m venv venv
```

El segundo *venv* es el nombre del entorno (Se puede poner otro).

**Paso 2.**

Activar entorno virtual.

```
source venv/bin/activate
```

**Paso 3.**

Dentro del entorno, levantar el archivo requirements.txt que contiene las dependencias necesarias para poder trabajar.

```
pip install -r requirements.txt
```

**Paso 4.**

Crear un archivo app.py a la altura del entorno virtual desde Visual Studio Code.

![app.py](img/1_entorno.jpeg "app.py")

**Paso 5.**
 
Crear instancia de FLASK

```python 
from flask import (
 Flask
)

app = Flask(__name__)
```

**Paso 6.**

Iniciar servidor
```
flask run --reload
```

**Paso 7.**

Crear una ruta

```python 
@app.route('/')
def index():
    return "<h1> Hola Flask </h1>"
```

## *Templates*

### **Creacion.**

A la misma altura de la carpeta se crea la carpeta *templates* de donde se tomaran todos los archivos HTML a los cuales se vincularan las distintas rutas.

![temp](img/2_templates.jpeg "temp")

Posteriormente, importo *render_template* de Flask

```python 
from flask import (
    render_template
)

```

Realizado esto, se modifica la ruta en el archivo app.py

```python 
@app.route('/')
def index():
    return render_template('index.html')
```

### **Utiles - Jinja.**

- Hacer extension.
```html
{% extends 'layout.html' %}
```
- Crear bloque
```html
{% block title %}  {% endblock %}
```

### **Context Procesor**

Dentro de *app.py*, creo el siguiente metedo:

```python 
@app.context_processor
def set_mensaje():
    mensaje = "Bienvenido al ITEC"
    return dict(
        mensaje = mensaje
    )
```

Todo el contenido del diccionario definido en este metodo se puede citar en cualquier template.

