# Instalacion Django con python
### (Leer en MarkDown con Vs Code)
<br>
1.	Instalar python con path (Omitir si ya tienes instalado python)

2. instalar pip:
	1. Chequear si pip instalado:
		- En cmd: <code>pip --version</code>
	2. Si no: https://pip.pypa.io/en/stable/cli/pip_install/
	3. Chequear nuevamente si pip esta bien instalado
	<br><br>
3. Instalar Django:
	1. En cmd: <code>pip install django</code>
	2. En cmd: <code>django-admin version</code>
	<br><br>
4. Crear directorio para el servidor:
	1. Crear la carpeta y luego entrar dentro de ella.
	2. Click en la barra de direcciones y ponerse al inicio y anteponer "cmd " a la ruta y enter.
	3. Esto nos posicionará en la ubicación de la carpeta con la consola.
	<br><br>
5. Crear proyecto de Django:
	1. <code>django-admin startproject [nombreProyecto]</code>
	2. Una vez creado el proyecto se crea automáticamente una aplicación que servirá como default o admin.<br>(sugerencia dejarla como "admin").
	3. cd <code>[carpetaNombreProyecto]</code> (lugar donde está manage.py).
	4. <code>code  .</code> (esto abre vscode en este directorio).
	<br><br>
6. Crear una aplicación dentro del proyecto:
	1. <code>python manage.py startapp [nombreAplicacion]</code> (Crea el nuevo directorio de una nueva app)
	<br><br>
7. Configurar la página dentro del servidor:
	1. <code>cd [nombreAplicacion] </code> (Con esto entramos a la carpeta de la aplicacion recién creada)
	<br><br>
	2. Dentro de la carpeta [nombreAplicacion], crear directorio llamado templates crear el index.html
	<br><br>
	3. Abrir archivo views.py y crear la siguiente funcion en la linea 4:<br>
		<code>def nombreFuncion(request):<br>
			return render(request, 'index.html') </code>
	<br><br>
	4. Editar archivo urls.py en carpeta aplicacion [admin]:
		1. Agregar en la linea 18:	<code>from [direccionCarpetaAplicacion].views import [nombreFuncion]</code> (Estamos llamando a la funcion que esta en el archivo views.py que esta dentro de la [carpetaAplicacion])
		<br><br>
	5. Luego agregar en la seccion urlpatterns:
		1. debajo de: <code>path('admin/', admin.site.urls),</code><br>
		 Agregar: <code>path('[aliasDeLaSeccion]', [nombreFuncionEnViews.py])</code>
	<br><br>
	6. Editar el archivo settings.py en la misma carpeta:
		1. Agregar en la sección INSTALLED_APPS=[] en la ultima fila antes de cerrar el corchete:<br>
		<code>'[nombreApp]',</code>
	<br><br>
8.  Guardar los cambios y ejecutar el servidor:
	1. python manage.py makemigrations (mira los cambios y puedes volver atras)
	2. python manage.py migrate (mira todas las migraciones y guarda los cambios hechos)
	3. cambiar a cmd y ejecutar: <code>python manage.py runserver</code>
	<br><br>
9.	Agregar todos los assets a la página:
	1.	Crear una carpeta llamada "static" dentro de la carpeta de la aplicacion(En el mismo nivel que templates).
	<br><br>
	2.	Se agregaran todos los assets dentro de esa carpeta (Como css, imagenes, JScript file.)<br>
		y se dejarán en el directorio las páginas o secciones de esta misma(documentos .html).
		<br><br>
	3.	Al inicio del documento HTML se agregará la siguiente línea de código<code> {% load static %}</code>
	<br><br>
	4.	Y por último, se editarán las rutas de los elementos al nuevo orden del directorio y también al nuevo formato el cual será:
	<code>{% static 'ruta del elemento' %}</code>
	<br><br>
10. Agregar las subpaginas como secciones de la misma pagina
	1.	Volver al punto 7.3 hasta el 7.5
	2.	luego, en todas las páginas dónde se haga hypervinculo a otro documento html, solamente se invoca el alias, en vez de la ruta dónde está el documento.html
