CREATE TABLE Articulos
(
    ArticuloID  INTEGER PRIMARY KEY,
    Nombre varchar(30),
    Familia INTEGER,
    Costo FLOAT,
    Cantidad INT NOT NULL,
    Maximo INT NOT NULL,
    Minimo INT NOT NULL,
    UbicacionID INT NOT NULL
);

CREATE TABLE Proveedor(
    ProveedorID INTEGER PRIMARY KEY,
    Nombre varchar(30),
    ArticuloID  INTEGER
);

CREATE TABLE FamiliadeArticulos(
    FamiliaID INTEGER PRIMARY KEY,
    Marca varchar(30),
    Modelo varchar(30)
);

CREATE TABLE Almacenes(
    AlmacenID varchar(2),
    NombreAlmacen varchar(30)
);