# Aplicación de Compresión de Texto

## Autores
- jorge luis bedoya sanchez 
- Nehir Rodríguez tapias

## ¿Para qué sirve?
Este código proporciona una herramienta para la compresión y descompresión de texto utilizando la biblioteca `zlib` de Python, facilitando el manejo eficiente del almacenamiento de datos y la transferencia de información a través de la reducción del tamaño de los archivos de texto. Al proporcionar un texto, el programa puede comprimir este texto para reducir su tamaño o descomprimir texto previamente comprimido para restaurar su contenido original.

## Propósito
El objetivo de este código es ofrecer una solución simple y eficaz para la compresión y descompresión de textos, mejorando la eficiencia en el manejo de grandes volúmenes de información y facilitando la optimización del almacenamiento de datos y la velocidad de transferencia en diversas aplicaciones y procesos.

## Prerrequisitos
- **Instalación de Python**: Python es el lenguaje de programación utilizado en este programa, por lo que es necesario tener Python instalado en su sistema. Python se puede descargar desde el sitio web oficial de Python y se instala siguiendo las instrucciones proporcionadas.
- **Datos de entrada relevantes**: Al ejecutar el programa se requerirá proporcionar el texto a comprimir o el texto comprimido a descomprimir, dependiendo de la operación deseada.

## ¿Cómo está hecho?
El proyecto consta de una estructura modular que incluye los siguientes archivos principales:

- **compressorlogic.py**: Contiene la lógica principal para las operaciones de compresión y descompresión.
- **console.py**: Proporciona una interfaz de consola para que los usuarios interactúen con el programa.
- **testcaseregular.py**: Incluye pruebas unitarias para casos de uso comunes de compresión y descompresión.
- **testcaseerror.py**: Contiene pruebas unitarias para manejar errores y casos límite.
- **testcasesextraordinary.py**: Incluye pruebas unitarias para escenarios extraordinarios y poco comunes.

### Estructura sugerida:
- **Carpeta compressor**: Donde se almacena la lógica principal del proyecto.
- **Carpeta test**: Donde se guardan las pruebas unitarias para verificar la funcionalidad del código.
- **Carpeta console**: Donde se ubica la interfaz de usuario para interactuar con el programa sin necesidad de acceder al código fuente.

El código hace uso de la biblioteca `zlib` de Python, que proporciona funciones de compresión y descompresión, así como de la biblioteca estándar de Python para otras necesidades básicas del programa. Además, utiliza la biblioteca `unittest` para implementar las pruebas unitarias, asegurando la calidad y el correcto funcionamiento del software.
