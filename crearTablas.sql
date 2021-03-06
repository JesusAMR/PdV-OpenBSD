CREATE TABLE FamiliadeArticulos
(
    FamiliaID INTEGER PRIMARY KEY,
    Nombre VARCHAR(30),
    Marca VARCHAR(30),
    Modelo VARCHAR(30)
);

CREATE TABLE Almacenes
(
    AlmacenID VARCHAR(2),
    NombreAlmacen VARCHAR(30),
    Estado INTEGER DEFAULT 0
);

CREATE TABLE Articulos
(
    ArticuloID INTEGER PRIMARY KEY,
    UbicacionID INTEGER,
    FamiliaID INTEGER,
    Nombre VARCHAR(30),
    Costo FLOAT,
    Cantidad INTEGER NOT NULL,
    Maximo INTEGER NOT NULL,
    Minimo INTEGER NOT NULL,
    Estado INTEGER DEFAULT 0,
    FOREIGN KEY(UbicacionID) REFERENCES Almacenes(AlmacenID),
    FOREIGN KEY (FamiliaID) REFERENCES FamiliadeArticulos(FamiliaID)
);

CREATE TABLE Proveedor
(
    ProveedorID INTEGER PRIMARY KEY,
    Nombre VARCHAR(30),
    Estado INTEGER DEFAULT 0
);

CREATE TABLE ProveedorArt
(
    ProvArtID INTEGER PRIMARY KEY,
    ProveedorID INTEGER,
    ArticuloID INTEGER,
    Estado INTEGER DEFAULT 0,
    FOREIGN KEY(ProveedorID) REFERENCES Proveedor(ProveedorID),
    FOREIGN KEY(ArticuloID) REFERENCES Articulos(ArticuloID)
);

CREATE TABLE Orden
(
    OrdenID INTEGER PRIMARY KEY,
    ArticuloID INTEGER,
    ProveedorID INTEGER,
    Cantidad INTEGER NOT NULL,
    FOREIGN KEY(ArticuloID) REFERENCES Articulos(ArticuloID),
    FOREIGN KEY(ProveedorID) REFERENCES Proveedor(ProveedorID)
);