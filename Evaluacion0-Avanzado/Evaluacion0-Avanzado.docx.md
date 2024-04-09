![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.001.png)

**Evaluación: Sobre la linea de comandos**

**Objetivos**

Linux, siendo un sistema operativo tipo Unix, es ampliamente utilizado en servidores, supercomputadoras y sistemas distribuidos. Conocer la línea de comandos de Linux permite comprender y manipular el sistema operativo subyacente en el que se ejecutan sus aplicaciones concurrentes y distribuidas, ofreciendo una comprensión profunda de su entorno de ejecución.

La línea de comandos de Linux es una herramienta poderosa para la automatización de tareas repetitivas y la gestión eficiente de recursos del sistema. Podemos aprender a escribir scripts para automatizar la compilación y ejecución de sus programas, la gestión de procesos, el monitoreo del uso de recursos y la implementación de sistemas. Esta habilidad es invaluable en entornos de computación distribuida, donde la gestión manual de múltiples nodos y servicios puede ser tediosa y propensa a errores.

Muchas herramientas esenciales para el desarrollo, la prueba y la depuración de software en computación concurrente y distribuida son accesibles a través de la línea de comandos. Esto incluye herramientas para control de versiones (como **git**), empaquetado y despliegue de software (como **make** y **docker**), y monitoreo de rendimiento y recursos (como **top**, **vmstat**, y **netstat**) . Familiarizarse con estas herramientas es esencial para el desarrollo de software eficiente.

El conocimiento de la línea de comandos es fundamental para interactuar con servicios en la nube y sistemas distribuidos, muchos de los cuales ofrecen interfaces basadas en CLI (Command Line Interface) para su gestión y configuración. Aprenderemos a desplegar, configurar y monitorear aplicaciones distribuidas en entornos cloud, utilizando la línea de comandos.

La línea de comandos promueve un entendimiento más profundo de cómo funcionan los computadores y las redes, alentando a todos a pensar y resolver problemas de manera algorítmica. Esta forma de pensamiento es transferible a muchos otros ámbitos de la informática y la ingeniería de software.

**Instrucciones de Entrega:**

- Realiza todos los pasos de cada sección en la terminal, capturando capturas de pantalla
  - copiando el texto de la terminal que demuestre la ejecución de la sección Learning the Shell de la página: <https://linuxcommand.org/lc3_learning_the_shell.php>
- Crea un documento en markdown que incluya una breve explicación de cada tarea, junto con las capturas de pantalla o texto correspondiente.
- Subir el documento final a tu repositorio personal hasta el día 13 de abril (23:59).

**Navigation**

**Comandos: pwd, cd, ls**

**Comando: *pwd* (print working directory)**

Este comando muestra el directorio de trabajo actual en el que nos situamos (el cual es 'ubuntu').

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.002.png)

**Comando: *ls***

Este comando muestra los directorios y/o archivos contenidos en el directorio actual en el que nos situamos.

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.003.png)

**Comando: *cd***

Este comando nos permite cambiar o movernos entre los distintos directorios existentes.

- Acceso Absoluta

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.004.png)

- Acceso relativa

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.005.png)

**Looking Around**

**Comandos: ls, less, file Comando: *ls***

Este comando lista los directorios y/o archivos existentes.

**ls: Solo muestra los archivos y/o directorios del directorio de trabajo actual.**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.006.png)

**ls /bin: Muestra los archivos y/o directorios del directorio /bin.**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.007.jpeg)

**ls -l: Muestra los archivos y/o directorios del directorio actual en formato 'long'.**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.008.png)

**ls -l /etc /bin: Muestra los archivos y/o directorios de los directorios /bin y /etc en formato 'long'.**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.009.jpeg)

**ls -la: Muestra los archivos y/o directorios (incluyendo los ocultos) en formato 'long'.**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.010.jpeg)**ls -l -a: Muestra los archivos y/o directorios (incluyendo los ocultos por el -a) en formato 'long' (es igual a 'ls -la').**

- **CONSIDERACIÓN - COMANDO: 'ls -la ..' o 'ls -l -a ..'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.011.png)

Los dos puntos '..' hacen referencia al directorio que contiene al directorio 'vanesa', es decir, 'home'. En otras palabras, se obtienen los archivos y/o directorios ocultos y no ocultos del directorio 'home'. 'home' en este caso, puesto que dependerá del directorio actual en donde se encuentre el usuario.

**Comando: *less***

Este comando permite visualizar archivos de texto mediante un visualizador de archivos de texto.

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.012.png)

**Comando: *file***

Este comando permite indicar el tipo y/o formato de un archivo

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.013.png)

**A Guided Tour**

**Directorio root: '/'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.014.png)

**Directorio boot: '/boot'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.015.png)

**Directorio etc: '/etc/**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.016.jpeg)

**‘bin' y 'usr/bin': '/bin' '/usr/bin'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.017.jpeg)

**'sbin' y 'usr/sbin': '/sbin' '/usr/sbin'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.018.jpeg)

**Directorio usr: '/usr'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.019.png)

**Directorio user/local: '/usr/local'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.020.png)

**Directorio var: '/var'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.021.png)

**lib: '/lib'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.022.jpeg)

**Directorio home: '/home'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.023.png)

**Directorio root: '/root'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.024.png)

**Directorio tmp: '/tmp'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.025.png)

**Directorio dev: '/dev'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.026.jpeg)

**Directorio proc: '/proc'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.027.jpeg)

**Directorio media: '/media'**

![](Aspose.Words.befddf99-87e5-4bed-bfaf-22ddccfc246e.028.png)

Manipulating Files

Esta lección presentará los siguientes comandos:

- [**cp**](https://linuxcommand.org/lc3_man_pages/cp1.html)- copiar archivos y directorios
- [**mv**](https://linuxcommand.org/lc3_man_pages/mv1.html)- mover o cambiar el nombre de archivos y directorios
- [**~~rm~~**](https://linuxcommand.org/lc3_man_pages/rm1.html)- eliminar archivos y directorios
- [**mkdir**](https://linuxcommand.org/lc3_man_pages/mkdir1.html)- crea directorios
