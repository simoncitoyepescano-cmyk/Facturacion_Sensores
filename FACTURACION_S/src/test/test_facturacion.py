import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import FACTURACION_S.src.model.logica_sensores as logica_sensores

class TestsFacturacion(unittest.TestCase):
    """
    Clase utilizada para realizar las pruebas correspondientes a cada cliente, 
    teniendo en cuenta su "numero_servicios" y "precio_unitario". 
    Cada método deberá definir un "valor_total_esperado", el cual será comparado 
    con el valor calculado por el archivo "facturacion_sensores". 
    De esta manera, se podrá verificar y garantizar que la factura se genere correctamente
    y que ambos valores coincidan.
    """
    #GAMMA
    def test_comprobar_valor_gamma(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente GAMMA sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
    #Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 1741500

        #Establecer datos de salida esperada
        valor_total_esperado = 2072385
   
        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)
   
    #CORLANC_Abril
    def test_comprobar_valor_corlanc_abril(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente CORLANC en el mes de abril, sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
    #Establecer datos de entrada
        numero_servicios: int = 2
        precio_unitario: float = 241875

        #Establecer datos de salida esperada
        valor_total_esperado = 575662.5
        valor_total = round(valor_total_esperado)

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(valor_calculado,valor_total,0)

    #CORLANC_Enero_Febrero_Marzo
    def test_comprobar_valor_corlanc_enero_febrero_marzo(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente CORLANC en enero,febrero y marzo, sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
        #Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 738958

        #Establecer datos de salida esperada
        valor_total_esperado = 879360
        valor_total = round(valor_total_esperado)
   
        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)
   
        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(round(valor_calculado),valor_total)

    #LOCERIA
    def test_comprobar_valor_loceria(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente LOCERIA sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
        #Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 3483000

        #Establecer datos de salida esperada
        valor_total_esperado =  4144770

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(valor_calculado,valor_total_esperado)

    #ENKA
    def test_comprobar_valor_enka(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente ENKA sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
        #Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 1680000

        #Establecer datos de salida esperada
        valor_total_esperado = 1999200

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)

    #CRYOGAS GATEWAYS
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente CRYOGAS GATEWAYS sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
    def test_comprobar_valor_cryogas_gateways(self):
        #Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 6820000

        #Establecer datos de salida esperada
        valor_total_esperado = 8115800

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)

    #CRYOGAS SENSOR
    def test_comprobar_valor_cryogas_sensor(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente CRYOGAS SENSOR sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
        #Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 1500000

        #Establecer datos de salida esperada
        valor_total_esperado = 1785000

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA)
    def test_comprobar_valor_materiales_pinturas_sabaneta_abril(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA) en abril,
        sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
        #Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 411188

        #Establecer datos de salida esperada
        valor_total_esperado = 489314

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA)
    def test_comprobar_valor_materiales_pinturas_sabaneta_enero_febrero_marzo(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA) en enero,febrero y marzo,
        sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
        #Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 1330123

        #Establecer datos de salida esperada
        valor_total_esperado = 1582846      

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #MOLDES ITAGUI
    def test_comprobar_valor_moldes_itagui_enero_febrero_marzo(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente MOLDES ITAGUI en enero,febrero y marzo
        sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
        #Establecer datos de entrada
        numero_servicios: int = 3
        precio_unitario: float = 394110

        #Establecer datos de salida esperada
        valor_total_esperado = 1406973      

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S - CALCINACIÓN ENE FEB MAR
    def test_comprobar_valor_calcinacion_enero_febrero_marzo(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente CALCINACIÓN en enero,febrero y marzo,
        sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
        #Establecer datos de entrada
        numero_servicios: int = 3
        precio_unitario: float = 1576442

        #Establecer datos de salida esperada
        valor_total_esperado = 5627898      

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S - CALCINACIÓN ABR MAY JUN
    def test_comprobar_valor_calcinacion_abril_mayo_junio(self):
        """
        Prueba encargada de verificar que el valor total de la factura
        del cliente CALCINACIÓN en abril,mayo y junio,
        sea calculado correctamente según el número
        de servicios y el precio unitario establecidos.
        """
        #Establecer datos de entrada
        numero_servicios: int = 3
        precio_unitario: float = 145125

        #Establecer datos de salida esperada
        valor_total_esperado = 518096      

        #Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)


    # CASOS DE ERROR

    # ERROR 1 - CANTIDAD DE SERVICIOS IGUAL A CERO
    def test_error_cantidad_servicios_cero(self):
        """
        Prueba encargada de verificar que el valor total de la factura,
        sea calculado debido a que CANTIDAD DE SERVICIOS IGUAL A CERO.
        """
        # Establecer datos de entrada
        numero_servicios: int = 0
        precio_unitario: float = 241875

        # Verificar que el programa detecte el dato invalido
        with self.assertRaises(logica_sensores.ServiciosInvalidos):
            logica_sensores.calcular_valor_factura(numero_servicios, precio_unitario)


    # ERROR 2 - PRECIO UNITARIO IGUAL A CERO
    def test_error_precio_unitario_cero(self):
        """
        Prueba encargada de verificar que el valor total de la factura,
        sea calculado debido a que PRECIO UNITARIO IGUAL A CERO.
        """
        # Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 0

        # Verificar que el programa detecte el dato invalido
        with self.assertRaises(logica_sensores.PrecioInvalido):
            logica_sensores.calcular_valor_factura(numero_servicios, precio_unitario)


    # ERROR 3 - CANTIDAD DE SERVICIOS NEGATIVA
    def test_error_cantidad_servicios_negativa(self):
        """
        Prueba encargada de verificar que el valor total de la factura,
        sea calculado debido a que CANTIDAD DE SERVICIOS NEGATIVA.
        """
        # Establecer datos de entrada
        numero_servicios: int = -1
        precio_unitario: float = 241875

        # Verificar que el programa detecte el dato invalido
        with self.assertRaises(logica_sensores.ServiciosInvalidos):
            logica_sensores.calcular_valor_factura(numero_servicios, precio_unitario)


    # ERROR 4 - PRECIO UNITARIO NEGATIVO
    def test_error_precio_unitario_negativo(self):
        """
        Prueba encargada de verificar que el valor total de la factura,
        sea calculado debido a que PRECIO UNITARIO NEGATIVO.
        """
        # Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = -241875

        # Verificar que el programa detecte el dato invalido
        with self.assertRaises(logica_sensores.PrecioInvalido):
            logica_sensores.calcular_valor_factura(numero_servicios, precio_unitario)


    # CASOS DE PRUEBA EXTRAORDINARIOS

    # EXTRAORDINARIO 1 - GRAN CANTIDAD DE SERVICIOS
    def test_extraordinario_gran_cantidad_servicios(self):
        """
        Se verifica que la función calcule correctamente el valor de la factura
        cuando el cliente tiene GRAN CANTIDAD DE SERVICIOS.
        """
        # Establecer datos de entrada
        numero_servicios: int = 100
        precio_unitario: float = 1000

        # Establecer datos de salida esperada
        valor_total_esperado = 119000

        # Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios, precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado, valor_total_esperado)


    # EXTRAORDINARIO 2 - VALOR UNITARIO CON DECIMALES
    def test_extraordinario_valor_unitario_decimal(self):
        """
        Se verifica que la función calcule correctamente el valor de la factura
        cuando el cliente VALOR UNITARIO CON DECIMALES.
        """
        # Establecer datos de entrada
        numero_servicios: int = 2
        precio_unitario: float = 1250.50

        # Establecer datos de salida esperada
        valor_total_esperado = 2976.19

        # Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios, precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(valor_calculado, valor_total_esperado, 2)


    # EXTRAORDINARIO 3 - VALOR UNITARIO MUY ALTO
    def test_extraordinario_valor_unitario_alto(self):
        """
        Se verifica que la función calcule correctamente el valor de la factura
        cuando el cliente VALOR UNITARIO MUY ALTO.
        """
        # Establecer datos de entrada
        numero_servicios: int = 1
        precio_unitario: float = 10000000

        # Establecer datos de salida esperada
        valor_total_esperado = 11900000

        # Probar la funcion que resuelve problemas
        valor_calculado = logica_sensores.calcular_valor_factura(numero_servicios, precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado, valor_total_esperado)


if __name__ == '__main__':
    unittest.main()

