import sys
sys.path.append("src")  # Agrega el directorio 'src' al path de búsqueda de módulos de Python

import compressor.compressorlogic as compresorlogic  # Importa el módulo de lógica del compresor
from compressor.compressorlogic import *  # Importa todos los elementos del módulo compressorlogic

class Aplicacion:
    def __init__(self):
        self.compresor = compresorlogic.CompresorZlib()  # Instancia un objeto de la clase CompresorZlib

    def ejecutar(self):
        print("Bienvenido a la aplicación de compresión/descompresión de texto.")
        texto_usuario = input("Por favor, ingrese el texto: ")  # Solicita al usuario que ingrese el texto
        accion = input("¿Desea comprimir o descomprimir el texto? (comprimir/descomprimir): ")  # Pregunta si desea comprimir o descomprimir el texto

        if accion.lower() == "comprimir":  # Procesa la acción de compresión
            resultado = self.compresor.comprimir(texto_usuario)  # Comprime el texto ingresado
            print(f"Texto comprimido (en bytes): {resultado.hex()}")  # Muestra el texto comprimido en formato hexadecimal
        elif accion.lower() == "descomprimir":  # Procesa la acción de descompresión
            resultado = self.compresor.descomprimir(texto_usuario)  # Intenta descomprimir el texto ingresado
            if resultado:
                print(f"Texto descomprimido: {resultado}")  # Muestra el texto descomprimido si es exitoso
            else:
                print("No se pudo descomprimir el texto, asegúrese de que esté en el formato correcto.")  # Informa de un error si no se puede descomprimir
        else:
            print("Acción no reconocida. Por favor, ingrese 'comprimir' o 'descomprimir'.")  # Maneja entradas no reconocidas

if __name__ == "__main__":
    app = Aplicacion()  # Crea una instancia de Aplicacion
    app.ejecutar()  # Ejecuta el método ejecutar de la instancia

