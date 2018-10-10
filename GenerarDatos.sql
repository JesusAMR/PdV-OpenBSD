--Familia de Articulos
INSERT INTO FamiliadeArticulos (Nombre, Marca, Modelo)
VALUES ('Vestimenta Elegenate' ,'Gucci','Gang');
INSERT INTO FamiliadeArticulos (Nombre, Marca, Modelo)
VALUES ('Vestimenta S' ,'Elegancia de','Francia');

--Almacenes
INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('C3', 'Niños');
INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('C1', 'Adultos');
INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('B1', 'Damas');
INSERT INTO Almacenes (AlmacenID, NombreAlmacen) VALUES ('B2', 'Masculino');

--Articulos
INSERT INTO Articulos (ArticuloID, UbicacionID, FamiliaID, Nombre, Costo, Cantidad, Maximo, Minimo)
VALUES (4521, 'C1', 1, 'Camisa', 500.20, 100, 100, 20);

INSERT INTO Articulos (ArticuloID, UbicacionID, FamiliaID, Nombre, Costo, Cantidad, Maximo, Minimo)
VALUES (4522, 'C1', 1, 'Sueter', 300.0, 80, 100, 20);

--Proveedores
INSERT INTO Proveedor (Nombre) VALUES ('Sonny Javier');
INSERT INTO Proveedor (Nombre) VALUES ('Rebbeca Ozuna');
INSERT INTO Proveedor (Nombre) VALUES ('Luis Mario García');
INSERT INTO Proveedor (Nombre) VALUES ('Pablo Quiroz');

--Proveedores Artiuclos
INSERT INTO ProveedorArt (ProveedorID, ArticuloID) VALUES (1, 4521);
INSERT INTO ProveedorArt (ProveedorID, ArticuloID) VALUES (2, 4521);
INSERT INTO ProveedorArt (ProveedorID, ArticuloID) VALUES (3, 4522);
INSERT INTO ProveedorArt (ProveedorID, ArticuloID) VALUES (4, 4522);
--INSERT INTO Proveedor (Nombre, ArticuloID) VALUES ('Sonny Javier', 4521);
--INSERT INTO Proveedor (Nombre, ArticuloID) VALUES ('Rebbeca Ozuna', 4521);
--INSERT INTO Proveedor (Nombre, ArticuloID) VALUES ('Luis Mario García', 4522);
--INSERT INTO Proveedor (Nombre, ArticuloID) VALUES ('Pablo Quiroz', 4522);

