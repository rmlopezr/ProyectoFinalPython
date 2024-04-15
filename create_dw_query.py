CREATE_DW =  '''
CREATE TABLE IF NOT EXISTS dimension_tiempo (
    id_tiempo INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    anio INT NOT NULL,
    mes INT NOT NULL,
    dia_mes INT NOT NULL,
    dia_semana INT NOT NULL,
    semana_anio INT NOT NULL,
    trimestre INT NOT NULL,
    es_fin_de_semana TINYINT NOT NULL,
    es_dia_festivo TINYINT NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_articulos (
  idarticulo bigint DEFAULT NULL,
  idcategoria bigint DEFAULT NULL,
  codigo text,
  nombre text,
  precio_venta double DEFAULT NULL,
  stock bigint DEFAULT NULL,
  descripcion text,
  imagen text,
  estado tinyint DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS dim_categoria (
  idcategoria bigint DEFAULT NULL,
  nombre text,
  descripcion text,
  estado tinyint DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS fact_ventas (
  idcategoria bigint DEFAULT NULL,
  idarticulo bigint DEFAULT NULL,
  idventa bigint DEFAULT NULL,
  idingreso bigint DEFAULT NULL,
  iddetalle_venta bigint DEFAULT NULL,
  iddetalle_ingreso bigint DEFAULT NULL,
  cantidad bigint DEFAULT NULL,
  precio_venta double DEFAULT NULL,
  precio_compra double DEFAULT NULL
);

'''