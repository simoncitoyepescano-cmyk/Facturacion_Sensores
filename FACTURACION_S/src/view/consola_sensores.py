from datetime import date
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import FACTURACION_S.src.model.logica_sensores as logica_sensores

nit = input("Ingrese el nit del cliente: ")
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

cliente_actual = logica_sensores.Cliente(nit,nombre_cliente,numero_servicios,precio_sensor)
calcular_factura = cliente_actual.calcular_valor_factura(numero_servicios,precio_sensor)
                                          
while opcion_calcular != 3:
    if opcion_calcular == 1:
        print(f"El valor a pagar por {cliente_actual.nombre_cliente} es de {calcular_factura}$")
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
        print(cliente_actual.detalles_compra())
        print("--------------------------------------------")
        print("\n")

    elif opcion_calcular == 3:
        print("Hasta luego")
        print("\n")
        break
        
    opcion_calcular = int(input("Ingrese otra opción a realizar: "))
    print("---------------------------------------------")
