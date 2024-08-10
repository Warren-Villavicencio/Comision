import sqlite3

class VendedorModel:
    def __init__(self):
        self.conn = sqlite3.connect('ventas.db')
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ventas
                            (id INTEGER PRIMARY KEY,
                             nombre_vendedor TEXT,
                             area_trabajo TEXT,
                             sueldo_basico REAL,
                             articulo TEXT,
                             precio_articulo REAL,
                             comision REAL,
                             total_ganancias REAL)''')
        self.conn.commit()

    def agregar_venta(self, nombre, area, sueldo, articulo, precio):
        comision = precio * 0.1
        total = sueldo + comision
        self.cursor.execute('''INSERT INTO ventas 
                            (nombre_vendedor, area_trabajo, sueldo_basico, articulo, precio_articulo, comision, total_ganancias) 
                            VALUES (?, ?, ?, ?, ?, ?, ?)''',
                            (nombre, area, sueldo, articulo, precio, comision, total))
        self.conn.commit()

    def obtener_ventas(self):
        self.cursor.execute("SELECT * FROM ventas")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()
