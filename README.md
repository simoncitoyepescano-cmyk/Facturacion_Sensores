# 🧾 Sistema de Facturación de Sensores

## 📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de una función para calcular el **valor a pagar por la facturación de servicios de sensores de una empresa**.

El proyecto fue desarrollado tomando como base **facturas reales proporcionadas por la empresa**, utilizando principalmente el número de servicios y el valor unitario registrados en ellas para comprobar que los resultados obtenidos por el programa fueran correctos.

Además, en el repositorio se encuentra un **audio en el que se explica el proceso de facturación por sensores de la empresa**, permitiendo conocer el contexto del proceso que se está representando mediante el programa.

---

## 🎯 Objetivo

El objetivo principal es desarrollar y probar una función que permita calcular correctamente el valor total a pagar por los servicios de sensores, teniendo en cuenta la cantidad de servicios, el valor unitario y el IVA correspondiente.

También se busca comprobar el funcionamiento del programa mediante **pruebas unitarias**, incluyendo pruebas basadas en facturas reales, casos de error y casos extraordinarios.

---

## ⚙️ Funcionamiento

El programa recibe dos valores de entrada:

* 🔢 **Número de servicios:** cantidad de servicios o sensores que se deben facturar.
* 💰 **Valor unitario:** valor correspondiente a cada servicio.

El sistema calcula automáticamente el IVA del **19%** y lo agrega al valor de los servicios.

### 🧮 Operación

**Valor a pagar = (Número de servicios × Valor unitario) + ((Número de servicios × Valor unitario) × 19%)**

---

## 📥 Valores de entrada

| Entrada                    | Descripción                                             |
| -------------------------- | ------------------------------------------------------- |
| 🔢 **Número de servicios** | Cantidad de servicios de sensores que se deben facturar |
| 💰 **Valor unitario**      | Valor correspondiente a cada servicio                   |

---

## 📤 Valor de salida

| Salida               | Descripción                                            |
| -------------------- | ------------------------------------------------------ |
| 💵 **Valor a pagar** | Valor total de los servicios incluyendo el IVA del 19% |

---

## 🧾 IVA

Para el proceso de facturación analizado en este proyecto se utiliza un **IVA fijo del 19%**.

El IVA es calculado automáticamente por el programa a partir del valor obtenido de multiplicar el número de servicios por el valor unitario.

---

## 🧪 Pruebas unitarias

Las pruebas fueron desarrolladas utilizando **Python y la librería `unittest`**.

Una parte importante de las pruebas se realizó utilizando información obtenida de **facturas reales de la empresa**. Estas contienen diferentes cantidades de servicios y valores unitarios, permitiendo comprobar que el programa genere los valores esperados.

Entre las facturas utilizadas para las pruebas se encuentran registros de diferentes clientes como:

* Gamma
* Corlanc
* Locería
* Enka
* Cryogas
* Suministros de Colombia S.A.S.
* Materiales y Pinturas Sabaneta
* Moldes Itagüí
* Calcinación

El objetivo es verificar que los resultados calculados por el programa coincidan con los valores esperados de las facturas.

---

## ❌ Casos de error

Además de las pruebas realizadas con las facturas, se desarrollaron **4 casos de error** para comprobar el comportamiento del sistema cuando se ingresan datos inválidos.

Los casos son:

### 🔴 Error 1 — Número de servicios igual a 0

Se comprueba que el sistema no permita realizar una facturación cuando la cantidad de servicios es igual a `0`.

### 🔴 Error 2 — Valor unitario igual a 0

Se comprueba que el sistema no permita utilizar un valor unitario igual a `0`.

### 🔴 Error 3 — Número de servicios negativo

Se comprueba que el sistema rechace una cantidad negativa de servicios, ya que no es posible facturar una cantidad negativa.

### 🔴 Error 4 — Valor unitario negativo

Se comprueba que el sistema rechace un valor unitario negativo, ya que un servicio no puede tener un precio negativo.

Estos casos permiten comprobar que el programa no solamente realice operaciones matemáticas, sino que también tenga en cuenta la **validación de los datos de entrada**.

---

## 🟣 Casos de prueba extraordinarios

También se realizaron **3 casos de prueba extraordinarios**. Estos casos no representan errores, sino situaciones diferentes a los valores utilizados normalmente en las facturas.

### 🟣 Extraordinario 1 — Gran cantidad de servicios

Se prueba el funcionamiento del programa utilizando **100 servicios** con un valor unitario de **$1.000**.

El objetivo es comprobar que el sistema pueda trabajar correctamente con una cantidad de servicios mucho mayor a las utilizadas en las facturas de referencia.

### 🟣 Extraordinario 2 — Valor unitario con decimales

Se prueba el sistema utilizando **2 servicios** con un valor unitario de **$1.250,50**.

Este caso permite comprobar que el programa pueda trabajar correctamente con valores unitarios que contienen decimales.

### 🟣 Extraordinario 3 — Valor unitario muy alto

Se prueba el sistema utilizando **1 servicio** con un valor unitario de **$10.000.000**.

El objetivo es comprobar que la función pueda manejar correctamente valores unitarios considerablemente superiores a los utilizados en las facturas de referencia.

### 📊 Resumen de pruebas especiales

| Tipo              | Caso                  | Objetivo                         |
| ----------------- | --------------------- | -------------------------------- |
| 🔴 Error          | Servicios = `0`       | Validar cantidad de servicios    |
| 🔴 Error          | Precio = `0`          | Validar valor unitario           |
| 🔴 Error          | Servicios negativos   | Rechazar cantidades inválidas    |
| 🔴 Error          | Precio negativo       | Rechazar valores inválidos       |
| 🟣 Extraordinario | 100 servicios         | Probar una cantidad elevada      |
| 🟣 Extraordinario | Precio decimal        | Probar valores con decimales     |
| 🟣 Extraordinario | Precio de $10.000.000 | Probar un valor unitario elevado |

---

## 🎧 Explicación del proceso

Dentro del repositorio se encuentra un **audio relacionado con el proyecto**.

En este audio se explica el **proceso de facturación por sensores de la empresa**, proporcionando el contexto necesario para comprender cómo funciona el servicio y de dónde provienen los datos utilizados para realizar las pruebas.

El audio complementa la información presentada en el código, las facturas y las pruebas unitarias.

---
# 📂 Estructura del repositorio

El proyecto está organizado dentro de la carpeta principal FACTURACION_S, donde se encuentran los archivos de documentación, la información utilizada para las pruebas y el código fuente del sistema.

```
FACTURACION_S/
│
├── 📄 README.md
│   └── Documentación general del proyecto
│
├── 🎧 Audio
│   └── Explicación del proceso de facturación por sensores
│
├── 📊 Archivo de Excel
│   └── Información de facturas, casos de error y pruebas
│
└── 📁 src/
    │
    ├── 🧠 model/
    │   ├── __init__.py
    │   └── facturacion_sensores.py
    │
    ├── 🧪 test/
    │   ├── __init__.py
    │   └── test_facturacion.py
    │
    └── 🖥️ view/
        ├── __init__.py
        └── consola_sensores.py
```
        
## 📄 README.md

Contiene la documentación general del proyecto, incluyendo:

Descripción del sistema.
Objetivo.
Funcionamiento.
Valores de entrada y salida.
Cálculo del IVA.
Pruebas realizadas.
Casos de error.
Casos extraordinarios.
Estructura del proyecto.
Futuras implementaciones.
Información de los autores.

## 🎧 Audio

Contiene la explicación del proceso de facturación por sensores de la empresa.

El audio permite comprender el proceso real que sirvió como base para desarrollar el sistema y realizar las diferentes pruebas.

## 📊 Archivo de Excel

Contiene la información utilizada como referencia para el desarrollo del proyecto, incluyendo los datos obtenidos de las facturas de la empresa, así como la información de los casos de error y casos de prueba.

## 🧠 model

Contiene la lógica principal del sistema.

__init__.py → Permite identificar la carpeta como un paquete de Python.

facturacion_sensores.py → Contiene la función encargada de realizar el cálculo de la facturación y las validaciones de los datos de entrada.

## 🧪 test

Contiene las pruebas unitarias del proyecto.

__init__.py → Permite identificar la carpeta como un paquete de Python.

test_facturacion.py → Contiene las pruebas basadas en las facturas reales, los 4 casos de error y los 3 casos extraordinarios.

## 🖥️ view

Contiene la parte encargada de la interacción con el usuario.

__init__.py → Permite identificar la carpeta como un paquete de Python.

consola_sensores.py → Contiene la interfaz de consola para interactuar con el sistema de facturación.

## 🔗 Organización general

La estructura del proyecto permite separar claramente cada responsabilidad:

📊 Información → 🧠 Model → 🖥️ View → 🧪 Test

De esta manera:

📊 Excel: proporciona la información de referencia.

🧠 Model: realiza los cálculos y validaciones.

🖥️ View: permite la interacción mediante consola.

🧪 Test: comprueba que el sistema funcione correctamente.

🎧 Audio: explica el proceso real de facturación.

📄 README: documenta todo el proyecto.

---

## 🚀 Futuras implementaciones

Como futura mejora del proyecto, se busca implementar los **meses del servicio como una variable de entrada**.

Actualmente, los datos utilizados fueron establecidos principalmente con base en las **facturas reales proporcionadas por la empresa**. Por esta razón, el número de meses no se maneja actualmente como una entrada independiente y el sistema está limitado a las situaciones representadas en las facturas utilizadas.

Al implementar los meses como una variable de entrada, el programa podría adaptarse de una manera más flexible a diferentes periodos de facturación.

### 🔮 Posibles mejoras

* 📅 Permitir ingresar la cantidad de meses del servicio.
* 🔄 Adaptar el cálculo a diferentes periodos de facturación.
* 🧮 Realizar cálculos más dinámicos.
* 📈 Aumentar la variedad de casos de prueba.
* ⚙️ Representar de una manera más completa el proceso real de facturación de la empresa.

---

## 💻 Tecnologías utilizadas

| Tecnología      | Uso                                       |
| --------------- | ----------------------------------------- |
| 🐍 **Python**   | Desarrollo del programa                   |
| 🧪 **unittest** | Creación y ejecución de pruebas unitarias |
| 🐙 **GitHub**   | Almacenamiento y gestión del proyecto     |

---

## 📚 Metodología

El proyecto se desarrolló siguiendo el siguiente proceso:

**Facturas reales → Identificación de datos → Desarrollo de la función → Pruebas con facturas → Casos de error → Casos extraordinarios → Análisis de resultados**

De esta manera, el proyecto combina información real de la empresa con pruebas diseñadas para comprobar diferentes comportamientos del sistema.

---

## 👥 Autores

**Simon Yepes Cano** - 
**Cesar Junior Ramirez**

---

## 📌 Conclusión

El proyecto permite representar de manera sencilla el proceso de **facturación de servicios de sensores de una empresa**, utilizando como referencia información obtenida de facturas reales.

Las pruebas unitarias permiten comprobar que los cálculos realizados por el programa sean correctos, mientras que los **4 casos de error** permiten validar el comportamiento del sistema frente a datos inválidos.

Por otra parte, los **3 casos extraordinarios** permiten comprobar que el programa también pueda trabajar correctamente con situaciones diferentes a las encontradas normalmente en las facturas.

Como futura mejora, se plantea incorporar los **meses del servicio como una variable de entrada**, haciendo que el sistema sea más flexible y pueda adaptarse a diferentes periodos de facturación.
