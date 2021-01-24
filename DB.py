import MySQLdb

DB_HOST = "localhost"
DB_HOST = "root"
DB_HOST = "password"
DB_HOST = "ServidorWeb"


##Funcion para realizar la conexión con la base de datos
def connect():
    con = MySQLdb.connect("localhost", "root", "password", "ServidorWeb")
    return con


##Funcion para comprobar si el usuario y la contraseña son correctos
def comprobar_user_and_pass(name, password):
    try:
        con = connect()
        query = "SELECT id FROM usuarios WHERE nombre LIKE %s AND password LIKE %s"
        cursor = con.cursor()
        cursor.execute(query, (name, password))
        rows = cursor.rowcount
        if rows > 0:
            return True
        else:
            return False
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()


##Funcion para comprobar si el login ya existe
def comprobar_login(name):
    try:
        con = connect()
        query = "SELECT id FROM usuarios WHERE nombre LIKE %s"
        cursor = con.cursor()
        cursor.execute(query, (name,))
        rows = cursor.rowcount

        if rows > 0:
            return True
        else:
            return False
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()


##recorrer los libros del usuario
def recorrer_tabla(usuario):
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute("""SELECT isbn,titulo,autores,publisher,anhopub,idioma,paginas,comentarios FROM libros
              WHERE user LIKE %s""", (usuario,))
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


##insertar datos en la tabla
def insertar_libro(usuario, libro):
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute("""INSERT INTO libros (isbn, user, titulo, autores, publisher, anhopub, idioma, paginas, comentarios) 
        VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)""",
                       (libro.isbn, usuario, libro.titulo, libro.autores, libro.publisher, libro.anho_pub, libro.lang,
                        libro.pages, libro.comments))
        db.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def eliminar_libro(isbn, titulo,usuario):
    try:
        db = connect()
        cursor = db.cursor()
        query = """DELETE FROM libros WHERE (isbn = %s OR titulo = %s) AND user = %s"""
        cursor.execute(query, (isbn, titulo, usuario))
        db.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


##comprobar que un libro ya existe en la base de datos
def comprobar_libro(isbn, titulo,usuario):
    try:
        con = connect()
        query = "SELECT id FROM libros WHERE (isbn = %s OR titulo = %s) AND user = %s"
        cursor = con.cursor()
        cursor.execute(query, (isbn, titulo, usuario))
        rows = cursor.rowcount
        if rows > 0:
            return True
        else:
            return False
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()


##seleccionar un libro a partir de su isbn o titulo
def seleccionar_libro(isbn, titulo, usuario):
    try:
        con = connect()
        query = "SELECT isbn,titulo,autores,publisher,anhopub,idioma,paginas,comentarios  FROM libros WHERE (isbn " \
                "LIKE %s OR titulo LIKE %s) AND user = %s"
        cursor = con.cursor()
        cursor.execute(query, (isbn, titulo,usuario))
        return cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()


##editamos un libro
def editar_libro(isbn, titulo, autores, publisher, anhopub, idioma, paginas, comentarios,usuario):
    try:
        con = connect()
        query = "UPDATE libros SET autores = %s, publisher = %s, anhopub = %s, idioma = %s, paginas = %s, comentarios " \
                "= %s WHERE (isbn = %s OR titulo =%s) AND user = %s"
        cursor = con.cursor()
        cursor.execute(query, (autores, publisher, anhopub, idioma, paginas, comentarios, isbn, titulo, usuario))
        con.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()


##buscamos los libros con el titulo o isbn parecidos o iguales
def search_libro(usuario, search):
    try:
        con = connect()
        cursor = con.cursor()
        cursor.execute("""SELECT isbn,titulo,autores,publisher,anhopub,idioma,paginas,comentarios FROM libros
              WHERE user LIKE %s AND (isbn like %s OR titulo like %s)""", (usuario, search + '%', search +'%'))
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()
