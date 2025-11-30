"""
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

class singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(singleton, cls).__new__(cls)
        return cls._instance
    
singleton1 = singleton()
print(singleton1)
singleton2 = singleton()
print(singleton2)

print(singleton1 is singleton2)

"""
* DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 """

class usuario:
    _instance = None
    id: int = None
    username: str = None
    nombre: str = None
    email: str = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(usuario, cls).__new__(cls)
        return cls._instance
    def asignar_usuario(self, id, username, nombre, email):
        self.id = id
        self.username = username
        self.nombre = nombre
        self.email = email
    def recuperar_usuario(self):
        return(f"{self.id}, {self.username}, {self.nombre}, {self.email}")
    def borrar_usuario(self):
        self.id = None
        self.username = None
        self.nombre = None
        self.email = None

inicio_1 = usuario()
print(inicio_1.recuperar_usuario())
inicio_1.asignar_usuario(69, "Enzo-09", "Enzo", "johnDoe@gmail.com")
print(inicio_1.recuperar_usuario())
inicio_1.borrar_usuario()
print(inicio_1.recuperar_usuario())
