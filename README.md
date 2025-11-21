# Mini Office

Mini Office es una aplicación de escritorio desarrollada en Python utilizando PySide6 (Qt for Python).  
Permite crear, editar y guardar documentos de texto con formato, incorporando funciones básicas de un procesador de texto como edición, formato y búsqueda avanzada.

---

![Captura](images/app.png)

---

## Funcionalidades principales

### Gestión de archivos

- Nuevo archivo: Limpia el contenido actual para iniciar un nuevo documento.
- Abrir archivo: Permite cargar archivos de texto (.txt) o HTML (.html).
- Guardar archivo: Guarda el documento en formato texto o HTML según la extensión seleccionada.
- Salir: Cierra la aplicación de forma segura.

### Edición de texto

- Deshacer / Rehacer: Control de cambios para revertir o restaurar acciones.
- Copiar, cortar y pegar: Soporte completo del portapapeles.
- Formato de texto: Aplicación de negrita, cursiva, cambio de fuente y color de fondo del texto.

### Búsqueda y reemplazo

- Panel lateral acoplable o flotante para buscar y reemplazar texto.
- Posibilidad de buscar siguiente, anterior o todas las coincidencias.
- Resaltado de coincidencias en el documento.
- Reemplazo individual o global de términos.

### Interfaz y usabilidad

- Barra de herramientas principal con las acciones más frecuentes.
- Subbarra de formato de texto con botones para negrita, cursiva, fuente y color de fondo.
- Barra de estado que muestra en tiempo real el número de palabras y caracteres del documento.
- Atajos de teclado para todas las acciones principales.

---

## Atajos de teclado

| Acción              | Atajo            |
| ------------------- | ---------------- |
| Nuevo               | Ctrl + N         |
| Abrir               | Ctrl + A         |
| Guardar             | Ctrl + G         |
| Salir               | Ctrl + E         |
| Deshacer            | Ctrl + Z         |
| Rehacer             | Ctrl + Y         |
| Copiar              | Ctrl + C         |
| Cortar              | Ctrl + X         |
| Pegar               | Ctrl + V         |
| Buscar / Reemplazar | Ctrl + F         |
| Negrita             | Ctrl + B         |
| Cursiva             | Ctrl + I         |
| Color de fondo      | Ctrl + Shift + C |
| Tipo de letra       | Ctrl + T         |

---

## Tecnologías utilizadas

- Python
- PySide6

---

## Pasos para generar el ejecutador .exe

- Instalar pipx para utilizarlo como instalador en lugar de pip, así evitamos conflictos con dependencias y otros problemas.

![Captura](images/capturas/1.png)

- Agregamos pipx a las variable de entorno del sistema para poder usarlo como comando desde terminal.

![Captura](images/capturas/2.png)

- Instalar pipenv que sirve para gestionar las dependencias y el entorno virtual que vamos a usar.

![Captura](images/capturas/3.png)

- Inicializar el entorno virtual.

![Captura](images/capturas/4.png)

- Instalar las dependencias necesarias sobre el entorno virtual, en este caso pyside6 y pyinstaller.

![Captura](images/capturas/5.png)

- Entramos al subshell.

![Captura](images/capturas/6.png)

- Ahora hay que generar el .exe en un único archivo con --onefile, --noconsole para evitar ver se despliegue la consola al ejecutarlo, --name para definir el nombre del .exe, --icon para definir el icono y --add-data para agregar las imagenes y otros recursos de los que dependan el proyecto.

![Captura](images/capturas/7.png)

---

## Autor

Ignacio Manuel<br>
Desarrollo de Aplicaciones Multiplataforma (DAM)<br>
Módulo: Desarrollo de Interfaces
