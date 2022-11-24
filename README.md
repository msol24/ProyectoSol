# Rock and Blog

*Maria Sol Pucciarelli*

>Proyecto basado en un blog para reseñar nuevos discos. La temática (el disco) lo genera el superuser y los comentarios y opiniones, los suscriptores. Todo en muy fase beta, usando las herramientas y maneras aprendidas durante el cursado de Python impartido por Coder House.

## Herramientas utilizadas

- Python 3.9

- Django 4.1.3

- HTML: 5

## Instalacion git clone

Para acceder al proyecto clonándolo, deberás ejecutar en consola:
 
```sh
git clone https://github.com/msol24/ProyectoSol.git
```

## Instalacion entorno virtual 
```sh
pip install virtualenv

virtualenv "virtual1"

.\virtual1\scripts\activate
```
Luego de observar el entorno virtual activo, ponemos a correr el servidor...
```sh
python manage.py runserver
```
y seguimos el vínculo brindado en consola...
```sh
Django version 4.1.3, using settings 'ProyectoSol.settings'
Starting development server at http://127.0.0.1:8000/
```
## Frontend

Una vez dentro de la aplicación web, observamos una navbar con cuatro botones:

- Suscribirse: guarda un suscriptor, con nombre, mail, fecha de nacimiento y un dato booleano, para en un futuro reciba notificaciones por mail.

- Postea: guarda un comentario del suscriptor, con id (que debe generarlo el usuario en el momento, 12345 por ejemplo), nombre del suscriptor, fecha en la que escribe, y la descripción o post justamente.

- Buscar Post: realiza una busqueda a traves del id del post, devuelve el comentario y el id.

- Buscar Suscriptor: realiza una busqueda por coincidencia de email, devuelve el nombre del suscriptor y el email asociado.

En el page content, encontramos una serie de posts, en los que doy una breve info del material y un boton de **Opina**, en el que el suscriptor deja un comentario o reseña, y se guarda con su nombre y la fecha de publicación.

Todos los datos recolectados se pueden ver a traves del **admin de Django**...
- Superuser: SolPucha
- Password: Vera13102020

Las funcionalidades de este primer proyecto, son basicamente poner en practica el uso de Herencias de HTML, Vistas generadas por Clases, Formularios para la inserción de datos y formularios para la búsqueda por coincidencia en los datos generados en la mini base de datos.

## Backend

El proyecto se creó utilizando una plantilla de HTML obtenida de https://startbootstrap.com/ como template y añadiendo las funcionalidades ya mencionadas.

## Modelos
Los modelos fueron creados por la generación de **clases**, una por cada temática propuesta en el blog (los discos a comentar), siendo 5 en total; más una clase para suscriptor y otra para post. 

## Formularios

Formularios creados por clases, heredando los Forms de Django.

Un formulario para la opinión de cada propuesta, solicitando la fecha de publicación, el nobre de usuario y la reseña en sí.

Los otros forms solicitan datos para la creación de suscriptor (solicita nombre, email, fecha de nacimiento y el booleano para aceptar mails), y de post (id de post, nombre, fecha y descripción).

## Vistas

Son vistas basadas en funciones, y como todo lo anterior, habrá una funcion para cada temática (para las opiniones del suscriptor)...

```sh
 def we_opinion(request):
```

Y dos funciones para suscriptor y post, una de creación y otra de búsqueda...

```sh
 def crear_suscriptor(request):

 def buscar_suscriptor(request):
```
## Muchas Gracias!