from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from controlador import VendedorController

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Ventas")
        self.setGeometry(100, 100, 400, 500)

        self.controlador = VendedorController()

        layout = QVBoxLayout()

        self.nombre_input = QLineEdit(placeholderText="Nombre del vendedor")
        self.area_input = QLineEdit(placeholderText="Área de trabajo")
        self.sueldo_input = QLineEdit(placeholderText="Sueldo básico")
        self.articulo_input = QLineEdit(placeholderText="Artículo vendido")
        self.precio_input = QLineEdit(placeholderText="Precio del artículo")

        self.registrar_btn = QPushButton("Registrar Venta")
        self.registrar_btn.clicked.connect(self.registrar_venta)

        self.resultados = QTextEdit()
        self.resultados.setReadOnly(True)

        layout.addWidget(self.nombre_input)
        layout.addWidget(self.area_input)
        layout.addWidget(self.sueldo_input)
        layout.addWidget(self.articulo_input)
        layout.addWidget(self.precio_input)
        layout.addWidget(self.registrar_btn)
        layout.addWidget(self.resultados)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def registrar_venta(self):
        nombre = self.nombre_input.text()
        area = self.area_input.text()
        sueldo = float(self.sueldo_input.text())
        articulo = self.articulo_input.text()
        precio = float(self.precio_input.text())

        self.controlador.registrar_venta(nombre, area, sueldo, articulo, precio)
        self.actualizar_resultados()

    def actualizar_resultados(self):
        ventas = self.controlador.obtener_todas_las_ventas()
        self.resultados.clear()
        for venta in ventas:
            self.resultados.append(f"Venta: {venta}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
