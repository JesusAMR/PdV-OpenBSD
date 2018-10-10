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
        conn.commit()
        return existen

def imprimirListaFilas(lista, encabezadoDefault = ""):
    print(encabezadoDefault, end = "")
    for fila in lista:
        print("|", end = " ")
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
        Nombre = input('Ingrese el nombre del articulo: ')
        ##############################
        while(x == True):
            Familia = input('Ingrese la familia ')
            c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + Familia +"' ")
            for row in c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + Familia +"' "):
                # if row not in c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + Familia +"' "):
                #     print ("No existe la familia ingresada. Consulte el manual para mas informacion")
                if row in c.execute("SELECT FamiliaID FROM FamiliadeArticulos WHERE FamiliaID= '" + Familia +"' "):
                    x = False
        ###########################
        costo = input('Ingrese el costo del articulo: ')
        ############################## CANTIDAD
        cantidad  = input('Ingrese la cantidad de articulos')
        ############################## MaXIMO
        x = True
        while(x == True):
            max = int(input('Ingrese el max de articulos: '))
            if max == '' or max < 5 or max > 100000 :
                print ("La cantidad ingresada no esta permitida")
            else:
                x = False
                break
        ############################## MINIMO
        x = True
        while(x == True):
            min = int(input('Ingrese el minimo de articulos: '))
            if min < max and min > 1:
                x = False
            else:
                print("No se puede ingresar esa cantidad")
        ##############################
        x = True
        while(x == True):
            listaFilas = Inventario().mostrarUbicacion()
            ubicacionID = input('Ingrese el ID de la ubicacion')
            for fila in listaFilas:
                if ubicacionID == fila[0]:
                    x = False
            if not x:
                print("Identificador incorrecto")
        ##############################

        c.execute("INSERT INTO Articulos(UbicacionID, FamiliaID, Nombre, Costo, Cantidad, Maximo, Minimo) values (?, ?, '" + Nombre + "' , '" + costo + "' , '" + cantidad + "'  , ? , ?)", (ubicacionID, Familia, max, min))
        conn.commit()
        #print (list(c.execute("SELECT * FROM Articulos")))
        input()

    def eliminarRegistro(self):
        x = True
        y = True
        while(x == True):
            artID = input("Ingrese el ID a eliminar\n¿No recuerda el ID? Ingrese '?' para mostrar todos los registros.\nSu opcion: ")
            if artID == '?':
                print("Tabla Articulos")
                for row in c.execute('SELECT * FROM Articulos WHERE Estado = 0'):
                    print (row)

            c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + artID +"' ")
            for row in c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + artID +"' "):
                if row in c.execute("SELECT ArticuloID FROM Articulos WHERE ArticuloID= '" + artID +"' "):
                    c.execute("UPDATE Articulos SET Estado = 1 WHERE ArticuloID = %s" % (artID))
                    x = False
                input()
        conn.commit()

    def actualizarRegistro(self):
        x = True
        self.encabezado             = "Articulos\n|ID del Articulo | Nombre | Marca | Modelo | Ubicacion | Costo | Cantidad | Maximo | Minimo|\n"
        self.consultaArt            = "SELECT * FROM Articulos WHERE ArticuloID = %s"
        self.actualizacionCompuesta = "UPDATE Articulos SET %s = %s WHERE ArticuloID = %s"
        self.consultaDefault        = """ SELECT a.ArticuloID,
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
            ORDER BY a.ArticuloID
            """
        while(x == True):
            artID = input("Ingrese el ID a actualizar\n¿No recuerda el ID? Ingrese '?' para mostrar todos los registros.\nSu opcion: ")
            if artID == '?':
                listaFilas = ejecutarQuery(self.consultaDefault)
                if not listaFilas:
                    print ("Primero ingrese o active algun articulo")
                    return
                imprimirListaFilas(listaFilas, self.encabezado)
            else:
                listaFilas = ejecutarQuery(self.consultaArt % (int(artID)))
                if not listaFilas:
                    print ("Ingrese un identificador correcto")
                    continue
                for fila in listaFilas:
                    if int(artID) == fila[0]:
                        articulo = int(artID)
                        x = False
        x = True
        columna = ""
        while(x == True):
            opcion = int(input("""Ingrese el numero de la opcion que desea modificar
            1)Nombre
            2)Costo
            3)Cantidad
            4)Maximo
            5)Minimo
            6)Estado
            7)Ubicacion
                """))
            if opcion == 1:
                columna = "Nombre"
            if opcion == 2:
                columna = "Costo"
            if opcion == 3:
                columna = "Cantidad"
            if opcion == 4:
                columna = "Maximo"
            if opcion == 5:
                columna = "Minimo"
            if opcion == 6:
                columna = "Estado"
            if opcion == 7:
                columna = "Ubicacion"
            if len(columna) == 0:
                print("Ingrese un valor correcto")
                continue
            x = False
        x = True
        valor = input("Ingrese el nuevo valor de la columna " + columna + " : ")
        if opcion != 1:
            valor = int(valor)
        else:
            valor = "'" + valor + "'"
        listaFilas = ejecutarQuery(self.actualizacionCompuesta % (columna, valor, articulo))

class InsertarProveedor:
    def __init__(self):
        #self.proveedorID = ""
        self.proveedorDescripcion = ""
        self.eliminadoB = ""

    def llenarDatosProveedor(self):
        provdesc = input('Ingrese la descricion del proveedor')
        elimB = input('¿Que carajos es esto? No se, ingresa algo')
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
        consulta = "SELECT FamiliaID, Nombre FROM FamiliadeArticulos"
        encabezado = "|Identificador | Nombre|\n"
        lista = ejecutarQuery(consulta)
        imprimirListaFilas(lista, encabezado)

    def mostarProveedores(self):
        consulta = "SELECT ProveedorID, Nombre FROM Proveedor WHERE Estado = 0"
        encabezado = "|Identificador | Nombre|\n"
        lista = ejecutarQuery(consulta)
        imprimirListaFilas(lista, encabezado)

    def mostrarUbicacionArticulo(self, articuloID):
        consulta = "SELECT al.AlmacenID, al.Nombre, a.Nombre FROM Almacenes al INNER JOIN Articulos a ON a.ArticuloID = al.ArticuloID AND a.ArticulosID = %s WHERE al.Estado = 0"
        encabezado = "|Identificador Almacen | Nombre Almacen | Nombre Articulo|\n"
        lista = ejecutarQuery(consulta)
        imprimirListaFilas(lista, encabezado)
    
    def mostrarUbicacion(self, articuloID):
        consulta = "SELECT AlmacenID, Nombre FROM Almacenes WHERE Estado = 0"
        encabezado = "|Identificador | Nombre|\n"
        lista = ejecutarQuery(consulta)
        imprimirListaFilas(lista, encabezado)
        return lista


class Pedidos:
    def __init__(self):
        self.ProveedorID = ""
        self.Nombre = ""
        self.ArticuloID = ""
        self.encabezado = "|ID del Articulo | Nombre | Marca | Modelo | Ubicacion | Costo | Cantidad | Maximo | Minimo|\n"
        self.consultaDefault = """ SELECT a.ArticuloID,
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
            ORDER BY a.ArticuloID
            """

    def pedidoProovedor(self):
        x = True
        consultaArt     =   "SELECT * FROM Articulos WHERE ArticuloID = %s"
        consultaProvArt =   "SELECT p.ProveedorID, p.Nombre FROM Articulos a INNER JOIN Proveedor p ON p.ArticuloID =  a.ArticuloID WHERE p.ArticuloID = %s"
        actualizarArt   =   "UPDATE Articulos SET Cantidad = %s WHERE ArticuloID = %s"
        consultaCantMax =   "SELECT ArticuloID, Cantidad, Maximo, Minimo FROM Articulos WHERE ArticuloID= %s "
        while (x == True ):
            pedido = input("Introduzca el ID del articulo al que desea hacer pedido\nSi no recuerda los datos introduzca ? para verlos\nSu opcion: ")
            if pedido == '?':
                if Consulta().mostrar():
                    return
            else:
                listaFilas = ejecutarQuery(consultaArt % (pedido))
                if not listaFilas:
                    print ("Ingrese un identificador correcto")
                    continue
                for fila in listaFilas:
                    if int(pedido) == fila[0]:
                        articulo = int(pedido)
                        x = False
        x = True
        while (x == True ):
            vendor = input("Seleccione el proveedor: \nSi no conoce a los proveedores pulse ? para verlos.\nSu opcion: ")
            if vendor == '?':
                listaFilas = ejecutarQuery(consultaProvArt % (articulo))
                if not listaFilas:
                    return
                imprimirListaFilas(listaFilas)
            else:
                listaFilas = ejecutarQuery(consultaProvArt % (articulo))
                if not listaFilas:
                    print  ("Ingrese un identificador correcto")
                    continue
                for fila in listaFilas:
                    if int(vendor) == fila[0]:
                        proveedor = int(vendor)
                        x = False
        x = True
        while(x == True):
            listaFilas = ejecutarQuery(consultaCantMax % (articulo))
            imprimirListaFilas(listaFilas, "| Articulo | Cantidad | Maximo | Minimo |\n")
            cantidadDef =   int(listaFilas[0][1])
            maximo      =   int(listaFilas[0][2])
            minimo      =   int(listaFilas[0][3])
            cantidad    =   int(input ("Ahora introduzca la cantidad de articulos que desea pedir: "))
            if not self.validarCantidad(cantidad, cantidadDef, maximo, minimo):
                print ("Vuelva a ingresar la cantidad")
                continue
            listaFilas  =   ejecutarQuery(actualizarArt % (cantidadDef + cantidad, articulo))
            print("Se ha realizado el pedido al proveedor")
            x = False
    
    def validarCantidad(self, cant, cantdef, maximo, minimo):
        if(cant > maximo):
            return False
        elif(cant + cantdef < minimo):
            print("Su cantidad insertada no cumple el minimo del articulo")
            return False
        elif(cant + cantdef > maximo):
            print("Su cantidad insertada sobrepasa el maximo del articulo")
            return False
        else:
            return True

class Consulta:
    def __init__(self):
        self.encabezado = "|ID del Articulo | Nombre | Marca | Modelo | Ubicacion | Costo | Cantidad | Maximo | Minimo|\n"
        self.encabezadoProveedor = "|ID del Articulo | Nombre | Nombre Proveedor | Marca | Modelo | Ubicacion | Costo | Cantidad | Maximo | Minimo|\n"
        self.consultaDefault = """ SELECT a.ArticuloID,
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
            ORDER BY a.ArticuloID
            """
        self.consultaFamilia = """ SELECT a.ArticuloID,
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
            ORDER BY a.ArticuloID, fa.Nombre
                """
        self.consultaProveedor = """ SELECT a.ArticuloID,
            a.Nombre,
            p.Nombre,
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
            INNER JOIN Proveedor p
                ON p.ArticuloID = a.ArticuloID
                AND p.ProveedorID = %s
            WHERE a.Estado = 0
            ORDER BY a.ArticuloID, p.Nombre
                """
    
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
            opc = int(input("Ingrese una opcion: "))
            if opc == 1:
                Inventario().mostarFamilia()
                familiaID = int(input("Ingrese el identificador de la familia por la cual desea filtrar: "))
                os.system("clear")
                listaFilas = ejecutarQuery(self.consultaFamilia % (familiaID))
                if not listaFilas:
                    print("No hay articulos con esa familia")
                else:
                    imprimirListaFilas(listaFilas, self.encabezado)
                input()
            elif opc == 2:
                Inventario().mostarProveedores()
                proveedorID = int(input("Ingrese el identificador del proveedor por el cual desea filtrar: "))
                os.system("clear")
                listaFilas = ejecutarQuery(self.consultaProveedor % (proveedorID))
                if not listaFilas:
                    print("No hay articulos con ese proveedor")
                else:
                    imprimirListaFilas(listaFilas, self.encabezado)
                input()
            elif opc == 3:
                self.mostrar()
                input()
            elif opc == 4:
                x = False

    def mostrar(self):
        print("Inventario")
        listaFilas = ejecutarQuery(self.consultaDefault)
        if not listaFilas:
            print("No hay datos en el inventario")
            input()
            return False
        imprimirListaFilas(listaFilas, self.encabezado)

class Ordenes:
    def __init__(self):
        self.consultaActualizar = "UPDATE Articulos SET Cantidad = %s WHERE ArticuloID = %s"

    def buscarOrdenes(self):
        consulta = "SELECT * FROM Articulos WHERE Cantidad < Minimo AND Estado = 0"
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
        encabezado = "|ID del Articulo | Nombre | Costo | Cantidad | Maximo | Minimo|\n"
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

    def reabastecerArticulos(self, pendientes):
        articuloID = int(input("Ingrese el identificador del articulo al cual se desea reabastecer hasta el tope: "))
        cantidad = 0
        for pendiente in pendientes:
            if articuloID == pendiente[0]:
                cantidad = pendiente[2]
        listaFilas = ejecutarQuery(self.consultaActualizar % (cantidad, articuloID))
        print (listaFilas)
        input()

    def mostrar(self):
        print("Ordenes por realizar:")
        ordenes = self.buscarOrdenes()
        if not ordenes:
            return
        pendientes = self.consultarOrdenes(ordenes)
        self.reabastecerArticulos(pendientes)
