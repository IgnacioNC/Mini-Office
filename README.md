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

## 🎤 Comandos de voz

MiniOffice incluye un sistema de **reconocimiento de voz** que permite ejecutar acciones del editor mediante comandos hablados.  
Para activarlo, selecciona **Editar → Reconocer voz** o pulse el icono del micrófono.

### 🗣️ Comandos disponibles

| Comando                              | Acción realizada                       |
| ------------------------------------ | -------------------------------------- |
| **"negrita"**                        | Activa o desactiva el texto en negrita |
| **"cursiva"**                        | Activa o desactiva la cursiva          |
| **"subrayado"**                      | Activa o desactiva el subrayado        |
| **"nuevo"** / **"nuevo documento"**  | Crea un archivo en blanco              |
| **"guardar"** /**"guardar archivo"** | Guarda el archivo actual               |

### 📝 Funcionamiento

El sistema escucha **un único comando** al activarse y ejecuta la acción correspondiente.  
Su objetivo es permitir **control por voz del editor**, no dictado continuo de texto.

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

## Firma digital del ejecutable

- Creación del certificado y comprobación.

![Captura](images/capturas/Screenshot_3.png)  
![Captura](images/capturas/Screenshot_4.png)

- Asignación de la contraseña al .pfx

![Captura](images/capturas/Screenshot_5.png)

- Exportación del certificado al escritorio.

![Captura](images/capturas/Screenshot_6.png)

- Instalación del SDK para las firmas de windows y lo agregamos al path del sistema.

![Captura](images/capturas/Screenshot_7.png)  
![Captura](images/capturas/Screenshot_8.png)

- Firma aplicada al ejecutable y verificación.

![Captura](images/capturas/Screenshot_9.png)
![Captura](images/capturas/Screenshot_10.png)

---

## Creación del instalador con Inno Setup

Para generar un instalador profesional se utilizó **Inno Setup**, configurando los parámetros.

- Instalación de Inno Setup

![Captura](images/capturas/Screenshot_11.png)

- En lugar de crear un Script en blanco, he utilizado el de Wizard.

![Captura](images/capturas/Screenshot_12.png)

- Proceso de instalación.

![Captura](images/capturas/Screenshot_13.png)
![Captura](images/capturas/Screenshot_14.png)
![Captura](images/capturas/Screenshot_15.png)
![Captura](images/capturas/Screenshot_16.png)
(Importante que si quieres que se genere el desinstalador marques la opción)

- Selección de licencia MIT.

![Captura](images/capturas/Screenshot_17.png)

- Continuación de la instalación.

![Captura](images/capturas/Screenshot_18.png)
![Captura](images/capturas/Screenshot_19.png)
![Captura](images/capturas/Screenshot_20.png)

- Nombre del instalador cuando se genere y dirección del icono que tendrá.

![Captura](images/capturas/Screenshot_22.png)

- Estilo que tendrá el instalador.

![Captura](images/capturas/Screenshot_23.png)

- Script del .iss una vez generado y configurado.

![Captura](images/capturas/Screenshot_25.png)

- Se han cambiado las rutas absolutas por rutas relativas y luego se ha compilado.

![Captura](images/capturas/Screenshot_26.png)

- Una vez generado el instalador, comprobar que funciona.

![Captura](images/capturas/Screenshot_28.png)
![Captura](images/capturas/Screenshot_29.png)
![Captura](images/capturas/Screenshot_31.png)

---

## Publicación del instalador y el .exe en GitHub Releases

Para no subir ejecutables al repositorio, se usa **GitHub Releases**.

- Instalación de GitHub CLI.

![Captura](images/capturas/Screenshot_32.png)

- Autenticación en cuenta de GitHub.

![Captura](images/capturas/Screenshot_33.png)

- Creación de la release desde terminal.

![Captura](images/capturas/Screenshot_35.png)

- Resultado final por terminal

![Captura](images/capturas/Screenshot_36.png)

El instalador puede descargarse desde la sección **Releases** del repositorio.

---

## Autor

Ignacio Manuel<br>
Desarrollo de Aplicaciones Multiplataforma (DAM)<br>
Módulo: Desarrollo de Interfaces
