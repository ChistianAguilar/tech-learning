class Usuario:
    # Constructor con atributos con distintas protecciones
    def __init__(self, nombre, email, password):
        self.nombre = nombre        # Atributo Público
        self._email = email         # Atributo Protegido
        self.__password = password  # Atributo Privado <-- Encapsulado 
    
    # Getters (Leer atributos)
    
    # Getter para email (protegido)
    def obtener_email(self):
        return self._email
    
    # Getter para password (privado)
    def obtener_password(self):
        print("Acceso restringido a password")
        return "****" # No muestra el password real
    
    
    # Setters (modificar atributos)
    
    # Setters para email (validadcion)
    def establecer_email(self, nuevo_email):
        if "@" in nuevo_email and "." in nuevo_email:
            self._email = nuevo_email
            print(f"Email actualizado: {self._email}")
        else:
            print("Email inválido")
    
    # Setter para password (validacion estricta)
    def establecer_password(self, nuevo_password):
        if len(nuevo_password) >= 8:
            self.__password = nuevo_password
            print("Password actualizado")
    
    # Método para mostrar info segura
    def mostrar_info(self):
        return f"Usuario: {self.nombre}, Email: {self._email}"
    
    def __str__(self):
        return self.mostrar_info()
        
        
# Objetos ()

# Crear usuario
usuario = Usuario("Leba", "leba@email.com", "123456789")

# Acceso seguro (Getters)
print(usuario.nombre)           #Publico: Leba
print(usuario.obtener_email())  #Protegido: leba@email.com
print(usuario.obtener_password()) # Privado: ****

# Modificación segura (setters)
usuario.establecer_email("nuevo@email.com")
usuario.establecer_email("hola") # invalido

usuario.establecer_password("nuevapass123")
usuario.establecer_password("1234") # invalido

print(usuario)