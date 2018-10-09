import sqlite3
conn = sqlite3.connect('proyecto.db')
c = conn.cursor()

class SQL:
    #Creamos la bd
    def __init__(self):
        self.tablas = [
            """
            CREATE TABLE Articulos(
                ArticuloID  INTEGER PRIMARY KEY,
                Nombre varchar(30),
                Familia INTEGER,
                Costo FLOAT,
                Cantidad INT NOT NULL,
                Maximo INT NOT NULL,
                Minimo INT NOT NULL,
                UbicacionID INT NOT NULL
            );
            """,
            """
            CREATE TABLE Proveedor(
                ProveedorID INTEGER PRIMARY KEY,
                Nombre varchar(30),
                ArticuloID  INTEGER
            );
            """,
             """
             CREATE TABLE FamiliadeArticulos(
                FamiliaID INTEGER PRIMARY KEY,
                Marca varchar(30),
                Modelo varchar(30)
             );
             """,
             """
             CREATE TABLE Almacenes(
                AlmacenID varchar(2),
                NombreAlmacen varchar(30)
             );
             """
        ]
    def executeQuery(self, query):
        c.execute(query)

    def crearTabla(self):
        for table in self.tablas:
            self.executeQuery(table);
x = SQL()
x.crearTabla()

## Insertamos una fila
# c.execute("INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('C3', 'Niños')")
# c.execute("INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('C1', 'Adultos')")
# c.execute("INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('B1', 'Damas')")
# c.execute("INSERT INTO Proveedor (Nombre) VALUES ('Sonny Javier')")
# c.execute("INSERT INTO Proveedor (Nombre) VALUES ('Rebbeca Ozuna')")
# c.execute("INSERT INTO Proveedor (Nombre) VALUES ('Luis Mario García')")
# c.execute("INSERT INTO Proveedor (Nombre) VALUES ('Pablo Quiroz')")






# Save (commit) the changes
conn.commit()
#print (list(c.execute("SELECT * FROM TablaArticulos")))
conn.close()
