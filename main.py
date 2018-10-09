import os
import query

x = True
while(x == True):
    os.system("clear")
    Ordenes = query.Ordenes().mostrarOrdenes()
    if Ordenes:
        "Hay ordenes que realizar, favor de consultarlas"
    print ("""Menú del proyecto
        1.- Dar de alta
        2.- Hacer pedidos
        3.- Hacer consulta
        4.- Ordenes
        5.- Salir
        """)
    opc = int(input("Ingrese una opción: "))
    if opc == 1:
        Articulos = query.InsertarArticulos()
        opc1 = int(input("""¿Desea dar de alta, eliminar o actualizar?
                        1.- Dar de alta
                        2.- Eliminar registro
                        3.- Actualizar
                        4.- Salir
                        """)
            )
        os.system("clear")
        if opc1 == 1:
            Articulos.llenarDatosArticulos()
        if opc1 == 2:
            Articulos.eliminarRegistro()
        if opc1 == 3:
            Articulos.actualizarRegistro()
    if opc == 2:
        Proveedor = query.Pedidos()
        Proveedor.pedidoProovedor()
    if opc == 3:
        Consulta = query.Consulta()
        Consulta.menu()
    if opc == 4:
        Ordenes = query.Ordenes()
        Ordenes.mostrar()
    if opc == 5:
        x = False
