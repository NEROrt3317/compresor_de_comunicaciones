# Comprensor de comunicaciones 

## Descripción
El Compresor de Comunicaciones es una herramienta diseñada para optimizar la transmisión de datos 
al reducir el tamaño de los archivos sin comprometer la integridad de la información. 
Utilizando algoritmos avanzados de compresión, este proyecto busca facilitar la 
transferencia de datos en entornos donde el ancho de banda es limitado o costoso..

## Características
Enumera las características principales de tu proyecto. Por ejemplo:
- Compresión de datos utilizando algoritmos.
- Interfaz fácil de usar para comprimir y descomprimir archivos.
- Soporte para múltiples tipos de archivos y formatos de datos.

## Instalación
Proporciona instrucciones claras sobre cómo instalar y configurar el proyecto. Por ejemplo:
1. Clona el repositorio a tu máquina local:
   ```
   git clone https://github.com/jorgebls/compresor-de-comunicaciones
   ```
2. Navega al directorio del proyecto:
   ```
   cd comprensor_de_comunicaciones/src/console/
   ```
3. Ejecutar el programa :
   ```
   python -m console.py
   ```

## Ejecución
Explica cómo utilizar tu proyecto. Por ejemplo:
1. Ejecuta el programa principal:
   ```
   python console.py
   ```
2. Se abrirá una interfaz de usuario donde puedes seleccionar los archivos que deseas comprimir o descomprimir.


## Ejemplos
Se proporciona un pedazo de código de que como funciona para comprimir o descomprimir un archivo. Por ejemplo:

```python
# Ejemplo de cómo comprimir o descomprimir un archivo

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

```
Comprimir
Bienvenido a la aplicación de compresión/descompresión de texto.
Por favor, ingrese el texto: hola
¿Desea comprimir o descomprimir el texto? (comprimir/descomprimir): comprimir
Texto comprimido (en bytes): 789ccbc8cf490400042a01a5
Descomprimir

Bienvenido a la aplicación de compresión/descompresión de texto.
Por favor, ingrese el texto: 789ccbc8cf490400042a01a5

¿Desea comprimir o descomprimir el texto? (comprimir/descomprimir): descomprimir
Texto descomprimido: hola

## Licencia MIT

Copyright (c) 2024 NEHIR RODRIGUEZ, JORGE BEDOYA 

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y los archivos de documentación asociados (el "Software"), para tratar
en el Software sin restricciones, incluidos, entre otros, los derechos
utilizar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y / o vender
copias del Software, y permitir a las personas a quienes se les proporcione el Software lo hagan
lo mismo, sujeto a las siguientes condiciones:

El aviso de derechos de autor anterior y este aviso de permiso se incluirán en todos
copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
IMPLÍCITO, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
ADECUACIÓN PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO
LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGÚN RECLAMO, DAÑO U OTRO
RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, DERIVADO DE,
FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS NEGOCIOS EN EL
EL SOFTWARE.
