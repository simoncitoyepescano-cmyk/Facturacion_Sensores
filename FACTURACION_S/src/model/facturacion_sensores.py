class ServiciosInvalidos(Exception):
  """Se lanza cuando la cantidad de servicios ingresada es 0 o menor. Indica que no se puede calcular la factura sin servicios válidos."""
  def __init__(self):
    super().__init__(self, "CALCULAR: Valor Factura. No es posible calcular la factura. Ingrese un valor de numero de servicios mayor que cero.")

class PrecioInvalido(Exception):
  """Se lanza cuando el precio unitario de los servicios es 0 o menor. Indica que no se puede calcular la factura con un precio inválido."""
  def __init__(self):
    super().__init__(self, "CALCULAR: Valor Factura. No es posible calcular la factura. Ingrese un precio unitario de servicios mayor que cero.")

def verificar_numero_servicios(numero_servicios):
  if numero_servicios <= 0:
    raise ServiciosInvalidos()

def verificar_precio_unitario(precio_unitario):
  if precio_unitario <= 0:
    raise PrecioInvalido()

def calcular_valor_factura(numero_servicios:int,precio_unitario:float)->float:
  """Devuelve un float que contiene el valor de servicios que debera pagar cada Cliente
  según su "numero de servicios" y el "precio unitario" de cada sensor multiplicandolo por
  un valor fijo del iva que seria el 19%.
  "numero_servicios": Es un entero que contiene el número de servicios que estan siendo
  utilizados actualmente por la empresa.
  "precio_unitario": Es un flotante que contiene el precio unitario de cada sensor
  que podria variar según el cliente."""

  porcentaje_iva = 19/100 #VALOR FIJO PUESTO POR LA EMPRESA
  
  iva = porcentaje_iva * (numero_servicios * precio_unitario)
  valor_servicios = (numero_servicios * precio_unitario) + iva

  return valor_servicios
