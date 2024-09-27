
# 🌐 Verificador de Disponibilidad de  Sitios Web

Bienvenido al proyecto **Verificador de Disponibilidad de  Sitios Web**. Este programa permite a los usuarios verificar la conectividad de un sitio web ingresando una URL en una interfaz gráfica simple.


## Descripción del Proyecto 📝

Este proyecto está desarrollado en Python usando la biblioteca `tkinter` para crear una interfaz gráfica de usuario (GUI). Los usuarios pueden ingresar una URL y el programa comprobará su disponibilidad utilizando el módulo `urllib`.

### Funciones principales:

- Verificar la conectividad de un sitio web ingresando su URL.
- Mostrar un mensaje de error si la URL no tiene un formato válido.
- Informar si el sitio web está disponible o no basándose en el código de estado HTTP.

## Cómo Usar 🚀

### Pasos para ejecutar el programa:

1. Clona o descarga este repositorio en tu máquina local.
2. Asegúrate de tener Python 3 instalado.
3. Ejecuta el archivo `main.py` para iniciar la aplicación.

### Requisitos 🛠️

- **Python 3.x**
- **tkinter** (incluido en la instalación estándar de Python)

No se requiere instalación de paquetes externos adicionales.

## ¿Cómo Funciona la Comprobación de Conectividad? 🌐

1. **Ingresar una URL**: El usuario ingresa una URL en la casilla de texto y hace clic en el botón "Comprobar" para verificar la conectividad.
2. **Validar la URL**: La función `es_url_valida(url)` verifica si la URL tiene el formato correcto usando una expresión regular. Si no es válida, se muestra un mensaje de error.
3. **Conexión a la URL**: Si la URL es válida, el programa intenta conectarse al sitio web usando `urllib.request.urlopen()`.
4. **Verificar el Código de Estado HTTP**: Si el código de estado HTTP es 200, significa que el sitio está disponible y el programa lo muestra en la interfaz gráfica. Si no, se muestra el error correspondiente.
5. **Mostrar los Resultados**: El resultado de la comprobación se muestra en la interfaz gráfica, indicando si el sitio está en línea o si ocurrió algún error.

### Validación de URL:

La función `es_url_valida(url)` utiliza una expresión regular para validar URLs de la siguiente forma:

- Debe comenzar con `http://` o `https://` (si no está presente, el programa lo agrega automáticamente).
- Debe tener un dominio válido, como `example.com`.

### Funciones del Programa 🛠️

- `es_url_valida(url)`: Valida si una URL tiene el formato correcto.
- `comprobar_conectividad()`: Verifica la conectividad del sitio web y maneja posibles errores como URL incorrecta, error de HTTP o fallo en la conexión.

## Ejemplo de Uso 🖥️

1. Abre la aplicación.
2. Introduce una URL (por ejemplo, `https://www.google.com`) en la caja de texto.
3. Haz clic en "Comprobar".
4. El resultado se mostrará en la parte inferior indicando si el sitio está disponible o si hubo algún error.

## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto:

1. Realiza un **fork** del repositorio.
2. Crea una nueva rama para tus cambios (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus modificaciones y asegúrate de que los cambios sean funcionales.
4. Haz un **commit** de tus cambios (`git commit -m 'Agregada nueva funcionalidad'`).
5. Envía tus cambios a tu repositorio en GitHub (`git push origin feature/nueva-funcionalidad`).
6. Crea una solicitud de extracción (**pull request**) a este repositorio principal.

## Autor 👤

**[Tu Nombre]** 🚀

- GitHub: [JCMeloza](https://github.com/JCMeloza)
- Correo Electrónico: [melozajuancarlos@gmail.com](mailto:melozajuancarlos@gmail.com)

## Licencia 📜

Este proyecto está bajo la Licencia MIT - consulta el archivo `LICENSE.md` para más detalles.
