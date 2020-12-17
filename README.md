## Detección de billetes
14/12/2020


Por :   Juan Aguilera ,
        Ricardo Mardones  


####  Referencias: https://github.com/puigalex/deteccion-objetos-video


### Instrucciones:
Si no tiene conda, recomendamos descargar miniconda3 y añadirlo a su path, sino usar Anaconda Prompt para navegar en los ambientes virtuales.

link de descarga:
```
https://docs.conda.io/en/latest/miniconda.html
```

###### Crear un ambiente virtual con conda y activarlo

```
conda create -n <nombre_venv> python=3.6
conda activate <nombre_venv>
```

###### Instalar PyTorch y torchvision

En caso de que tenga disponible GPU

```
pip install torch===1.5.0 torchvision===0.6.0 -f https://download.pytorch.org/whl/torch_stable.html
```

En caso de que solo se tenga disponible cpu
```
pip install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html##
```

###### Instalar los requerimientos para el entorno virtual.

```
pip install -r requirements.txt
```
###### Descargar los pesos necesarios para la deteccion en el siguiente link
```
https://drive.google.com/drive/folders/1WUfFYVQJHfnu9zykEf5jZiSoq6v-qNqy?usp=sharing
```
Donde:

Peso funcional cpu: yolov3_ckpt_97.pth

Peso funcional solo gpu: yolov3_ckpt_6.pth

Agregamos este archivo a la carpeta checkpoints

Notamos que es necesario cambiar este valor en commons.py en las lineas 59 y 65 dependiendo de el peso escogido de la siguente forma:

![Captura de el servidor web](/images_readme/pesos.png)

###### Ejecutar la siguiente linea de codigo para iniciar el webservice

```
python flaskservice.py
```
Todo listo para acceder a su webservice de manera local!

si necesita saber su direccion ip, en la cmd de windows digite

```
ipconfig
```

Esto nos dará la dirección (IPv4) al servidor que nos ayudará a ejecutar la detección de billetes.


![Captura de el servidor web](/images_readme/flaskservice.png)

##### Nos conectamos desde el navegador webpreferido, ya sea en un computador o dispositivo movil y seleccionar un archivo deseado, luego hacemos click en upload para cargarlo al servidor.



# __Disfrutar de una (aun mejorable) detección de billetes__

![Captura de el servidor web](/images_readme/flaskServiceResult.png)

# __App movil con reconocimiento de billetes!__

Adicionalmente para implementar este webservice en una aplicación movil capaz de reconocimiento de billetes chilenos, clonamos el siguiente repositorio

```
https://github.com/mgks/Android-SmartWebView
```
Abrimos el proyecto en Android Studio y cambiamos en java/MainActivity la linea 128 por lo siguiente
```
private static String ASWV_URL          = "http://192.168.0.5:5000/";
```
Donde la direccion http://192.168.0.5:5000/ corresponde a la direccion del webservice creado anteriormente.

Como se ve a continuacion

![Captura de el servidor web](/images_readme/AppMovil.png)

Queda por implementar en esta aplicación el uso de la cámara.
