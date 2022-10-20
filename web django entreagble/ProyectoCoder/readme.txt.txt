Pagina web gimansio.

Para ingresar a la pagina web, primero me situo en la carpeta "Proyecto coder" para poder iniciar el manage.py y abrir el servidor.
Ingresamos a http://127.0.0.1:8000/AppCoder/ , y veremos la pagina principal, con sus respectivas secciones, inicio, gimnasio, cliente y rutinas;
si hacemos click a cada una de ellas nos llevara a dicha url donde se mostrara el mensaje de cada seccion.

Luego cree definiciones POST para poder agregar informacion de las secciones de Gimnasio, Rutinas y Clientes, estos se encuentran en los siguientes urls :
- http://127.0.0.1:8000/AppCoder/form1/  . Para rutinas.
-http://127.0.0.1:8000/AppCoder/form2/ . Para clientes.
-http://127.0.0.1:8000/AppCoder/form3/ . Para el gimnasio.

Tambien cree el metodo GET para poder buscar rutinas, con la siguiente url:

http://127.0.0.1:8000/AppCoder/buscarRutinas/ .  Lo hice con el formato "text" para poder escribir por ejemplo "PECHO", y que me salga el dia.



Las funcionalidades POST Y GET , se encuentran en el apartado de views.py junto a las vistas de cada seccion, que al  mismo tiempo estan vinculadas con un url, creado en urls.py a los cuales vincule con un template
creado en la carpeta templates.






