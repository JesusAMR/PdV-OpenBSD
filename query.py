#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sqlite3
conn = sqlite3.connect('proyect.db')
c = conn.cursor()

cant_solitar = 0

def ejecutarQuery(consulta):
    c.execute(consulta)
    existen = c.fetchall()
    #Regresa falso si no hay ordenes que pedir, si no, regresa el arreglo de listas de articulos que requieren ordenes
    if not existen:
        return False
    else:
        return existen

def imprimirListaFilas(lista, encabezadoDefault = ""):
    print(encabezadoDefault, end = "")
    for fila in lista:
        for valor in fila:
            print(valor, end = " | ")
        print("")

class InsertarArticulos:
    
    def __init__(self):
        self.articuloID = ""
        self.Nombre = ""
        self.Costo = ""
        self.Cantidad = ""
        self.Maximo   = ""
        self.Minimo  = ""
        self.UbicacionID = ""

    def llenarDatosArticulos(self):
        x = True
        ##############################
        Nombre = input('Ingrese el nombre del artículo: ')
        ##############################
        while(x == True):
            Familia = input('Ingrese la familia ')
            c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + Familia +"' ")
            for row in c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + Familia +"' "):
                # if row not in c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + Familia +"' "):
                #     print ("No existe la familia ingresada. Consulte el manual para más información")
                if row in c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + Familia +"' "):
                    x = False
        ###########################
        costo = input('Ingrese el costo del artículo: ')
        ############################## CANTIDAD XD
        cantidad  = input('Ingrese la cantidad de artículos')
        ############################## MÁXIMO
        x = True
        while x==True:
            max = int(input('Ingrese el max de artículos: '))
            if max == '' or max < 5 or max > 100000 :
                print ("La cantidad ingresada no está permitida")
            else:
                x = False
                break
        ############################## MINIMO
        x = True
        while x==True:
            min = int(input('Ingrese el minimo de articulos: '))
            if min < max and min > 1:
                x = False
            else:
                print("No se puede ingresar esa cantidad")
        ##############################
        ubicacionID = input('Ingrese el ID de la ubicación')
        ##############################

        c.execute("INSERT INTO Articulos(UbicacionID, FamiliaID, Nombre, Costo, Cantidad, Maximo, Minimo) values (?, ?, '" + Nombre + "' , '" + costo + "' , '" + cantidad + "'  , ? , ?)", (ubicacionID, Familia, max, min))
        conn.commit()
        #print (list(c.execute("SELECT * FROM Articulos")))
        input()

    def eliminarRegistro(self):
        x = True
        y = True
        while(x == True):
            artID = input("Ingrese el ID a eliminar\n¿No recuerda el ID? Ingrese '?' para mostrar todos los registros.\nSu opción: ")
            if artID == '?':
                print("Tabla Artículos")
                for row in c.execute('SELECT * FROM Articulos WHERE Estado = 0'):
                    print (row)

            c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + artID +"' ")
            for row in c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + artID +"' "):
                if row in c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + artID +"' "):
                    c.execute("UPDATE Articulos SET Estado = 1 WHERE ArticuloID = '" + artID +"'")
                    x = False
                input()
        conn.commit()

    def actualizarRegistro(self):
        x = True
        while(x == True):
            artID = input("Ingrese el ID a actualizar\n¿No recuerda el ID? Ingrese '?' para mostrar todos los registros.\nSu opción: ")
            if artID == '?':
                print("Tabla Artículos")
                print("ID del Artículo | Nombre | Marca | Modelo | Costo | Cantidad | Máximo | Mínimo | Ubicación")
                for row in c.execute("""SELECT a.ArticuloID, a.Nombre, fa.Marca, fa.Modelo, a.Costo, a.Cantidad, a.Maximo, a.Minimo, alm.NombreAlmacen
                    FROM Articulos a
                    INNER JOIN FamiliadeArticulos fa
                        on fa.FamiliaID = a.FamiliaID
                    INNER JOIN Almacenes alm
                        on alm.AlmacenID = a.UbicacionID
                    WHERE a.Estado = 0"""):
                    for value in row:
                        print (value, end = "  |  ")
                input()

            var1 = input("Ingrese el nuevo nombre ")
            while(x == True):
                var2 = input("Ingrese la familia ")
                c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE Estado = 0 AND FamiliaID= '" + var2 +"' ")
                for row in c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + var2 +"' "):
                    # if row not in c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + Familia +"' "):
                    #     print ("No existe la familia ingresada. Consulte el manual para más información")
                    if row in c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + var2 +"' "):
                        x = False
            var3 = input("Ingrese el nuevo costo:  ")
            var4 = input("Ingrese la cantidad:  ")
            var5 = input("Ingrese la cantidad máxima:  ")
            var6  = input("Ingrese la cantidad minima:  ")
            var7  = input("Ingrese la ubicaciónID:  ")
            c.execute("UPDATE Articulos SET Nombre = '" + var1 +"', Familia= '" + var2 +"', Costo = '" + var3 +"', Cantidad = '" + var4 +"', Maximo = '" + var5 +"', Minimo= '" + var6 +"', UbicacionID = '" + var7 +"'   WHERE ArticuloID = '" + artID +"' ")
            # for row in c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + artID +"' "):
            #     if row in c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + artID +"' "):
            #         c.execute("DELETE FROM Articulos where ArticuloID = '" + artID +"'")
            #         x = False
            conn.commit()

class InsertarProveedor:
    def __init__(self):
        #self.proveedorID = ""
        self.proveedorDescripcion = ""
        self.eliminadoB = ""

    def llenarDatosProveedor(self):
        provdesc = input('Ingrese la descrición del proveedor')
        elimB = input('¿Qué carajos es esto? No sé, ingresa algo')
        c.execute("INSERT INTO TablaProveedor (proveedorDescripcion , eliminadoB) VALUES ('" + provdesc + "', '" + elimB + "')")
        conn.commit()
        input()

class InsertarFamiliaArticulos:
    def __init__(self):
        self.estado = ""
    def llenarDatosFamiliaArticulos(self):
        estado = input('Estado: ')
        c.execute("INSERT INTO FamiliaArticulos(estado) VALUES ('" + estado + "')")
        conn.commit()
        input()

class Inventario:
    def mostarFamilia(self):
        consulta = 'SELECT * FROM FamiliadeArticulos'
        encabezado = "Identificador | Nombre|\n"
        lista = ejecutarQuery(consulta)
        imprimirListaFilas(lista, encabezado)
    def mostrar(self):
        print("Tabla Artículos")
        for row in c.execute('SELECT * FROM Articulos'):
            print (row)
        print("Tabla Proveedor")
        for row in c.execute('SELECT * FROM TablaProveedor'):
            print (row)
        print("Tabla Proveedor Artículos")
        for row in c.execute('SELECT * FROM ProveedorArticulos'):
            print (row)
        print("Tabla Ubicación")
        for row in c.execute('SELECT * FROM Ubicacion'):
            print (row)
        print("Tabla Ubicación Artículo")
        for row in c.execute('SELECT * FROM UbicacionArticulo'):
            print (row)
        print("Tabla Familia")
        for row in c.execute('SELECT * FROM Familia'):
            print (row)
        print("Tabla Familia Artículos")
        for row in c.execute('SELECT * FROM FamiliaArticulos'):
            print (row)
        print("Tabla Marca")
        for row in c.execute('SELECT * FROM Marca'):
            print (row)
        print("Tabla Marca Artículo")
        for row in c.execute('SELECT * FROM MarcaArticulo'):
            print (row)
        #print("__________________________________________________")

class Pedidos:
    def __init__(self):
        self.ProveedorID = ""
        self.Nombre = ""
        self.ArticuloID = ""

    def pedidoProovedor(self):
        x = True
        while (x ==True ):
            pedido = input("Introduzca el ID del artículo al que desea hacer pedido\nSi no recuerda los datos introduzca ? para verlos xD")
            if pedido == '?':
                print("Tabla Artículos")
                print("ID del Artículo | Nombre | Familia | Costo | Cantidad | Máximo | Mínimo | Ubicación")
                for row in c.execute('SELECT * FROM Articulos'):
                    print (row)
                input()
        #c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + pedido +"' ")
            for row in c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + pedido +"' "):
                if row in c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + pedido +"' "):
                    x = False
        x = True
        while (x ==True ):
            vendor = input("Seleccione el proveedor: \nSi no conoce a los proveedores pulse ? para ver la tabla.\nSu opción: ")
            if vendor == '?':
                print("Tabla Proveedor")
                for row in c.execute('SELECT ProveedorID, Nombre FROM Proveedor'):
                    print (row)
                input()
            for row in c.execute("SELECT ProveedorID, Nombre FROM Proveedor WHERE ProveedorID ='" + vendor +"' "):
                if row in c.execute("SELECT ProveedorID, Nombre FROM Proveedor WHERE ProveedorID= '" + vendor +"' "):
                    x = False
        cantidad = input ("Ahora introduzca la cantidad de artículos que necesita para completar su máximo requerido")
        #c.execute("SELECT Cantidad, Maximo, Minimo FROM Articulos WHERE ArticuloID= '" + pedido +"' ")
        maxinissin = c.execute("SELECT  Maximo FROM Articulos WHERE ArticuloID= '" + pedido +"' ")
        print (list(maxinissin))
        print("Sigue en desarrollo...........................")
        # if (list(maxinissin)) > cantidad:
        #     print("Hola mundo"
        input()
        c.execute("UPDATE Cantidad = '" + cantidad +"'  FROM Articulos WHERE ArticuloID= '" + pedido +"' ")
        # if maxinissin > cantidad
        #     print ("No te pases de pendejo, ya viste las tablas y todavía quieres añadirle de más, no mames, deberían correte como proveedor.")

        #cant_solitar += cant_solitar

class Consulta:
    def __init__(self):
        self.encabezado = "ID del Artículo | Nombre | Marca | Modelo | Ubicación | Costo | Cantidad | Máximo | Mínimo|\n"
    def menu(self):
        x = True
        while(x == True):
            os.system("clear")
            print ("""¿Como desea filtrar los articulos?
                1.- Familia de articulos
                2.- Nombre de proveedor
                3.- Sin filtros
                4.- Salir
                """)
            opc = int(input("Ingrese una opción: "))
            if opc == 1:
                Inventario().mostarFamilia()
                familiadID = int(input("Ingrese el identificador de la familia por la cual desea filtrar: "))
                os.system("clear")
                consulta = """ SELECT a.ArticuloID,
                    a.Nombre,
                    fa.Marca,
                    fa.Modelo,
                    al.NombreAlmacen,
                    a.Costo,
                    a.Cantidad,
                    a.Maximo,
                    a.Minimo
                    FROM Articulos a
                    INNER JOIN Almacenes al
                        ON al.AlmacenID = a.UbicacionID
                    INNER JOIN FamiliadeArticulos fa
                        ON fa.FamiliaID = a.FamiliaID
                        AND fa.FamiliaID = %s
                    WHERE a.Estado = 0
                """ % (familiadID)
                listaFilas = ejecutarQuery(consulta)
                imprimirListaFilas(listaFilas, self.encabezado)
                input()
            elif opc == 4:
                x = False

    def mostrar(self):
        print("Inventario")
        
        #Poner columna por columna
        consulta = """ SELECT a.ArticuloID,
            a.Nombre,
            fa.Marca,
            fa.Modelo,
            al.NombreAlmacen,
            a.Costo,
            a.Cantidad,
            a.Maximo,
            a.Minimo
            FROM Articulos a
            INNER JOIN Almacenes al
                ON al.AlmacenID = a.UbicacionID
            INNER JOIN FamiliadeArticulos fa
                ON fa.FamiliaID = a.FamiliaID
            WHERE a.Estado = 0
        """
        listaFilas = ejecutarQuery(consulta)
        if not listaFilas:
            print("No hay datos en el inventario")
            input()
            return false
        imprimirListaFilas(listaFilas, encabezado)
        input()

class Ordenes:
    def buscarOrdenes(self):
        consulta = "SELECT * FROM Articulos WHERE Cantidad <= Minimo AND Estado = 0"
        existen = ejecutarQuery(consulta)
        #Regresa falso si no hay ordenes que pedir, si no, regresa el arreglo de listas de articulos que requieren ordenes
        if not existen:
            print ("No hay ordenes que pedir")
            input()
            return False
        else:
            return existen

    def consultarOrdenes(self, lista):
        ordenes = []
        encabezado = "|ID del Artículo | Nombre | Costo | Cantidad | Máximo | Mínimo|\n"
        for row in lista:
            #0 es ID del Articulo, 3 es Nombre, 5 es Cantidad y 6 es Maximo por lo tanto queda lo faltante para completar el max
            ordenes.append([row[0], row[3], row[6] - row[5]])
        for orden in ordenes:
            print("Identificador: " + str(orden[0]) + "\nNombre de Articulo: " + str(orden[1]) + "\nCantidad requerida: " + str(orden[2]) + "\n")
        return ordenes

    def mostrarOrdenes(self):
        print("Ordenes por realizar:")
        ordenes = self.buscarOrdenes()
        if not ordenes:
            return
        self.consultarOrdenes(ordenes)
        input()

    def mostrar(self):
        print("Ordenes por realizar:")
        ordenes = self.buscarOrdenes()
        if not ordenes:
            return
        pendientes = self.consultarOrdenes(ordenes)

        familiadID = int(input("Ingrese el identificador del articulo al cual se desea realizar reabastecer: "))
        consulta = """UPDATE Articulos
            a.Nombre,
            fa.Marca,
            fa.Modelo,
            al.NombreAlmacen,
            a.Costo,
            a.Cantidad,
            a.Maximo,
            a.Minimo
            FROM Articulos a
            INNER JOIN Almacenes al
                ON al.AlmacenID = a.UbicacionID
            INNER JOIN FamiliadeArticulos fa
                ON fa.FamiliaID = a.FamiliaID
                AND fa.FamiliaID = %s
            WHERE a.Estado = 0
        """ % (familiadID)
        listaFilas = ejecutarQuery(consulta)
        imprimirListaFilas(listaFilas, self.encabezado)
        input()

        input()
