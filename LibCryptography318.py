# Importamos el módulo Fernet de cryptography
from cryptography.fernet import Fernet

# Generamos una clave aleatoria y la guardamos en un archivo
clave = Fernet.generate_key()
with open("clave.key", "wb") as archivo:
    archivo.write(clave)

# Creamos un objeto Fernet con la clave
f = Fernet(clave)

# Definimos el mensaje que queremos encriptar
#mensaje = b"Hola, soy Copilot"
mensaje = input("ingresa tu texto: \n")
byte_mensaje = mensaje.encode('ASCII')
# Encriptamos el mensaje con el método encrypt
cifrado = f.encrypt(byte_mensaje)
cifrado_string_data = cifrado.decode('utf-8')

# Imprimimos el mensaje cifrado
print(cifrado_string_data)

# Desciframos el mensaje con el método decrypt
descifrado = f.decrypt(cifrado)
descifrado_string_data = descifrado.decode('utf-8')

# Imprimimos el mensaje original
print(descifrado_string_data)
