from datetime import date
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import FACTURACION_S.src.model.logica_sensores as logica_sensores

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
    def __init__(self,nombre_cliente: str, numero_servicios: int, precio_sensor: float):
        self.nombre_cliente = nombre_cliente
        self.numero_servicios = numero_servicios
        self.precio_sensor = precio_sensor

    def detalles_compra(self):
        """
        Devuelve una cadena de texto con el resumen de la compra del cliente,
        mostrando su nombre, la cantidad de sensores activos, el precio de cada
        sensor y el valor total que debe pagar.
        """
        return f"Cliente: {self.nombre_cliente} \nSensores activos: {self.numero_servicios} \nPrecio de cada sensor: {self.precio_sensor} \n---------------------------- \nValor a pagar: {logica_sensores.calcular_valor_factura(self.numero_servicios,self.precio_sensor)}"

print("\n")

nombre_cliente = input("Ingrese el nombre del cliente: ")
numero_servicios = int(input("Ingrese el número de sensores activos que posee el cliente: "))
precio_sensor = float(input("Ingrese el valor de cada sensor: "))

print("\n")
print("-----------------------")
print("MENU")
print("-----------------------")
print("1. Calcular valor factura")
print("2. Generar factura")
print("3. Salir")
print("-----------------------")
print("\n")
opcion_calcular = int(input("Ingrese la opción a realizar: "))
print("--------------------------------------------")

while opcion_calcular != 3:
    if opcion_calcular == 1:
        cliente_actual = Cliente(nombre_cliente,numero_servicios,precio_sensor)
        print(f"El valor a pagar por {cliente_actual.nombre_cliente} es de {logica_sensores.calcular_valor_factura(numero_servicios,precio_sensor)}$")
        print("--------------------------------------------")
        print("\n")

    elif opcion_calcular == 2:
        hoy=date.today()
        print(f"Factura realizada el {hoy}")
        valor_antes_iva = numero_servicios * precio_sensor
        print(f"Valor antes de IVA: {valor_antes_iva}$") 
        valor_iva_aplicado = valor_antes_iva * 0.19
        print(f"Valor IVA aplicado: {valor_iva_aplicado}$")
        valor_total = valor_antes_iva + valor_iva_aplicado
        print(f"Valor total a pagar: {valor_total}$")
        cliente_actual= Cliente(nombre_cliente,numero_servicios,precio_sensor)
        print(cliente_actual.detalles_compra())
        print("--------------------------------------------")
        print("\n")

    elif opcion_calcular == 3:
        print("Hasta luego")
        print("\n")
        break
        
    opcion_calcular = int(input("Ingrese otra opción a realizar: "))
    print("---------------------------------------------")
