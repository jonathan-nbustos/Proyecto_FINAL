## App Calendary 

Es una aplicación web creada para poder dejar registro de las vacaciones, de los cumpleaños y realizar algun comentario o saludo.
Cabe mencionar que para poder acceder a dicha información y poder dejar registro, se debe contar con un usuario y contraseña.

Cuando se cuenta con un user, aparecerán las siguientes opciones adicionales:

- CUMPLEAÑOS: Aquí podrá ver el listado de cumpleaños, crear un nuevo cumpleaños, como así también modificarlo, eliminarlo o ver en detalle.
- VACACIONES: Aquí podrá ver el litado de vacaciones, cargar un nuevo período de vacaciones, realizar algún cambio, verlo en detalle  y eliminarla.
- SALUDOS: Aquí verán los saludos que dejan las personas, y también podrán, editarlo, modificarlo o borrarlo.
- CONTACTO: Desde aquí podrán enviar alguna consulta o sugerencia.
- LOGIN: Una vez logueado, si cuenta con permiso de ADMINISTRADOR, podrá acceder al Panel ADMINISTRADOR.
- Al lado de Login, encontrarán el nombre de su propio USER, desde el que podrán acceder para Editarlo, Agregar un AVATAR o cambiar la contraseña .
- Si se cuenta con un AVATAR, aparecerá al lado del nombre de Usuario.
- En el inicio se cuenta con 3 ACCESSOS RÁPIDOS a Cumpleaños, Vacaciones y Saludos.

## Entornos virtuales


Para iniciar el servidior, se debe crear y activar el Entorno Virtual:

CREAR:
- `python -m venv .venv` (Windows)
- `python3 -m venv .venv` (Linux o Mac)

ACTIVAR:
- `.\.venv\Scripts\activate`  (Windows Powershell)
- `source .venv/bin/activate` (Linux o Mac)

También se deben crear e instalar los paquetes de requirements.txt:

CREAR:
- `pip freeze >> requirements.txt`

ACTIVAR:
- `pip install -r requirements.txt`


## Luego se crea el Proyecto "project"
    
1. Crear una carpeta para el proyecto en la raiz:
    - `md project`

2. Acceder a la carpeta `project`
    - `cd project`

3. Crear las carpetas y archivos necesarios
    - `django-admin startproject config .`

4. Ejecutar el servidor:
    - `python manage.py runserver`


## Establecer `config.settings.SECRET_KEY`

```py
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()
```

## Posteriormente se crean las Aplicaciones:

1. Estar ubicado dentro de `project` pero fuera de `config`
    
2. Crear las aplicaciones Django con el nombre que desee. En este casose crearon 3:

    - `django-admin startapp AppCalendary`
    - `django-admin startapp cumpleanios`
    - `django-admin startapp vacaciones`

3. Agregar el nombre de las app en lista `config.settings.INSTALLED_APPS`

4. Cada aplicación cuenta con la carpeta templates: que contienen las páginas web.

5. También podrán observar los componenetes necesarios para crear y navegar entre las páginas como son: 
    - "urls.py":Este archivo define las URL de la aplicación, especificando qué vista (función o clase de vista) manejará cada URL.
                Contiene la configuración de las rutas y la asignación a las funciones o clases de vista correspondientes.
    - "views.py": En este archivo se encuentran las funciones o clases de vista que definen cómo responder a las solicitudes web.
                  Contiene la lógica de presentación y se encarga de procesar la entrada del usuario y devolver la respuesta adecuada.
    - "models.py": Aquí se definen las clases de modelos que representan las tablas en la base de datos.
                   Define la estructura de los datos y las relaciones entre ellos.
    - "forms.py": Contiene clases de formulario que se utilizan para validar y procesar los datos ingresados por el usuario en formularios HTML.
                  Facilita la validación de datos y su posterior almacenamiento en la base de datos.

Estos archivos trabajan en conjunto para construir una aplicación web Django funcional y bien estructurada.

## Crear base de datos

Crear archivos Python pre-SQL:

- `python manage.py makemigrations`

Crear SQL y modificar base de datos:

- `python manage.py migrate`

## Crear superusuario

- `python manage.py createsuperuser`
- Usuario de prueba: coder / 123

## Crear directorio media
- Encontrarán las imagenes del Avatar.