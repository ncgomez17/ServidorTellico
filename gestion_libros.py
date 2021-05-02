from flask import Flask, render_template, request, redirect, url_for, session, json
import DB
from libros import Libro
from flask import Blueprint

gestion_libros = Blueprint('ServidorWeb', __name__, template_folder='templates', static_folder='static')


@gestion_libros.route("/colecciones/eliminar/", methods=["GET", "POST"])
def borrar_libro():
    try:
        isbn = request.args.get('isbn')
        titulo = request.args.get('titulo')
        if titulo is None:
            titulo = "NULL"
        if isbn is None:
            isbn = "NULL"
        DB.eliminar_libro(isbn, titulo, session['nombre'])
        return redirect(url_for('coleccion'))

    except Exception as e:
        print(e)
    return redirect(url_for('coleccion'))


@gestion_libros.route("/editar/", methods=["GET", "POST"])
def editar_libro():
    try:
        if request.method == 'GET':
            isbn = request.args.get('isbn')
            titulo = request.args.get('titulo')
            mensaje = ""
            libro = DB.seleccionar_libro(isbn, titulo, session['nombre'])
            autores = libro[0][2]
            publisher = libro[0][3]
            anhopub = libro[0][4]
            idioma = libro[0][5]
            paginas = libro[0][6]
            comentarios = libro[0][7]
        if request.method == 'POST':
            isbn = request.form['isbn']
            titulo = request.form['titulo']
            autores = request.form['autores']
            publisher = request.form['publisher']
            anhopub = request.form['anhopub']
            idioma = request.form['idioma']
            paginas = request.form['paginas']
            comentarios = request.form['comentarios']
            DB.editar_libro(isbn, titulo, autores, publisher, anhopub, idioma, paginas, comentarios, session['nombre'])
            return redirect(url_for('coleccion'))

        return render_template("editar_libro.html", isbn=isbn, titulo=titulo, autores=autores, publisher=publisher,
                               anhopub=anhopub, idioma=idioma, paginas=paginas, comentarios=comentarios,
                               Mensaje=mensaje)

    except Exception as e:
        print(e)
    return render_template("editar_libro.html", isbn=isbn, titulo=titulo, autores=autores, publisher=publisher,
                           anhopub=anhopub, idioma=idioma, paginas=paginas, comentarios=comentarios, Mensaje=mensaje)


@gestion_libros.route("/anhadir/", methods=["GET", "POST"])
def anhadir_libro():
    try:

        if request.method == 'POST':
            l = Libro()
            l.isbn = request.form['isbn']
            l.titulo = request.form['titulo']
            l.autores = request.form['autores']
            l.publisher = request.form['publisher']
            l.anho_pub = request.form['anhopub']
            l.lang = request.form['idioma']
            l.pages = request.form['paginas']
            l.comments = request.form['comentarios']
            exists = DB.comprobar_libro(l.isbn, l.titulo, session['nombre'])
            if exists is False:
                DB.insertar_libro(session['nombre'], l)
                return redirect(url_for('coleccion'))
            else:
                return render_template("anhadir_libro.html",Mensaje="El isbn o titulo ya existen")

        return render_template("anhadir_libro.html")


    except Exception as e:
        print(e)
    return render_template("anhadir_libro.html")
