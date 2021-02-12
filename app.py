import jwt
from flask import Flask, render_template, request, redirect, url_for, session, json
import hashlib
import DB
from libros import Libro
from gestion_libros import gestion_libros

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.register_blueprint(gestion_libros, url_prefix='/gestion')
if __name__ == "__main__":
    app.run(debug=True)


@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def home_func():
    try:
        if request.method == 'POST':
            if request.form['username'] and request.form['password']:
                name = request.form['username']
                password = request.form['password']
                h = hashlib.sha256()
                h.update(password.encode(encoding='UTF-8', errors='strict'))
                comprobacion = DB.comprobar_user_and_pass(name, h.hexdigest())
                if comprobacion is True:
                    session['nombre'] = name
                    return redirect("/colecciones")
                else:
                    return render_template('login.html', Mensaje="Error:Usuario o contraseña incorrectos")
    except Exception as e:
        print(e)
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def registro():
    conn = DB.connect()
    cursor = conn.cursor()
    try:
        if request.method == 'POST':
            if request.form['username'] and request.form['password'] and request.form['password2']:
                name = request.form['username']
                password = request.form['password']
                password2 = request.form['password2']
                exists = DB.comprobar_login(name)
                if exists is False and password ==password2:
                    sql = "INSERT INTO usuarios (nombre,password) VALUES (%s, %s)"
                    h = hashlib.sha256()
                    h.update(password.encode(encoding='UTF-8', errors='strict'))
                    val = (name, h.hexdigest())
                    cursor.execute(sql, val)
                    conn.commit()
                    session['nombre'] = name
                    return redirect("/colecciones")
                elif password != password2:
                    return render_template('registro.html', Mensaje="Error:Contraseñas no coinciden")
                else:
                    return render_template('registro.html', Mensaje="Error:El usuario ya existe")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return render_template("registro.html")


@app.route("/colecciones", methods=["GET", "POST"])
def coleccion():
    token = ""
    tabla = DB.recorrer_tabla(session['nombre'])
    if request.method == 'POST':
        token = write_token()
    if request.method == 'GET' and request.args.get('busqueda'):
        search = request.args.get('busqueda')
        tabla = DB.search_libro(session['nombre'], search)
        return render_template("tabla.html", Usuario=session['nombre'], libros=tabla, token=token)

    return render_template("tabla.html", Usuario=session['nombre'], libros=tabla, token=token)


##funcion para generar el token jwt
def write_token():
    payload = {'user': session['nombre']}
    token_bytes = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    token = token_bytes.decode()
    return token


##funcion para decodificar el token
def validate_token(encoded_jwt):
    try:
        response = jwt.decode(encoded_jwt, app.config['SECRET_KEY'], algorithms=['HS256'])
        return response
    except jwt.exceptions.DecodeError:
        return "Token no valido"


##Webservice que se encargara de procesar los mensajes de configuración
@app.route('/index/colecciones/sincronizacion/', methods=['GET', 'POST'])
def recibir_json():
    content = request.get_json()
    data = json.loads(content)
    list = []
    token = None
    message = ""
    try:
        for i in data:

            if "token" in i:
                token = i["token"]
                token_user = validate_token(token)
                usuario = token_user['user']
                exists = DB.comprobar_login(usuario)
            else:
                l = Libro()
                l.titulo = i["_Libro__titulo"]
                l.autores = i["_Libro__autores"]
                l.publisher = i["_Libro__publisher"]
                l.anho_pub = i["_Libro__anho_pub"]
                l.isbn = i["_Libro__isbn"]
                l.lang = i["_Libro__lang"]
                l.pages = i["_Libro__pages"]
                l.comments = i["_Libro__comments"]
                list.append(l)

        if exists is False:
            return "El token no tiene la información necesaria para identificar al usuario"
        else:
            for libro in list:
                comprobacion = DB.comprobar_libro(libro.isbn, libro.titulo, usuario)
                if comprobacion is False:
                    DB.insertar_libro(usuario, libro)
                else:
                    print("El libro ya existe en la base de datos")
                    message = message + "El libro" + str(l.isbn) + " con titulo " + str(
                        l.titulo) + "ya existe en la base de datos\n"
            return "Token recibido correctamente" + message
    except Exception as e:
        print(e)
        return "El token no es válido o tiene algun dato incorrecto"
