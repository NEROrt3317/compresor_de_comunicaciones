from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

# Importa la clase CompresorZlib de tu módulo de compresión
import sys
sys.path.append("src")

import compressor.compressorlogic as compresorlogic
from compressor.compressorlogic import *

class MiAplicacion(App):
    def build(self):
        Window.clearcolor = (0.06, 0.1, 0.12, 1)  # Un tono oscuro para el fondo de la ventana

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=[10, 20], spacing=10)

        # Título
        titulo = Label(text='Compresor de Comunicaciones', font_size='40sp', color=(0.2, 0.45, 0.8, 1), size_hint=(1, None), height=60)

        # Descripción
        descripcion = Label(text=('El Compresor de Comunicaciones es una herramienta diseñada para optimizar la '
                                  'transmisión de datos al reducir el tamaño de los archivos sin comprometer la '
                                  'integridad de la información.'),
                            font_size='16sp', color=(0.7, 0.7, 0.7, 1), size_hint=(1, None), halign='left', valign='middle')
        descripcion.bind(size=descripcion.setter('text_size'))  # Esto permite que el texto se ajuste al tamaño del Label

        # Añadir widgets al layout
        layout.add_widget(titulo)
        layout.add_widget(descripcion)

        # Ajustar la altura del layout de descripción para que todo el texto sea visible
        descripcion.size_hint_y = None
        descripcion.height = 150  # Ajusta esto según sea necesario para tu texto y tamaño de ventana


        # Caja de entrada de texto
        self.entrada = TextInput(hint_text='Escribe algo aquí o introduce el texto comprimido', font_size=25,size_hint=(2, 0.6), background_color=(0.12, 0.14, 0.17, 1), foreground_color=(0.8, 0.8, 0.8, 1))
        layout.add_widget(self.entrada)

        # Botones con esquinas redondeadas
        layout_botones = BoxLayout(size_hint=(1, 0.15), spacing=10)
        boton1 = Button(text='Comprimir', background_normal='', background_color=(0.2, 0.45, 0.8, 1), color=(1, 1, 1, 1))
        boton2 = Button(text='Descomprimir', background_normal='', background_color=(0.2, 0.45, 0.8, 1), color=(1, 1, 1, 1))
        boton1.bind(on_press=self.comprimir)
        boton2.bind(on_press=self.descomprimir)
        layout_botones.add_widget(boton1)
        layout_botones.add_widget(boton2)
        layout.add_widget(layout_botones)

        # Caja de texto para mostrar el resultado
        self.resultado = TextInput(text=' aca se motrara el resultado...',font_size=25)
        layout.add_widget(self.resultado)



        # Inicializa la clase de compresión
        self.compresor = compresorlogic.CompresorZlib()

        return layout

    def comprimir(self, instance):
        try:
            result=self.compresor.comprimir(self.entrada.text)
            self.resultado.text = "Texto comprimido (en bytes): \n" + result.hex()
        except Exception as e:
            self.resultado.text = f"Error al descomprimir: {e}"

    def descomprimir(self, instance):
        try:
            result=self.compresor.descomprimir(self.entrada.text)
            self.resultado.text = "Texto comprimido (en bytes): \n" + result
        except Exception as e:
            self.resultado.text = f"Error al descomprimir: {e}"

if __name__ == '__main__':
    MiAplicacion().run()
