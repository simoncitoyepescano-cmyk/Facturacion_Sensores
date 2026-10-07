class ServiciosInvalidos(Exception):
    def __init__(self):
        super().__init__(
            "CALCULAR: Valor Factura. No es posible calcular la factura. "
            "Ingrese un valor de numero de servicios mayor que cero."
        )


class PrecioInvalido(Exception):
    def __init__(self):
        super().__init__(
            "CALCULAR: Valor Factura. No es posible calcular la factura. "
            "Ingrese un precio unitario de servicios mayor que cero."
        )


def verificar_numero_servicios(numero_servicios):
    if numero_servicios <= 0:
        raise ServiciosInvalidos()


def verificar_precio_unitario(precio_unitario):
    if precio_unitario <= 0:
        raise PrecioInvalido()


def calcular_valor_factura(numero_servicios: int, precio_unitario: float) -> float:
    verificar_numero_servicios(numero_servicios)
    verificar_precio_unitario(precio_unitario)

    porcentaje_iva = 19 / 100
    iva = porcentaje_iva * (numero_servicios * precio_unitario)
    valor_servicios = (numero_servicios * precio_unitario) + iva

    return valor_servicios