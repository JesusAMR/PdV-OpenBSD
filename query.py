#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sqlite3
conn = sqlite3.connect('proyect.db')
c = conn.cursor()

cant_solitar = 0


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
    def mostrar(self):
        print("Tabla Artículos")

        #Poner columna por columna
        for row in c.execute('SELECT * from Articulos'):
            print (row)

class Ordenes:
    def buscarOrdenes(self):
        # where Cantidad <= Minimo
        c.execute('select * from Articulos')
        existen = c.fetchall()
        #Regresa falso si no hay ordenes que pedir, si no, regresa el arreglo de listas de articulos que requieren ordenes
        if not existen:
            print ("No hay ordenes que pedir")
            input()
            return False
        else:
            return existen

    def realizarOrdenes(self, lista):
        ordenes = {}
        for row in lista:
            print (row)
            #0 es ArticuloID, 5 es Cantidad, 6 es Maximo 
            ordenes[row[0]] = row[6] - row[5]
        print (ordenes)

    def mostrar(self):
        print("Ordenes por realizar:")
        ordenes = self.buscarOrdenes()
        if not ordenes:
            return
        self.realizarOrdenes(ordenes)
        input()


#Region "Maneras de recorrer una consulta BETA "
        # query = c.execute("SELECT * FROM Articulos")
        # print (query.fetchone())
        # print (query.fetchone())
        # print (query.fetchone())
        # print (query.fetchone())
        # print (query.fetchone())
        # print (query.fetchone())
        # print (query.fetchone())
        # print (query.fetchone())
        # print (query.fetchone())
        # for celda in query.fetchall():
        #     print u"Artículo ID: %d, Modelo ID: %d,Artículo ID: %d,Artículo ID: %d,Artículo ID: %d,Artículo ID: %d,Artículo ID: %d" % (celda[0], celda[1],celda[2],celda[3],celda[4],celda[5],celda[6])
        #print (list(c.execute("SELECT * FROM Articulos")))
        # conn.commit()
#end region
