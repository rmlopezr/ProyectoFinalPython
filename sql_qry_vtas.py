DDL_QUERY =  '''

CREATE TABLE IF NOT EXISTS categoria (
  idcategoria INT PRIMARY KEY,
  nombre VARCHAR(50),
  descripcion VARCHAR(100),
  estado boolean 
);

CREATE TABLE IF NOT EXISTS persona (
  idpersona INT PRIMARY KEY,
  tipo_persona VARCHAR(20),
  nombre VARCHAR(100),
  tipo_documento VARCHAR(20),
  num_documento VARCHAR(20),
  direccion VARCHAR(70),
  telefono VARCHAR(20),
  email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS rol (
  idrol INT PRIMARY KEY,
  nombre VARCHAR(30),
  descripcion VARCHAR(255),
  estado boolean
);

CREATE TABLE IF NOT EXISTS articulo (
  idarticulo INT PRIMARY KEY,
  idcategoria INT,
  codigo VARCHAR(50),
  nombre VARCHAR(100),
  precio_venta decimal(11,2),
  stock INT,
  descripcion VARCHAR(255),
  imagen VARCHAR(20),
  estado boolean,
  
  CONSTRAINT fk_categoria_articulo
    FOREIGN KEY (idcategoria)
        REFERENCES categoria(idcategoria)
);

CREATE TABLE IF NOT EXISTS usuario (
  idusuario INT PRIMARY KEY,
  idrol INT,
  nombre VARCHAR(100),
  tipo_documento VARCHAR(20),
  num_documento VARCHAR(20),
  direccion VARCHAR(70),
  telefono VARCHAR(20),
  email VARCHAR(50),
  clave VARCHAR(20),
  estado boolean,

  CONSTRAINT fk_rol_usuario
    FOREIGN KEY (idrol)
        REFERENCES rol(idrol)
);

CREATE TABLE IF NOT EXISTS ingreso (
  idingreso INT PRIMARY KEY,
  idproveedor INT,
  idusuario INT,
  tipo_comprobante VARCHAR(20),
  serie_comprobante VARCHAR(7),
  num_comprobante VARCHAR(10),
  fecha date,
  impuesto decimal(4,2),
  total decimal(11,2),
  estado VARCHAR(20),
  
  CONSTRAINT fk_persona_ingreso
    FOREIGN KEY (idproveedor)
        REFERENCES persona(idpersona),

  CONSTRAINT fk_usuario_ingreso
    FOREIGN KEY (idusuario)
        REFERENCES usuario(idusuario)
);

CREATE TABLE IF NOT EXISTS detalle_ingreso (
  iddetalle_ingreso INT PRIMARY KEY,
  idingreso INT,
  idarticulo INT,
  cantidad INT,
  precio_compra decimal(11,2),

  CONSTRAINT fk_articulo_detalle_ing
    FOREIGN KEY (idarticulo)
        REFERENCES articulo(idarticulo),
        
  CONSTRAINT fk_articulo_ingreso
    FOREIGN KEY (idingreso)
        REFERENCES ingreso(idingreso)
);

CREATE TABLE IF NOT EXISTS venta (
  idventa INT PRIMARY KEY,
  idcliente INT,
  idusuario INT,
  tipo_comprobante VARCHAR(20),
  serie_comprobante VARCHAR(7),
  num_comprobante VARCHAR(10),
  fecha date,
  impuesto decimal(4,2),
  total decimal(11,2),
  estado VARCHAR(20),

  CONSTRAINT fk_persona_venta
    FOREIGN KEY (idcliente)
        REFERENCES persona(idpersona),
        
  CONSTRAINT fk_usuario_venta
    FOREIGN KEY (idusuario)
        REFERENCES usuario(idusuario)
);

CREATE TABLE IF NOT EXISTS detalle_venta (
  iddetalle_venta INT PRIMARY KEY,
  idventa INT,
  idarticulo INT,
  cantidad INT,
  precio_venta decimal(11,2),
  descuento decimal(11,2),
  
  CONSTRAINT fk_articulo_detalle_vta
    FOREIGN KEY (idarticulo)
        REFERENCES articulo(idarticulo),
        
  CONSTRAINT fk_venta_detalle 
    FOREIGN KEY (idventa)
        REFERENCES venta(idventa)
);
'''