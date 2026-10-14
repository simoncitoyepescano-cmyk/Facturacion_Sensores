

from datetime import date

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ListProperty, StringProperty, BooleanProperty
from kivy.animation import Animation
from kivy.metrics import dp

import sys
import os


NOMBRE_ARCHIVO_MUSICA = "Anuel AA - 3 Some (Letra Lyrics).mp3"
RUTA_MUSICA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "assets", NOMBRE_ARCHIVO_MUSICA
)
VOLUMEN_MUSICA = 0.4  # entre 0.0 (silencio) y 1.0 (volumen máximo)


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
sys.path.append("src")
try:
    from model.logica_sensores import (
        calcular_valor_factura,
        verificar_numero_servicios,
        verificar_precio_unitario,
    )
except ImportError:
    from src.model.logica_sensores import (
        calcular_valor_factura,
        verificar_numero_servicios,
        verificar_precio_unitario,
    )



COLOR_FONDO = "#0F172A"       
COLOR_TARJETA = "#16213E"     
COLOR_TARJETA_2 = "#1B2A4A"
COLOR_ACENTO = "#22D3B8"      
COLOR_ACENTO_OSCURO = "#17A992"
COLOR_TEXTO = "#F1F5F9"
COLOR_TEXTO_SUAVE = "#94A3B8"
COLOR_ERROR = "#F87171"
COLOR_CAMPO = "#0F1F3D"
COLOR_BORDE = "#2C3E63"


KV = """
#:import dp kivy.metrics.dp

<CampoLabel@Label>:
    color: 0.85, 0.87, 0.92, 1
    font_size: '14sp'
    halign: 'left'
    valign: 'middle'
    size_hint_y: None
    height: dp(22)
    text_size: self.size

<CampoInput>:
    background_normal: ''
    background_active: ''
    background_color: 0, 0, 0, 0
    foreground_color: 0.95, 0.96, 0.98, 1
    cursor_color: 0.13, 0.83, 0.72, 1
    hint_text_color: 0.55, 0.62, 0.75, 1
    selection_color: 0.13, 0.83, 0.72, 0.35
    padding: [dp(14), dp(12), dp(14), dp(12)]
    font_size: '16sp'
    multiline: False
    size_hint_y: None
    height: dp(46)
    canvas.before:
        Color:
            rgba: self.fondo_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10)]
        Color:
            rgba: self.borde_color
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, dp(10))
            width: 1.3

<BotonAccion>:
    background_normal: ''
    background_down: ''
    background_color: 0, 0, 0, 0
    color: 0.04, 0.09, 0.1, 1
    bold: True
    font_size: '16sp'
    size_hint_y: None
    height: dp(50)
    canvas.before:
        Color:
            rgba: self.fondo_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(12)]

<BotonMusica>:
    background_normal: ''
    background_down: ''
    background_color: 0, 0, 0, 0
    color: 0.85, 0.87, 0.92, 1
    font_size: '12sp'
    bold: True
    size_hint: None, None
    size: dp(96), dp(30)
    canvas.before:
        Color:
            rgba: (0.13, 0.83, 0.72, 0.22) if self.activo else (0.16, 0.22, 0.35, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(15)]
        Color:
            rgba: (0.13, 0.83, 0.72, 1) if self.activo else (0.32, 0.4, 0.56, 1)
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, dp(15))
            width: 1

<BotonSecundario>:
    background_normal: ''
    background_down: ''
    background_color: 0, 0, 0, 0
    color: 0.85, 0.87, 0.92, 1
    bold: True
    font_size: '15sp'
    size_hint_y: None
    height: dp(50)
    canvas.before:
        Color:
            rgba: (0.16, 0.22, 0.35, 1) if self.state == 'normal' else (0.20, 0.27, 0.42, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(12)]
        Color:
            rgba: 0.24, 0.33, 0.5, 1
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, dp(12))
            width: 1

"""


class CampoInput(TextInput):
    
    fondo_color = ListProperty([0.06, 0.12, 0.24, 1])
    borde_color = ListProperty([0.17, 0.24, 0.39, 1])

    def marcar_error(self, activo: bool):
        if activo:
            Animation(borde_color=[0.97, 0.44, 0.44, 1], d=0.15).start(self)
        else:
            Animation(borde_color=[0.17, 0.24, 0.39, 1], d=0.15).start(self)


class BotonAccion(Button):
    
    fondo_color = ListProperty([0.13, 0.83, 0.72, 1])

    def on_press(self):
        Animation(fondo_color=[0.09, 0.66, 0.57, 1], d=0.08).start(self)

    def on_release(self):
        Animation(fondo_color=[0.13, 0.83, 0.72, 1], d=0.12).start(self)


class BotonSecundario(Button):
    pass


class BotonMusica(Button):
    
    activo = BooleanProperty(True)


Builder.load_string(KV)


def _hex_a_rgba(codigo_hex: str, alpha: float = 1.0):
    codigo_hex = codigo_hex.lstrip("#")
    r, g, b = (int(codigo_hex[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return [r, g, b, alpha]


class TarjetaPrincipal(BoxLayout):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        with self.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            # sombra
            Color(0, 0, 0, 0.35)
            self._sombra = RoundedRectangle(radius=[dp(20)])
            # fondo tarjeta
            Color(*_hex_a_rgba(COLOR_TARJETA))
            self._fondo = RoundedRectangle(radius=[dp(20)])
        self.bind(pos=self._actualizar, size=self._actualizar)

    def _actualizar(self, *args):
        self._fondo.pos = self.pos
        self._fondo.size = self.size
        self._sombra.pos = (self.x + dp(3), self.y - dp(5))
        self._sombra.size = self.size


class RaizFondo(FloatLayout):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(*_hex_a_rgba(COLOR_FONDO))
            self._fondo = Rectangle(pos=self.pos, size=self.size)
            # franja decorativa superior con el color de acento, muy sutil
            Color(*_hex_a_rgba(COLOR_ACENTO, 0.08))
            self._franja = Rectangle(pos=self.pos, size=(self.size[0], self.size[1] * 0.55))
        self.bind(pos=self._actualizar, size=self._actualizar)

    def _actualizar(self, *args):
        self._fondo.pos = self.pos
        self._fondo.size = self.size
        self._franja.pos = (self.x, self.y + self.height * 0.45)
        self._franja.size = (self.width, self.height * 0.55)


class FilaResultado(BoxLayout):
    """Fila 'etiqueta ..... valor' dentro del panel de resultado."""

    def __init__(self, etiqueta="", valor="—", color_valor=None, **kwargs):
        kwargs.setdefault("orientation", "horizontal")
        kwargs.setdefault("size_hint_y", None)
        kwargs.setdefault("height", dp(26))
        super().__init__(**kwargs)

        self._etiqueta = Label(
            text=etiqueta,
            color=_hex_a_rgba(COLOR_TEXTO_SUAVE),
            font_size="13.5sp",
            halign="left",
            valign="middle",
        )
        self._etiqueta.bind(size=self._etiqueta.setter("text_size"))

        self._valor = Label(
            text=valor,
            color=color_valor if color_valor else _hex_a_rgba(COLOR_TEXTO),
            font_size="14.5sp",
            bold=True,
            halign="right",
            valign="middle",
        )
        self._valor.bind(size=self._valor.setter("text_size"))

        self.add_widget(self._etiqueta)
        self.add_widget(self._valor)

    @property
    def valor(self):
        return self._valor.text

    @valor.setter
    def valor(self, texto):
        self._valor.text = texto


class FacturacionSensoresApp(App):
    title = "Facturación de Sensores"

    def build(self):
        Window.clearcolor = _hex_a_rgba(COLOR_FONDO)
        Window.size = (480, 720)
        Window.minimum_width, Window.minimum_height = (420, 640)

        raiz = RaizFondo()

        contenedor_scroll = FloatLayout()
        raiz.add_widget(contenedor_scroll)

        tarjeta = TarjetaPrincipal(
            size_hint=(None, None),
            width=dp(400),
            padding=dp(28),
            spacing=dp(14),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        tarjeta.bind(minimum_height=tarjeta.setter("height"))

        # --- Encabezado (título + botón de música) ---
        fila_titulo = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(36),
            spacing=dp(8),
        )
        etiqueta_titulo = Label(
            text="[b]Facturación de Sensores[/b]",
            markup=True,
            font_size="22sp",
            color=_hex_a_rgba(COLOR_TEXTO),
            halign="left",
            valign="middle",
        )
        etiqueta_titulo.bind(size=etiqueta_titulo.setter("text_size"))
        fila_titulo.add_widget(etiqueta_titulo)

        self.boton_musica = BotonMusica(text="Silenciar")
        self.boton_musica.bind(on_release=self.alternar_musica)
        fila_titulo.add_widget(self.boton_musica)
        tarjeta.add_widget(fila_titulo)

        tarjeta.add_widget(Label(
            text="Calcula el valor a pagar (incluye IVA del 19%)",
            font_size="13sp",
            color=_hex_a_rgba(COLOR_TEXTO_SUAVE),
            size_hint_y=None,
            height=dp(22),
        ))

        separador = self._crear_separador()
        tarjeta.add_widget(separador)

        # --- Campo: nombre del cliente ---
        tarjeta.add_widget(self._crear_etiqueta("Nombre del cliente"))
        self.campo_cliente = CampoInput(hint_text="Ej. Cryogas")
        tarjeta.add_widget(self.campo_cliente)

        # --- Campo: número de servicios ---
        tarjeta.add_widget(self._crear_etiqueta("Número de servicios / sensores"))
        self.campo_servicios = CampoInput(hint_text="Ej. 12", input_filter="int")
        tarjeta.add_widget(self.campo_servicios)

        # --- Campo: precio unitario ---
        tarjeta.add_widget(self._crear_etiqueta("Precio unitario por sensor"))
        self.campo_precio = CampoInput(hint_text="Ej. 15000 ó 15000.50")
        tarjeta.add_widget(self.campo_precio)

        # --- Mensaje de error ---
        self.etiqueta_error = Label(
            text="",
            color=_hex_a_rgba(COLOR_ERROR),
            font_size="12.5sp",
            size_hint_y=None,
            height=dp(0),
            halign="left",
            valign="middle",
        )
        self.etiqueta_error.bind(size=self.etiqueta_error.setter("text_size"))
        tarjeta.add_widget(self.etiqueta_error)

        # --- Botones ---
        fila_botones = BoxLayout(
            orientation="horizontal", spacing=dp(10),
            size_hint_y=None, height=dp(50),
        )
        boton_limpiar = BotonSecundario(text="Limpiar", size_hint_x=0.38)
        boton_limpiar.bind(on_release=self.limpiar_formulario)
        boton_calcular = BotonAccion(text="Calcular factura", size_hint_x=0.62)
        boton_calcular.bind(on_release=self.calcular_factura)
        fila_botones.add_widget(boton_limpiar)
        fila_botones.add_widget(boton_calcular)
        tarjeta.add_widget(fila_botones)

        tarjeta.add_widget(self._crear_separador())

        # --- Panel de resultado (tarjeta interna) ---
        self.panel_resultado = self._crear_panel_resultado()
        tarjeta.add_widget(self.panel_resultado)

        contenedor_scroll.add_widget(tarjeta)

        self.reproducir_musica()

        return raiz


    def reproducir_musica(self):
        """Carga y reproduce en loop el archivo definido en RUTA_MUSICA.
        Si el archivo no existe o no se puede cargar, la app sigue
        funcionando normalmente pero sin sonido."""
        self.sonido = None
        if not os.path.isfile(RUTA_MUSICA):
            print(
                f"[Música] No se encontró '{RUTA_MUSICA}'. "
                "La app arrancará sin música de fondo."
            )
            if hasattr(self, "boton_musica"):
                self.boton_musica.opacity = 0
                self.boton_musica.disabled = True
            return

        self.sonido = SoundLoader.load(RUTA_MUSICA)
        if self.sonido:
            self.sonido.loop = True
            self.sonido.volume = VOLUMEN_MUSICA
            self.sonido.play()
        else:
            print(f"[Música] No se pudo cargar '{RUTA_MUSICA}'.")

    def alternar_musica(self, *_):
        if not self.sonido:
            return
        if self.boton_musica.activo:
            self.sonido.volume = 0
            self.boton_musica.activo = False
            self.boton_musica.text = "Activar"
        else:
            self.sonido.volume = VOLUMEN_MUSICA
            self.boton_musica.activo = True
            self.boton_musica.text = "Silenciar"

    def on_stop(self):
        if getattr(self, "sonido", None):
            self.sonido.stop()


    def _crear_etiqueta(self, texto):
        etiqueta = Label(
            text=texto,
            color=_hex_a_rgba(COLOR_TEXTO_SUAVE),
            font_size="13sp",
            size_hint_y=None,
            height=dp(20),
            halign="left",
            valign="bottom",
        )
        etiqueta.bind(size=etiqueta.setter("text_size"))
        return etiqueta

    def _crear_separador(self):
        from kivy.graphics import Color, Rectangle
        contenedor = BoxLayout(size_hint_y=None, height=dp(1))
        with contenedor.canvas:
            Color(*_hex_a_rgba(COLOR_BORDE))
            linea = Rectangle(pos=contenedor.pos, size=contenedor.size)

        def actualizar(*_):
            linea.pos = contenedor.pos
            linea.size = contenedor.size

        contenedor.bind(pos=actualizar, size=actualizar)
        return contenedor

    def _crear_panel_resultado(self):
        from kivy.graphics import Color, RoundedRectangle
        panel = BoxLayout(
            orientation="vertical",
            spacing=dp(6),
            padding=dp(16),
            size_hint_y=None,
            height=dp(150),
        )
        with panel.canvas.before:
            Color(*_hex_a_rgba(COLOR_TARJETA_2))
            fondo = RoundedRectangle(radius=[dp(14)], pos=panel.pos, size=panel.size)

        def actualizar(*_):
            fondo.pos = panel.pos
            fondo.size = panel.size

        panel.bind(pos=actualizar, size=actualizar)

        self.etiqueta_estado = Label(
            text="Ingresa los datos y presiona [b]Calcular factura[/b]",
            markup=True,
            color=_hex_a_rgba(COLOR_TEXTO_SUAVE),
            font_size="13sp",
            halign="center",
            valign="middle",
        )
        self.etiqueta_estado.bind(size=self.etiqueta_estado.setter("text_size"))
        panel.add_widget(self.etiqueta_estado)

        self.fila_subtotal = FilaResultado(etiqueta="Subtotal", valor="—")
        self.fila_iva = FilaResultado(etiqueta="IVA (19%)", valor="—")
        self.fila_total = FilaResultado(
            etiqueta="Total a pagar", valor="—",
            color_valor=_hex_a_rgba(COLOR_ACENTO),
        )
        self.fila_fecha = FilaResultado(etiqueta="Fecha", valor="—")

        for fila in (self.fila_subtotal, self.fila_iva, self.fila_total, self.fila_fecha):
            fila.opacity = 0
            panel.add_widget(fila)

        self._panel_resultado_ref = panel
        return panel

   
    def limpiar_formulario(self, *_):
        self.campo_cliente.text = ""
        self.campo_servicios.text = ""
        self.campo_precio.text = ""
        self.campo_servicios.marcar_error(False)
        self.campo_precio.marcar_error(False)
        self._mostrar_error("")
        self.etiqueta_estado.text = "Ingresa los datos y presiona [b]Calcular factura[/b]"
        self.etiqueta_estado.opacity = 1
        for fila in (self.fila_subtotal, self.fila_iva, self.fila_total, self.fila_fecha):
            fila.opacity = 0
            fila.valor = "—"

    def _mostrar_error(self, mensaje):
        self.etiqueta_error.text = mensaje
        self.etiqueta_error.height = dp(34) if mensaje else 0

    def _formatear_moneda(self, valor: float) -> str:
        return "$ {:,.2f}".format(valor).replace(",", ".")

    def calcular_factura(self, *_):
        self.campo_servicios.marcar_error(False)
        self.campo_precio.marcar_error(False)
        self._mostrar_error("")

        nombre_cliente = self.campo_cliente.text.strip() or "Cliente"
        texto_servicios = self.campo_servicios.text.strip()
        texto_precio = self.campo_precio.text.strip()

        # Validación de campos vacíos / formato
        if not texto_servicios:
            self.campo_servicios.marcar_error(True)
            self._mostrar_error("Ingresa el número de servicios.")
            return
        if not texto_precio:
            self.campo_precio.marcar_error(True)
            self._mostrar_error("Ingresa el precio unitario.")
            return

        try:
            numero_servicios = int(texto_servicios)
        except ValueError:
            self.campo_servicios.marcar_error(True)
            self._mostrar_error("El número de servicios debe ser un entero válido.")
            return

        try:
            precio_unitario = float(texto_precio)
        except ValueError:
            self.campo_precio.marcar_error(True)
            self._mostrar_error("El precio unitario debe ser un número válido.")
            return

        # Validación de negocio (usa las mismas reglas del modelo)
        try:
            verificar_numero_servicios(numero_servicios)
        except Exception:
            self.campo_servicios.marcar_error(True)
            self._mostrar_error("El número de servicios debe ser mayor que cero.")
            return

        try:
            verificar_precio_unitario(precio_unitario)
        except Exception:
            self.campo_precio.marcar_error(True)
            self._mostrar_error("El precio unitario debe ser mayor que cero.")
            return

        # Cálculo
        subtotal = numero_servicios * precio_unitario
        total = calcular_valor_factura(numero_servicios, precio_unitario)
        iva = total - subtotal

        self.etiqueta_estado.text = f"[b]{nombre_cliente}[/b]  ·  {numero_servicios} sensor(es)"
        self.etiqueta_estado.opacity = 1

        self.fila_subtotal.valor = self._formatear_moneda(subtotal)
        self.fila_iva.valor = self._formatear_moneda(iva)
        self.fila_total.valor = self._formatear_moneda(total)
        self.fila_fecha.valor = date.today().strftime("%d/%m/%Y")

        for fila in (self.fila_subtotal, self.fila_iva, self.fila_total, self.fila_fecha):
            Animation(opacity=1, d=0.25).start(fila)


if __name__ == "__main__":
    FacturacionSensoresApp().run()