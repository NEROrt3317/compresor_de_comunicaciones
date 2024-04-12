import zlib

class CompresorZlib:
    def comprimir(self, texto):
        texto_bytes = texto.encode('utf-8')
        texto_comprimido = zlib.compress(texto_bytes)
        return texto_comprimido

    def descomprimir(self, texto_comprimido_hex):
        try:
            texto_comprimido = bytes.fromhex(texto_comprimido_hex)
            texto_descomprimido = zlib.decompress(texto_comprimido).decode('utf-8')
            return texto_descomprimido
        except (zlib.error, ValueError) as e:
            print(f"Hubo un error al descomprimir. Error: {str(e)}")
            return None

