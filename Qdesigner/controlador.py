from modelo import VendedorModel

class VendedorController:
    def __init__(self):
        self.modelo = VendedorModel()

    def registrar_venta(self, nombre, area, sueldo, articulo, precio):
        self.modelo.agregar_venta(nombre, area, sueldo, articulo, precio)

    def obtener_todas_las_ventas(self):
        return self.modelo.obtener_ventas()