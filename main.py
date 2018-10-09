import base
import os
import query

x = True
while(x == True):
    os.system("cls")
    print ("""Menú del proyecto xd
        1.- Dar de alta. Baka, Actualizar
        2.- Hacer pedidos xD
        3.- Hacer consulta
        """)

    opc=int(input("Ingrese una opción: "))
    if opc == 1:
        Articulos = query.InsertarArticulos()
        opc1 =int(input("""¿Desea dar de alta, eliminar o actualizar?
                        1.- Dar de alta
                        2.- Eliminar registro
                        3.- Actualizar
                        4.- Salir
                        """))
        if opc1 == 1:
            Articulos.llenarDatosArticulos()
        if opc1 == 2:
            Articulos.eliminarRegistro()
        if opc1 == 3:
            Articulos.actualizarRegistro()
    if opc==2:
        Proveedor = query.Pedidos()
        Proveedor.pedidoProovedor()
    if opc==3:
        Consulta = query.Consulta()
        Consulta.mostrar()
