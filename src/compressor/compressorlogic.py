import zlib

class CompresorZlib:

    def comprimir(self, texto):
        try:
            texto_bytes = texto.encode('utf-8')
            texto_comprimido = zlib.compress(texto_bytes)
            return texto_comprimido
        except TypeError as e:
            print(f"Error de tipo: el texto debe ser una cadena. Error: {str(e)}")
            return None
        except MemoryError as e:
            print(f"Error de memoria: no hay suficiente memoria para comprimir. Error: {str(e)}")
            return None
        except Exception as e:
            print(f"Error desconocido al comprimir. Error: {str(e)}")
            return None

    def descomprimir(self, texto_comprimido_hex):
        try:
            texto_comprimido = bytes.fromhex(texto_comprimido_hex)
            texto_descomprimido = zlib.decompress(texto_comprimido).decode('utf-8')
            return texto_descomprimido
        except ValueError as e:
            print(f"Error de valor: el contenido no está en formato hexadecimal correcto. Error: {str(e)}")
            return None
        except zlib.error as e:
            print(f"Error de zlib: problema al descomprimir. Error: {str(e)}")
            return None
        except Exception as e:
            print(f"Error desconocido al descomprimir. Error: {str(e)}")
            return None


