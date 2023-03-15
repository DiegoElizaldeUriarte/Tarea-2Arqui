# Flask Login App

Esta es una pequeña aplicación de login Flask que valida la entrada de usuario y contraseña antes de redirigir a la página de éxito de inicio de sesión.

## Ejecutando la aplicación

Para ejecutar la aplicación, primero debe construir la imagen Docker utilizando el siguiente comando:
docker build -t flask-app .

Una vez que la imagen se haya construido correctamente, puede ejecutar el contenedor utilizando el siguiente comando:
docker run -p 5000:5000 flask-app

Esto iniciará el contenedor y lo conectará al puerto 5000 de su máquina local, lo que le permitirá acceder a la aplicación Flask en su navegador en `http://localhost:5000`.

## Uso de la aplicación

Para iniciar sesión en la aplicación, vaya a la página de inicio de sesión en `http://localhost:5000/login`. Aquí encontrará un formulario de inicio de sesión que solicita su nombre de usuario y contraseña.

El nombre de usuario debe comenzar con mayúscula y la contraseña debe contener al menos una letra y un número. Si los campos cumplen con estas condiciones, la aplicación redirigirá automáticamente a la página de inicio de sesión exitosa en http://localhost:5000/success. De lo contrario, la aplicación redirigirá de nuevo a la página de inicio de sesión en http://localhost:5000/login sin mostrar un mensaje de error.





