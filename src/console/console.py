import sys
sys.path.append("src")

import compressor.compressorlogic as compresorlogic
from compressor.compressorlogic import *


class Aplicacion:
    def __init__(self):
        self.compresor = compresorlogic.CompresorZlib()

    def ejecutar(self):
        print("Bienvenido a la aplicación de compresión/descompresión de texto.")
        texto_usuario = input("Por favor, ingrese el texto: ")
        accion = input("¿Desea comprimir o descomprimir el texto? (comprimir/descomprimir): ")

        if accion.lower() == "comprimir":
            resultado = self.compresor.comprimir(texto_usuario)
            print(f"Texto comprimido (en bytes): {resultado.hex()}")
        elif accion.lower() == "descomprimir":
            resultado = self.compresor.descomprimir(texto_usuario)
            if resultado:
                print(f"Texto descomprimido: {resultado}")
            else:
                print("No se pudo descomprimir el texto, asegúrese de que esté en el formato correcto.")
        else:
            print("Acción no reconocida. Por favor, ingrese 'comprimir' o 'descomprimir'.")

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
