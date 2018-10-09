--Familia de Articulos
INSERT INTO FamiliadeArticulos (Nombre, Marca, Modelo)
VALUES ('Vestimenta Elegenate' ,'Gucci','Gang');
INSERT INTO FamiliadeArticulos (Familia, Marca, Modelo)
VALUES ('Vestimenta S' ,'Elegancia de','Francia');

--Almacenes
INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('C3', 'Niños');
INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('C1', 'Adultos');
INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('B1', 'Damas');

--Articulos
INSERT INTO Articulos (ArticuloID, UbicacionID, FamiliaID, Nombre, Costo, Cantidad, Maximo, Minimo)
VALUES (4521, 'C1', 1, 'TEST', 500.20, 100, 100, 20);

INSERT INTO Articulos (UbicacionID, FamiliaID, Nombre, Costo, Cantidad, Maximo, Minimo)
VALUES ('C1', 1, 'Sueter', 300.0, 80, 100, 20);

--Proveedores
INSERT INTO Proveedor (Nombre, ArticuloID) VALUES ('Sonny Javier', 4521);
INSERT INTO Proveedor (Nombre, ArticuloID) VALUES ('Rebbeca Ozuna', 4521);
INSERT INTO Proveedor (Nombre, ArticuloID) VALUES ('Luis Mario García', 4521);
INSERT INTO Proveedor (Nombre, ArticuloID) VALUES ('Pablo Quiroz', 4521);
