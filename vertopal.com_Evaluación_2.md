---
jupyter:
  colab:
    private_outputs: true
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .markdown id="JaB2T3TqgnPE"}
\#**Refactoring Techniques**

\##**1. Extract Method** Separar bloques de código en métodos con
nombres descriptivos hacer el código más claro y modular, facilitando la
identificación de secciones que pueden ejecutarse en paralelo o
requieren sincronización.
:::

::: {.cell .markdown id="ftKcAaekhPeG"}
En este código, la función `printOwing` imprime un banner y luego
imprime los detalles directamente dentro de la misma función. Los
detalles incluyen el nombre y la cantidad pendiente.
:::

::: {.cell .code id="E-BUP-tYfzlJ"}
``` python
def printOwing(self):
    self.printBanner()

    # print details
    print("name:", self.name)
    print("amount:", self.getOutstanding())
```
:::

::: {.cell .markdown id="f9d2IWFniR5S"}
En este código, la función `printOwin` también imprime un banner, pero
en lugar de imprimir los detalles directamente, llama a otra función
`printDetails` para hacerlo. La función printDetails toma una cantidad
pendiente como argumento y luego imprime el nombre y la cantidad
pendiente.
:::

::: {.cell .code id="lL2mW8M1gMQ-"}
``` python
def printOwing(self):
    self.printBanner()
    self.printDetails(self.getOutstanding())

def printDetails(self, outstanding):
    print("name:", self.name)
    print("amount:", outstanding)
```
:::

::: {.cell .markdown id="nR_IPwssi2XD"}
## **2. Inline method** {#2-inline-method}

Fusionar métodos que son demasiado granulares puede reducir la
sobrecarga de llamadas a métodos en ambientes de alta concurrencia,
mejorando el rendimiento.
:::

::: {.cell .code id="63slCK3XjJ2h"}
``` python
class PizzaDelivery:
    # ...
    def getRating(self):
        return 2 if self.moreThanFiveLateDeliveries() else 1

    def moreThanFiveLateDeliveries(self):
        return self.numberOfLateDeliveries > 5
```
:::

::: {.cell .markdown id="EDWWy_Bdjwhq"}
Es muy reduntante crear dos funciones cuando se puede crear una funcion.
Código utiliza un método adicional para hacer la comprobación de las
entregas tardías,
:::

::: {.cell .code id="-1yW7FT2ja2C"}
``` python
class PizzaDelivery:
  # ...
  def getRating(self):
    return 2 if self.numberOfLateDeliveries > 5 else 1
```
:::

::: {.cell .markdown id="1DkPovzwk029"}
Código hace la comprobación directamente dentro del método `getRating`.
:::

::: {.cell .markdown id="hcB2hiUbmyZi"}
## **3. Extract variable** {#3-extract-variable}

Extraer expresiones en variables puede ayudar a identificar datos
compartidos entre threads, lo cual es crucial para evitar condiciones de
carrera.
:::

::: {.cell .code id="4Uow0Pc9m5Hm"}
``` python
def renderBanner(self):
    if (self.platform.toUpperCase().indexOf("MAC") > -1) and \
       (self.browser.toUpperCase().indexOf("IE") > -1) and \
       self.wasInitialized() and (self.resize > 0):
        # do something
```
:::

::: {.cell .markdown id="ntJr61HFnVUF"}
El problema principal es no definir correctamente ya que

    self.platform.toUpperCase().indexOf("MAC") > -1)

se puede almacenar en una variable. Asi, podemos lograr que sea código
limpio.
:::

::: {.cell .code id="lngTrjP0nRYP"}
``` python
def renderBanner(self):
    isMacOs = self.platform.toUpperCase().indexOf("MAC") > -1
    isIE = self.browser.toUpperCase().indexOf("IE") > -1
    wasResized = self.resize > 0

    if isMacOs and isIE and self.wasInitialized() and wasResized:
        # do something
```
:::

::: {.cell .markdown id="JUlI7l8GwZcE"}
En este caso en

    isMacOs = self.platform.toUpperCase().indexOf("MAC") > -1

al almacenar en una variable es mas claro y en la condición. Es más
claro.
:::

::: {.cell .markdown id="_QknR7Hot6jF"}
## **4. Replace temp with Query** {#4-replace-temp-with-query}

Fomenta el uso de métodos para calcular valores en lugar de variables
temporales, lo cual puede simplificar la sincronización de acceso a
datos entre múltiples threads.
:::

::: {.cell .code id="iy14xATZuBAh"}
``` python
def calculateTotal():
    basePrice = quantity * itemPrice
    if basePrice > 1000:
        return basePrice * 0.95
    else:
        return basePrice * 0.98
```
:::

::: {.cell .markdown id="BpzJG70lxCNg"}
El código no esta claro. Debe existir dos funciones uno para calcular el
total y el otro para el hallar el precio.
:::

::: {.cell .code id="eyndOHzzt27r"}
``` python
def calculateTotal():
    if basePrice() > 1000:
        return basePrice() * 0.95
    else:
        return basePrice() * 0.98

def basePrice():
    return quantity * itemPrice
```
:::

::: {.cell .markdown id="mCfow6-mxWg7"}
En este caso, al existir dos funciones. Es mas entendible y que claro el
codigo.
:::

::: {.cell .markdown id="24TV5EQcuCQn"}
## **5. Remove assignments to parameters** {#5-remove-assignments-to-parameters}

Modificar parámetros dentro de una función puede llevar a efectos
secundarios inesperados en un entorno concurrente; evitarlo hace que el
código sea más seguro en términos de concurrencia.
:::

::: {.cell .code id="7J3MIHOjxhld"}
``` python
def discount(inputVal, quantity):
    if quantity > 50:
        inputVal -= 2
```
:::

::: {.cell .markdown id="Kva1Rfjzx2to"}
Primero, si un parámetro se pasa mediante referencia, luego de que el
valor del parámetro se cambia dentro del método, este valor se pasa al
argumento que solicitó llamar a este método. . El problema empeora si su
parámetro y su contenido están documentados pero el valor real puede
diferir de lo esperado dentro del método.
:::

::: {.cell .code id="QYL-CtJSxh5H"}
``` python
def discount(inputVal, quantity):
    result = inputVal
    if quantity > 50:
        result -= 2
    # ...
```
:::

::: {.cell .markdown id="6w9_NfjtyBUv"}
En este caso ya se solucione al guardar el inpuVal en result.
:::

::: {.cell .markdown id="r9IjwEHbuaYP"}
\##**6. Replace method with method object** Convierte métodos en objetos
que pueden ser ejecutados en paralelo, facilitando la división del
trabajo y la gestión del estado local de cada tarea.
:::

::: {.cell .code id="5ZgfNw62ufSF"}
``` python
class Order:
    # ...
    def price(self):
        primaryBasePrice = 0
        secondaryBasePrice = 0
        tertiaryBasePrice = 0
        # Perform long computation.
```
:::

::: {.cell .markdown id="xLaWvw8aycyM"}
Un método es demasiado largo y no se puede separar debido a masas
enredadas de variables locales que son difíciles de aislar entre sí.
:::

::: {.cell .code id="nPv0IeJvyZ45"}
``` python
class Order:
    # ...
    def price(self):
        return PriceCalculator(self).compute()


class PriceCalculator:
    def __init__(self, order):
        self._primaryBasePrice = 0
        self._secondaryBasePrice = 0
        self._tertiaryBasePrice = 0
        # Copy relevant information from the
        # order object.

    def compute(self):
        # Perform long computation.
```
:::

::: {.cell .markdown id="Bz_rDxsnyotG"}
En primer lugar, esto permite aislar el problema a nivel de clase. En
segundo lugar, allana el camino para dividir un método grande y difícil
de manejar en otros más pequeños que de todos modos no encajarían con el
propósito de la clase original.
:::

::: {.cell .markdown id="07Ot-Dj9ujEx"}
## **7. Split Temporary Variable** {#7-split-temporary-variable}

Evita la reutilización de variables temporales en contextos donde
múltiples threads pueden modificarlas, reduciendo así el riesgo de
condiciones de carrera.
:::

::: {.cell .code id="WIr7q6NSuokr"}
``` python
temp = 2 * (height + width)
print(temp)
temp = height * width
print(temp)
```
:::

::: {.cell .markdown id="uXnYfUwRzBnr"}
Tiene una variable local que se usa para almacenar varios valores
intermedios dentro de un método (excepto las variables de ciclo)
:::

::: {.cell .code id="CTzDrB3Sy0FD"}
``` python
perimeter = 2 * (height + width)
print(perimeter)
area = height * width
print(area)
```
:::

::: {.cell .markdown id="ufTlivPSzC2j"}
Utilice diferentes variables para diferentes valores. Cada variable debe
ser responsable de una sola cosa en particular.
:::

::: {.cell .markdown id="_yb3J67huowU"}
## **8. Encapsulate Collection** {#8-encapsulate-collection}

Encapsular colecciones y proveer métodos para su acceso y modificación
puede ayudar a controlar cómo y cuándo se accede a datos compartidos,
facilitando la sincronización.
:::

::: {.cell .markdown id="tDtEbBTPzfjM"}
<https://refactoring.guru/images/refactoring/diagrams/Encapsulate%20Collection%20-%20Before.png>
:::

::: {.cell .markdown id="ku2rxSD20DEm"}
Una clase contiene un campo de colección y un captador y definidor
simple para trabajar con la colección.
:::

::: {.cell .markdown id="WoJZesbx0G3U"}
<https://refactoring.guru/images/refactoring/diagrams/Encapsulate%20Collection%20-%20After.png>
:::

::: {.cell .markdown id="IQm12zOU0HCA"}
Haga que el valor devuelto por el captador sea de solo lectura y cree
métodos para agregar/eliminar elementos de la colección.
:::

::: {.cell .markdown id="YdrSLcZ_ut1L"}
## **9. Replace Conditional with Polymorphism** {#9-replace-conditional-with-polymorphism}

Utilizar polimorfismo en lugar de condicionales para manejar
comportamientos basados en tipos puede simplificar el código y mejorar
su extensibilidad, lo cual es útil cuando se diseñan sistemas
distribuidos que deben ser flexibles y escalables.
:::

::: {.cell .code id="unfj0-g2uyiQ"}
``` python
class Bird:
    # ...
    def getSpeed(self):
        if self.type == EUROPEAN:
            return self.getBaseSpeed()
        elif self.type == AFRICAN:
            return self.getBaseSpeed() - self.getLoadFactor() * self.numberOfCoconuts
        elif self.type == NORWEGIAN_BLUE:
            return 0 if self.isNailed else self.getBaseSpeed(self.voltage)
        else:
            raise Exception("Should be unreachable")
```
:::

::: {.cell .markdown id="p2U9_DLn0cPF"}
Tiene un condicional que realiza varias acciones según el tipo de objeto
o las propiedades
:::

::: {.cell .code id="A9Gz3kOY0iA-"}
``` python
class Bird:
    # ...
    def getSpeed(self):
        pass

class European(Bird):
    def getSpeed(self):
        return self.getBaseSpeed()


class African(Bird):
    def getSpeed(self):
        return self.getBaseSpeed() - self.getLoadFactor() * self.numberOfCoconuts


class NorwegianBlue(Bird):
    def getSpeed(self):
        return 0 if self.isNailed else self.getBaseSpeed(self.voltage)

# Somewhere in client code
speed = bird.getSpeed()
```
:::

::: {.cell .markdown id="ZglV8npa0n-g"}
Crea subclases que coincidan con las ramas del condicional. En ellos,
cree un método compartido y mueva el código de la rama correspondiente
del condicional a él. Luego reemplace el condicional con la llamada al
método relevante. El resultado es que la implementación adecuada se
logrará mediante polimorfismo dependiendo de la clase de objeto.
:::

::: {.cell .markdown id="KwV-9g1nuywR"}
## **10. Introduce Parameter Object** {#10-introduce-parameter-object}

Agrupar parámetros relacionados en objetos puede simplificar la firma de
los métodos y mejorar la organización del código, lo que es
especialmente útil en operaciones distribuidas que requieren múltiples
datos de entrada.
:::

::: {.cell .markdown id="DQu5_oZ603wu"}
<https://refactoring.guru/images/refactoring/diagrams/Introduce%20Parameter%20Object%20-%20Before.png>
:::

::: {.cell .markdown id="BU34L6RX0z_-"}
Sus métodos contienen un grupo repetido de parámetros.
:::

::: {.cell .markdown id="gGBGM0cn0-Ym"}
<https://refactoring.guru/images/refactoring/diagrams/Introduce%20Parameter%20Object%20-%20After.png>
:::

::: {.cell .markdown id="jAUJvqsD026Z"}
Reemplace estos parámetros con un objeto.
:::
