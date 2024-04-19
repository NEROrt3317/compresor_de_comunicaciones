import zlib  # Importa el módulo zlib para compresión y descompresión de datos

class CompresorZlib:
    # Método para comprimir un texto en formato string a bytes comprimidos
    def comprimir(self, texto):
        try:
            texto_bytes = texto.encode('utf-8')  # Convierte el texto a bytes utilizando UTF-8
            texto_comprimido = zlib.compress(texto_bytes)  # Comprime los bytes del texto
            return texto_comprimido
        except TypeError as e:
            print(f"Error de tipo: el texto debe ser una cadena. Error: {str(e)}")  # Maneja errores de tipo (por ejemplo, si el input no es un string)
            return None
        except MemoryError as e:
            print(f"Error de memoria: no hay suficiente memoria para comprimir. Error: {str(e)}")  # Maneja errores de memoria insuficiente
            return None
        except Exception as e:
            print(f"Error desconocido al comprimir. Error: {str(e)}")  # Maneja cualquier otro tipo de error desconocido
            return None

    # Método para descomprimir un texto en formato hexadecimal a un string descomprimido
    def descomprimir(self, texto_comprimido_hex):
        try:
            texto_comprimido = bytes.fromhex(texto_comprimido_hex)  # Convierte el texto hexadecimal a bytes
            texto_descomprimido = zlib.decompress(texto_comprimido).decode('utf-8')  # Descomprime los bytes y los convierte a string UTF-8
            return texto_descomprimido
        except ValueError as e:
            print(f"Error de valor: el contenido no está en formato hexadecimal correcto. Error: {str(e)}")  # Maneja errores de formato hexadecimal incorrecto
            return None
        except zlib.error as e:
            print(f"Error de zlib: problema al descomprimir. Error: {str(e)}")  # Maneja errores específicos de zlib al descomprimir
            return None
        except Exception as e:
            print(f"Error desconocido al descomprimir. Error: {str(e)}")  # Maneja cualquier otro tipo de error desconocido
            return None


