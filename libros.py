class Libro:
    """Define un libro al que se le pasaran unos parametros
    que consistiran en los distintos datos del libro
    """

    def __init__(self):
        self.__titulo = ""
        self.__autores = []
        self.__publisher = ""
        self.__anho_pub = ""
        self.__isbn = ""
        self.__lang = ""
        self.__pages = ""
        self.__comments = ""

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo):
        self.__titulo = nuevo

    @property
    def autores(self):
        return self.__autores

    @autores.setter
    def autores(self, nuevo):
        self.__autores = nuevo

    def añadir_autor(self, autor):
        self.__autores.append(autor)

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, nuevo):
        self.__publisher = nuevo

    @property
    def anho_pub(self):
        return self.__anho_pub

    @anho_pub.setter
    def anho_pub(self, nuevo):
        self.__anho_pub = nuevo

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, nuevo):
        self.__isbn = nuevo

    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, nuevo):
        self.__lang = nuevo

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, nuevo):
        self.__pages = nuevo

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, nuevo):
        self.__comments = nuevo

    def __str__(self):
        cadena = self.__titulo + '\n'
        for autor in self.__autores:
            cadena += autor + '\n'
        cadena += str(self.__anho_pub) + '\n' + str(self.__isbn) + '\n' + self.__lang + '\n'
        cadena += str(self.__pages) + '\n' + self.__comments + '\n'
        return cadena
