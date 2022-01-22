from itertools import product
from multiprocessing import connection
import os 
import sqlite3



ruta = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(ruta,"db_sqlite3.db")
print(db)

# CONECTARNOS
# nos conectamos y/o creamos el archivo
conection = sqlite3.connect(db)

# creamos un cursos para movernos en el archivo
cursor = conection.cursor()

# CREACIÓN DE TABLAS
crear_tabla = """
    create table if not exists productos(
        id integer primary key autoincrement,
        titulo varchar(100),
        descripcion text,
        precio int(100)
    )
"""

# ejecutamos una acción con el cursos
cursor.execute(crear_tabla)

# guardamos los cambios
conection.commit()


# insertar un registro
insert_in_table = """
    insert into productos values (null, "mesa portatil", "mesa para llevar el portatil",2345)
"""
cursor.execute(insert_in_table)
conection.commit()

varios = [
    ("flores","Flores bonitas",123),
    ("DarkSouls","Tremendo juego",456),
    ("camila","mi novia",789)
]

insertar_registros = """
    insert into productos values (null,?,?,?)
"""
# para ejecutar varios
cursor.executemany(insertar_registros, varios)
conection.commit()


# listar registros
listar_registros = "select * from productos"
productos = cursor.execute(listar_registros).fetchall()
for producto in productos:
    print(producto)

# un solo registro
un_registro = "select * from productos"
un_solo_registro = cursor.execute(un_registro).fetchone()
print("\n",un_solo_registro)

# cerrar la conexion
conection.close()