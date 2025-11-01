import os

from PySide6.QtWidgets import QMainWindow,QApplication, QLabel, QWidget, QDockWidget, QTextEdit, QToolBar, QMainWindow, QFileDialog, QStatusBar, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout, QColorDialog, QFontDialog
from PySide6.QtGui import QAction, QIcon, QKeySequence, QTextCursor, QTextCharFormat, QFont, QColor, QTextDocument
from PySide6.QtCore import Qt, QSize
from html import escape

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.window() # Configuración de la ventana.
        self.barra_menu()   # Configuración de la barra de menú.
        self.cargarIconos()  # Carga de los iconos.
        self.crearAcciones() # Creación de las acciones.
        self.agregarAccionesAlMenu() # Agregar acciones al menú.
        self.barraHerramientas() # Creación de la barra de herramientas y agregar acciones.
        self.bloqueTexto() # Creación del bloque de texto.
        self.crearLayoutBusqueda() # Creación del layout para buscar y reemplazar.
        self.letraSubBarraHerramientas() # Creación de la sub barra de herramientas para modificaciones de letra.
        self.shortCuts() # Asignación de los atajos de teclado.
        self.statusBar() # Creación de la barra de estado.
        self.statusBarMessage() # Mensaje inicial de la barra de estado.

        self.accionNuevo.triggered.connect(self.nuevoArchivo)
        self.accionAbrir.triggered.connect(self.abrirArchivo)
        self.accionGuardar.triggered.connect(self.guardarArchivo)
        self.accionSalir.triggered.connect(self.salirAplicacion)
        self.accionDeshacer.triggered.connect(self.deshacerAccion)
        self.acccionRehacer.triggered.connect(self.rehacerAccion)
        self.accionCopiar.triggered.connect(self.copiarTexto)
        self.accionCortar.triggered.connect(self.cortarTexto)
        self.accionPegar.triggered.connect(self.pegarTexto)
        self.accionBuscarReemplazar.triggered.connect(self.menuBuscarReemplazar)
        self.accionBuscar.triggered.connect(self.buscarPalabra)
        self.accionLetraNegrita.triggered.connect(self.toggleNegrita)
        self.accionLetraCursiva.triggered.connect(self.toggleCursiva)
        self.accionLetraColorFondo.triggered.connect(self.elegirColorFondoLetra)
        self.accionTipoLetra.triggered.connect(self.elegirFuente)
        self.texto.textChanged.connect(self.statusBarMessage)

    def window(self):

        self.setWindowTitle("Mini Word")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "images/iconoWord.png")))

    def barra_menu(self):
        
        barraMenu = self.menuBar()
        self.menuArchivo = barraMenu.addMenu("&Archivo")
        self.menuEditar = barraMenu.addMenu("&Editar")

    def letraSubBarraHerramientas(self):

        panelLetra = QWidget()
        layoutLetra = QHBoxLayout(panelLetra)
        layoutLetra.setAlignment(Qt.AlignTop)

        botonFuente = QPushButton(QIcon(self.iconoLetraFuente), "")
        self.botonNegrita = QPushButton(QIcon(self.iconoLetraNegrita), "")
        self.botonCursiva = QPushButton(QIcon(self.iconoLetraCursiva), "")
        botonColorFondo = QPushButton(QIcon(self.iconoLetraFondo), "")

        botonFuente.setToolTip("Fuente (Ctrl+T)")
        self.botonNegrita.setToolTip("Negrita (Ctrl+B)")
        self.botonCursiva.setToolTip("Cursiva (Ctrl+I)")
        botonColorFondo.setToolTip("Color de fondo (Ctrl+Shift+C)")

        layoutLetra.addWidget(botonFuente)
        layoutLetra.addWidget(self.botonNegrita)
        layoutLetra.addWidget(self.botonCursiva)
        layoutLetra.addWidget(botonColorFondo)

        botonFuente.setFixedSize(30, 30)
        self.botonNegrita.setFixedSize(30, 30)
        self.botonCursiva.setFixedSize(30, 30)
        botonColorFondo.setFixedSize(30, 30)

        botonFuente.setIconSize(QSize(26, 26))
        self.botonNegrita.setIconSize(QSize(26, 26))
        self.botonCursiva.setIconSize(QSize(26, 26))
        botonColorFondo.setIconSize(QSize(26, 26))

        self.botonCursiva.setCheckable(True)
        self.botonNegrita.setCheckable(True)

        estiloBoton = """
        QPushButton {
            border: none;
            border-radius: 4px;
            background-color: transparent;
        }
        QPushButton:hover {
            background-color: gray;
        }
        QPushButton:pressed {
            border: 0.5px solid rgba(128, 128, 128, 0.15);
            background-color: transparent;
        }
        QPushButton:checked {
            background-color: gray;
        }
        """
        botonFuente.setStyleSheet(estiloBoton)
        self.botonNegrita.setStyleSheet(estiloBoton)
        self.botonCursiva.setStyleSheet(estiloBoton)
        botonColorFondo.setStyleSheet(estiloBoton)

        self.contenedorDockLetra = QDockWidget()
        self.contenedorDockLetra.setWidget(panelLetra)

        layoutLetra.setContentsMargins(5, 5, 0, 0)
        self.contenedorDockLetra.setFixedHeight(35)    # Esto provoca que no pueda ajustar la altura el usuario
        layoutLetra.setSpacing(8)
        layoutLetra.setAlignment(Qt.AlignLeft)  # Alinea los botones a la izquierda

        self.contenedorDockLetra.setTitleBarWidget(QWidget()) # Quita la barra de título vacía
        self.contenedorDockLetra.setAllowedAreas(Qt.TopDockWidgetArea)
        self.addDockWidget(Qt.TopDockWidgetArea, self.contenedorDockLetra)

        botonFuente.clicked.connect(self.elegirFuente)
        self.botonNegrita.clicked.connect(self.toggleNegrita)
        self.botonCursiva.clicked.connect(self.toggleCursiva)
        botonColorFondo.clicked.connect(self.elegirColorFondoLetra)

    def elegirColorFondoLetra(self):
        self.texto.setTextBackgroundColor(QColorDialog.getColor())

    def elegirFuente(self):
        cursor = self.texto.textCursor()
        fuente_base = (
            self.texto.currentCharFormat().font()
            if cursor.hasSelection()
            else self.texto.currentFont()
        )

        ok, fuente = QFontDialog.getFont(fuente_base, self, "Seleccionar fuente") # En mi caso, si hago "fuente, ok" no me funciona

        formato = QTextCharFormat()
        formato.setFont(fuente)

        if cursor.hasSelection():
            cursor.mergeCharFormat(formato)
            self.texto.setTextCursor(cursor)
        else:
            self.texto.mergeCurrentCharFormat(formato)

    def toggleNegrita(self):
        if self.texto.fontWeight() != QFont.Bold:
            self.texto.setFontWeight(QFont.Bold)
            self.botonNegrita.setChecked(True)
        else:
            self.texto.setFontWeight(QFont.Normal)
            self.botonNegrita.setChecked(False)

    def toggleCursiva(self):
        if self.texto.fontItalic() == False:
            self.texto.setFontItalic(True)
            self.botonCursiva.setChecked(True)
        else:
            self.texto.setFontItalic(False)   
            self.botonCursiva.setChecked(False) 

    def barraHerramientas(self):

        barra_herramientas = QToolBar("Barra de herramientas")

        barra_herramientas.setToolButtonStyle(Qt.ToolButtonIconOnly)

        barra_herramientas.addAction(self.accionNuevo)
        barra_herramientas.addAction(self.accionAbrir)
        barra_herramientas.addAction(self.accionGuardar)
        barra_herramientas.addAction(self.accionSalir)
        barra_herramientas.addAction(self.accionDeshacer)
        barra_herramientas.addAction(self.acccionRehacer)
        barra_herramientas.addAction(self.accionCopiar)
        barra_herramientas.addAction(self.accionCortar)
        barra_herramientas.addAction(self.accionPegar)
        barra_herramientas.addAction(self.accionBuscarReemplazar)

        barra_herramientas.setIconSize(QSize(32, 32))

        barra_herramientas.setMovable(False)

        self.addToolBar(barra_herramientas) 

    def bloqueTexto(self):

        self.texto = QTextEdit()
        self.texto.setAcceptRichText(True)
        self.setCentralWidget(self.texto)
        self.texto.setFocus()
        self.texto.setViewportMargins(5, 4, 5, 4)

    def crearLayoutBusqueda(self):

        self.setCentralWidget(self.texto)

        panelDerecho = QWidget()
        layoutDerecho = QVBoxLayout(panelDerecho)
        layoutDerecho.setAlignment(Qt.AlignTop) 

        layoutBuscar = QHBoxLayout()
        self.textoBuscarPalabra = QLineEdit()
        tlBuscar = QLabel("Buscar: ")
        layoutBuscar.addWidget(tlBuscar)
        layoutBuscar.addWidget(self.textoBuscarPalabra)

        layoutReemplazar = QHBoxLayout()
        self.textoReemplazarPalabra = QLineEdit()
        tlReemplazarPalabra = QLabel("Reemplazar por: ")
        layoutReemplazar.addWidget(tlReemplazarPalabra)
        layoutReemplazar.addWidget(self.textoReemplazarPalabra)

        layoutBtnBuscar = QHBoxLayout()
        layoutBtnReemplazar = QHBoxLayout()

        botonBuscarSiguientePalabra = QPushButton("Buscar siguiente")
        layoutBtnBuscar.addWidget(botonBuscarSiguientePalabra)

        botonBuscarAnteriorPalabra = QPushButton("Buscar anterior")
        layoutBtnBuscar.addWidget(botonBuscarAnteriorPalabra)

        botonBuscarTodasPalabras = QPushButton("Buscar todo")
        layoutBtnBuscar.addWidget(botonBuscarTodasPalabras)

        botonReemplazarPalabra = QPushButton("Reemplazar")
        layoutBtnReemplazar.addWidget(botonReemplazarPalabra)

        botonReemplazarTodasPalabras = QPushButton("Reemplazar todo")
        layoutBtnReemplazar.addWidget(botonReemplazarTodasPalabras)

        layoutDerecho.addLayout(layoutBuscar)
        layoutDerecho.addLayout(layoutReemplazar)
        layoutDerecho.addLayout(layoutBtnBuscar)
        layoutDerecho.addLayout(layoutBtnReemplazar)

        self.contenedorDock = QDockWidget("BUSCAR Y REEMPLAZAR", self)
        self.contenedorDock.setWidget(panelDerecho)
        self.contenedorDock.setVisible(False)
        #self.contenedorDock.setFloating(True) # Inicia flotando
        self.contenedorDock.move(1220, 133.5)
        self.contenedorDock.topLevelChanged.connect(self.cambiarTamanioLayoutBusqueda)
        self.contenedorDock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.contenedorDock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)

        self.addDockWidget(Qt.RightDockWidgetArea, self.contenedorDock)

        self.textoBuscarPalabra.textChanged.connect(self.buscarPalabra)
        botonBuscarTodasPalabras.clicked.connect(self.buscarTodasPalabras)
        botonBuscarSiguientePalabra.clicked.connect(self.buscarSiguientePalabra)
        botonBuscarAnteriorPalabra.clicked.connect(self.buscarAnteriorPalabra)
        botonReemplazarPalabra.clicked.connect(self.reemplazarPalabra)
        botonReemplazarTodasPalabras.clicked.connect(self.reemplazarTodasPalabras)

        self.contenedorDock.visibilityChanged.connect(self.cambioVisibilidadDock)

    def cambiarTamanioLayoutBusqueda(self):
        if self.contenedorDock.isFloating():
            self.contenedorDock.resize(300, 100)
        else:
            self.contenedorDock.adjustSize()    

    def cargarIconos(self):

        self.iconoNuevo = os.path.join(os.path.dirname(__file__), "images/nuevo.png")
        self.iconoAbrir = os.path.join(os.path.dirname(__file__), "images/abrir.png")
        self.iconoGuardar = os.path.join(os.path.dirname(__file__), "images/guardar.png")
        self.iconoSalir = os.path.join(os.path.dirname(__file__), "images/salir.png")
        self.iconoDeshacer = os.path.join(os.path.dirname(__file__), "images/deshacer.png")
        self.iconoRehacer = os.path.join(os.path.dirname(__file__), "images/rehacer.png")
        self.iconoCopiar = os.path.join(os.path.dirname(__file__), "images/copiar.png")
        self.iconoCortar = os.path.join(os.path.dirname(__file__), "images/cortar.png")
        self.iconoPegar = os.path.join(os.path.dirname(__file__), "images/pegar.png")
        self.iconoBuscar = os.path.join(os.path.dirname(__file__), "images/buscar.png")
        self.iconoLetraFondo = os.path.join(os.path.dirname(__file__), "images/letraColorFondo.png")
        self.iconoLetraNegrita = os.path.join(os.path.dirname(__file__), "images/gordita.png")
        self.iconoLetraCursiva = os.path.join(os.path.dirname(__file__), "images/cursiva2.png")
        self.iconoLetraFuente = os.path.join(os.path.dirname(__file__), "images/letra.png")
    
    def crearAcciones(self):

        self.accionNuevo = QAction(QIcon(self.iconoNuevo), "Nuevo", self)
        self.accionAbrir = QAction(QIcon(self.iconoAbrir), "Abrir", self)
        self.accionGuardar = QAction(QIcon(self.iconoGuardar), "Guardar", self)
        self.accionSalir = QAction(QIcon(self.iconoSalir), "Salir", self)
        self.accionDeshacer =QAction(QIcon(self.iconoDeshacer), "Deshacer", self)
        self.acccionRehacer = QAction(QIcon(self.iconoRehacer), "Rehacer", self)
        self.accionCopiar = QAction(QIcon(self.iconoCopiar), "Copiar", self)
        self.accionCortar = QAction(QIcon(self.iconoCortar), "Cortar", self)
        self.accionPegar = QAction(QIcon(self.iconoPegar), "Pegar", self)
        self.accionBuscarReemplazar = QAction(QIcon(self.iconoBuscar), "Buscar/Reemplazar", self)
        self.accionBuscar = QAction("Buscar", self)
        self.accionLetraColorFondo = QAction(QIcon(self.iconoLetraFondo), "Color de fondo", self)
        self.accionLetraNegrita = QAction(QIcon(self.iconoLetraNegrita), "Negrita", self)
        self.accionLetraCursiva = QAction(QIcon(self.iconoLetraCursiva), "Cursiva", self)
        self.accionTipoLetra = QAction(QIcon(self.iconoLetraFuente), "Tipo de letra", self)

        self.accionNuevo.setToolTip("Crear un nuevo archivo (Ctrl+N)")
        self.accionAbrir.setToolTip("Abrir un archivo existente (Ctrl+A)")
        self.accionGuardar.setToolTip("Guardar el archivo actual (Ctrl+G)")
        self.accionSalir.setToolTip("Salir de la aplicación (Ctrl+E)")
        self.accionDeshacer.setToolTip("Deshacer la última acción (Ctrl+Z)")
        self.acccionRehacer.setToolTip("Rehacer la última acción deshecha (Ctrl+Y)")
        self.accionCopiar.setToolTip("Copiar el texto seleccionado (Ctrl+C)")
        self.accionCortar.setToolTip("Cortar el texto seleccionado (Ctrl+X)")
        self.accionPegar.setToolTip("Pegar desde el portapapeles (Ctrl+V)")
        self.accionBuscarReemplazar.setToolTip("Buscar y reemplazar texto en el documento (Ctrl+F)")
        self.accionTipoLetra.setToolTip("Cambiar propiedades de la letra (Ctrl+T)")

    def shortCuts(self):
        
        self.accionNuevo.setShortcut(QKeySequence("Ctrl+N"))
        self.accionAbrir.setShortcut(QKeySequence("Ctrl+A"))
        self.accionGuardar.setShortcut(QKeySequence("Ctrl+G"))
        self.accionSalir.setShortcut(QKeySequence("Ctrl+E"))
        self.accionDeshacer.setShortcut(QKeySequence("Ctrl+Z"))
        self.acccionRehacer.setShortcut(QKeySequence("Ctrl+Y"))
        self.accionCopiar.setShortcut(QKeySequence("Ctrl+C"))
        self.accionCortar.setShortcut(QKeySequence("Ctrl+X"))
        self.accionPegar.setShortcut(QKeySequence("Ctrl+V"))
        self.accionBuscarReemplazar.setShortcut(QKeySequence("Ctrl+F"))
        self.accionLetraNegrita.setShortcut(QKeySequence("Ctrl+B"))
        self.accionLetraCursiva.setShortcut(QKeySequence("Ctrl+I"))
        self.accionLetraColorFondo.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.accionTipoLetra.setShortcut(QKeySequence("Ctrl+T"))

    def agregarAccionesAlMenu(self):

        self.menuArchivo.addAction(self.accionNuevo)
        self.menuArchivo.addAction(self.accionAbrir)
        self.menuArchivo.addAction(self.accionGuardar)
        self.menuArchivo.addAction(self.accionSalir)

        self.menuEditar.addAction(self.accionDeshacer)
        self.menuEditar.addAction(self.acccionRehacer)
        self.menuEditar.addAction(self.accionCopiar)
        self.menuEditar.addAction(self.accionCortar)
        self.menuEditar.addAction(self.accionPegar)
        self.menuEditar.addAction(self.accionBuscarReemplazar)

        self.addAction(self.accionLetraNegrita)
        self.addAction(self.accionLetraCursiva)
        self.addAction(self.accionLetraColorFondo)
        self.addAction(self.accionTipoLetra)

    def nuevoArchivo(self):
        self.texto.clear()
        self.nombreArchivo = None

    def abrirArchivo(self):
        ruta = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt);;Archivos html (*.html);;Todos los archivos (*)")
        self.nombreArchivo = ruta[0] # Guarda el nombre del archivo abierto
        
        if ruta:
            try:
                with open(ruta[0], "r", encoding="utf-8") as archivo: # Se le pasa ruta[0] porque getOpenFileName devuelve una tupla
                    contenido = archivo.read()
                    if self.nombreArchivo.lower().endswith(".txt"): # Comprobar si es .txt o html (ignorando si .TXT es mayúscula)
                        self.texto.setPlainText(contenido)
                    else:
                        self.texto.setHtml(contenido)
            except Exception as e:
                print(f"No se pudo abrir el archivo: {e}")

    def guardarArchivo(self):
        # Si está vacío o es none, se le asigna el nombre predeterminado
        if not getattr(self, 'nombreArchivo', None):
            self.nombreArchivo = "Sin título 1.txt"

        ruta = QFileDialog.getSaveFileName(self, "Guardar archivo", self.nombreArchivo, "Archivos de texto (*.txt);;Archivos html (*.html);;Todos los archivos (*)")

        if ruta:
            try:
                with open(ruta[0], "w", encoding="utf-8") as archivo:
                    if self.nombreArchivo.lower().endswith(".txt"): # Comprobar si es .txt o html (ignorando si .TXT es mayúscula)
                        archivo.write(self.texto.toPlainText())
                    else:
                        archivo.write(self.texto.toHtml())
            except Exception as e:
                print(f"No se pudo guardar el archivo: {e}")

    def salirAplicacion(self):
        self.close()

    def deshacerAccion(self):
        self.texto.undo()

    def rehacerAccion(self):
        self.texto.redo()

    def copiarTexto(self):
        self.texto.copy()

    def cortarTexto(self):
        self.texto.cut()

    def pegarTexto(self):
        self.texto.paste()    

    def menuBuscarReemplazar(self):

        if (self.contenedorDock.isVisible() == False):

            self.contenedorDock.setVisible(True)
            self.textoBuscarPalabra.setFocus()

        else:
           
           self.contenedorDock.setVisible(False)
           self.texto.setExtraSelections([])
           self.statusBarMessage()

    def cambioVisibilidadDock(self, visible):
        if not visible:
            self.texto.setExtraSelections([])
            self.statusBarMessage()

    def resaltarPalabras(self, palabra):

        selecciones = []
        documento = self.texto.document()
        cursor = QTextCursor(documento)
        color = QColor(255, 255, 0, 80)
        self.contadorCoincidencias = 0
        
        while True:
            cursor = documento.find(palabra, cursor)
            if cursor.isNull():
                break
                
            seleccion = QTextEdit.ExtraSelection()
            seleccion.cursor = cursor
            formato = QTextCharFormat()
            formato.setBackground(color)
            seleccion.format = formato
            selecciones.append(seleccion)
            self.contadorCoincidencias += 1

        self.barraEstado.showMessage(f"{self.contadorCoincidencias} coincidencias encontradas")
        
        self.texto.setExtraSelections(selecciones)

    def resaltarCursor(self, cursor):
        
        # Resalta temporalmente la palabra que coincide sin modificar el documento, es decir,
        # si ponemos un background a una palabra, y buscamos esa palabra, no se reescribirá el fondo,
        # sino que será un fondo temporal que Qt dibujará por encima del QTextEdit usando ExtraSelection.
        palabraSelec = QTextEdit.ExtraSelection()
        palabraSelec.cursor = cursor
        color = Qt.gray

        formato = QTextCharFormat() 
        formato.setBackground(color)
        palabraSelec.format = formato

        selecciones = self.texto.extraSelections()

        nuevasSelecciones = []
        for seleccion in selecciones:
            colorFondo = seleccion.format.background().color()
            if colorFondo != color:  # Si no es gris se mantiene
                nuevasSelecciones.append(seleccion)

        selecciones = nuevasSelecciones

        selecciones.append(palabraSelec)

        self.texto.setExtraSelections(selecciones)

    def buscarTodasPalabras(self):

        self.resaltarPalabras(self.palabra)

    def buscarPalabra(self):

        self.texto.setExtraSelections([])
        self.statusBarMessage()
    
        buscarPalabra = self.textoBuscarPalabra.text().strip() # Palabra a buscar sin espacios

        if not buscarPalabra:
            self.texto.setExtraSelections([])

        self.palabra = buscarPalabra # Guardar la palabra para buscarSiguientePalabra o buscarAnteriorPalabra

        # Buscar primera palabra desde el principio
        documento = self.texto.document()
        cursor = documento.find(buscarPalabra, 0)

        if cursor.isNull(): # Si no coincide limpiar resaltados
            self.texto.setExtraSelections([])

        self.resaltarCursor(cursor)        # Pinta fondo con ExtraSelection
        self.texto.setTextCursor(cursor)   # Mover vista a la palabra encontrada

    def buscarSiguientePalabra(self):

        documento = self.texto.document()
        inicio = self.texto.textCursor()

        cursor = documento.find(self.palabra, inicio)

        if cursor.isNull():
            cursor = documento.find(self.palabra, 0)

        if not cursor.isNull():
            self.resaltarCursor(cursor)
            #cursor.clearSelection()            # Quita la selección azul de windows
            self.texto.setTextCursor(cursor) 

    def buscarAnteriorPalabra(self):

        documento = self.texto.document()
        inicio = self.texto.textCursor()

        cursor = documento.find(self.palabra, inicio, QTextDocument.FindBackward)

        if cursor.isNull():
            cursorFinal = QTextCursor(documento)
            cursorFinal.movePosition(QTextCursor.End)
            cursor = documento.find(self.palabra, cursorFinal, QTextDocument.FindBackward)

        if not cursor.isNull():
            self.resaltarCursor(cursor)
            self.texto.setTextCursor(cursor)

    def reemplazarPalabra(self):

        cursor = self.texto.textCursor()

        if cursor.hasSelection() and cursor.selectedText() == self.palabra:
            cursor.insertText(self.textoReemplazarPalabra.text())
            self.texto.setTextCursor(cursor)
            self.buscarSiguientePalabra()        

    def reemplazarTodasPalabras(self):

        textoCompleto = self.texto.toPlainText()
        textoModificado = textoCompleto.replace(self.palabra, self.textoReemplazarPalabra.text())
        self.texto.setPlainText(textoModificado)

    def statusBar(self):

        self.barraEstado = QStatusBar()
        self.setStatusBar(self.barraEstado)

    def statusBarMessage(self):

        palabra = self.texto.toPlainText().split()
        numPalabras = len(palabra)
        numCaracteres = len(self.texto.toPlainText())

        self.barraEstado.showMessage(str(numPalabras) + " palabras, " + str(numCaracteres) + " caracteres") 

if __name__ == "__main__":
    app = QApplication([])
    ventana = Ventana()
    ventana.showMaximized()
    app.exec()        