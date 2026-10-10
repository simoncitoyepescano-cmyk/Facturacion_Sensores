class Cliente:
  """
  Clase que representa a un cliente y almacena la información necesaria
  para realizar el cálculo del valor de los servicios que debe pagar.
  "cliente": Es una cadena de texto que contiene el nombre o identificador
  del cliente.
  "n_servicios": Es un entero que indica la cantidad de servicios o sensores
  que tiene contratados actualmente el cliente.
  "precio_sensor": Es un flotante que representa el precio unitario de cada
  sensor o servicio, el cual puede variar dependiendo del cliente.
  """
  def __init__(self,nit:str,nombre_cliente: str, numero_servicios: int, precio_sensor: float):
      self.nit = nit
      self.nombre_cliente = nombre_cliente
      self.numero_servicios = numero_servicios
      self.precio_sensor = precio_sensor

  def is_equal(self, otro: Cliente) -> bool:
      """ Verifica cada atributo de self contra otra
      instancia de esta clase y dispara una excepción si no
      son iguales"""

      assert (self.nit == otro.nit)
      assert (self.nombre_cliente == otro.nombre_cliente)
      assert (int(self.numero_servicios) == int(otro.numero_servicios))
      assert (float(self.precio_sensor) == float(otro.precio_sensor))
      
      return True

  #El metodo detalles compra se hace dentro de la clase cliente ya que son los detalles de la compra realizada por el mismo
  def detalles_compra(self):
      """
      Devuelve una cadena de texto con el resumen de la compra del cliente,
      mostrando su nombre, la cantidad de sensores activos, el precio de cada
      sensor y el valor total que debe pagar.
      """
      calcular_factura = self.calcular_valor_factura(self.numero_servicios,self.precio_sensor)
      return f"Cliente: {self.nit} - {self.nombre_cliente} \nSensores activos: {self.numero_servicios} \nPrecio de cada sensor: {self.precio_sensor} \n---------------------------- \nValor a pagar: {calcular_factura}"

def calcular_valor_factura(numero_servicios:int,precio_sensor:float)->float:
  """Devuelve un float que contiene el valor de servicios que debera pagar cada Cliente
  según su "numero de servicios" y el "precio unitario" de cada sensor multiplicandolo por
  un valor fijo del iva que seria el 19%.
  "numero_servicios": Es un entero que contiene el número de servicios que estan siendo
  utilizados actualmente por la empresa.
  "precio_sensor": Es un flotante que contiene el precio unitario de cada sensor
  que podria variar según el cliente."""

  porcentaje_iva = 19/100 #VALOR FIJO PUESTO POR LA EMPRESA
  
  iva = porcentaje_iva * (numero_servicios * precio_sensor)
  valor_servicios = (numero_servicios * precio_sensor) + iva

  if precio_sensor < 0:
    raise PrecioInvalido

  if numero_servicios < 0:
    raise ServiciosInvalidos

  if numero_servicios == 0:
      raise ServiciosInvalidos

  if precio_sensor == 0:
    raise PrecioInvalido
  
  return valor_servicios


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

def verificar_precio_sensor(precio_sensor):
  if precio_sensor <= 0:
    raise PrecioInvalido()

