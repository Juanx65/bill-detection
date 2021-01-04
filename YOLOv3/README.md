# __YOLOv3 para la detección de billetes__

###  Referencias:
Repositorio usado para el entrenamiento de la red en la detección de billetes
```
https://github.com/puigalex/deteccion-objetos-video
```

### Preliminares:

Esta guía está pensada para un implementarse en un ambiente Windows/Linux. Instalar todo lo especificado en requirements.txt.

Si no tiene conda, recomendamos descargar miniconda3 y añadirlo a su path, sino desa añadirlo a su path puede usar Anaconda Prompt para navegar en los ambientes virtuales.

link de descarga:
```
https://docs.conda.io/en/latest/miniconda.html
```

#### Crear un ambiente virtual con conda y activarlo

```
conda create -n <nombre_venv> python=3.6
conda activate <nombre_venv>
```

#### Instalar PyTorch y torchvision

En caso de que tenga disponible GPU

```
pip install torch===1.5.0 torchvision===0.6.0 -f https://download.pytorch.org/whl/torch_stable.html
```

En caso de que solo se tenga disponible cpu
```
pip install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html##
```

#### Instalar los requerimientos para el entorno virtual.
Ejecutar el siguiente comando en el cmd dentro de la carpeta __bill-detection__ en el entorno virtual recién creado

```
pip install -r requirements.txt
```

### Creación dataset:

Para entrenar un modelo con las clases de billetes que tu quieras, puedes hacerlo siguiendo estas instrucciones.

Deberas crear un amplio data-set con las fotos que utilizarás para el entrenamiento.

Deberás etiquetar las imagenes con el formato .txt de Yolo darknet.

## Cambiar la configuracion del modelo
Debes dirigirte a **train-bill-detection/config** y editar **custom.data** segun la cantidad de clases que tengas, para los billetes chilenso contamos con 5 clases
```
classes = 5
```
Lo mimso para las lineas **611**, **697**, **784** del archivo **yolov3-custom.cfg** que se encuentra dentro de la misma carpeta.

## Poner las imagenes y archivos de metadata en las carpetar necesarias

Las imagenes etiquetadas tienen que estar en el directorio **trian-bill-detection/data/custom/images** mientras que las etiquetas/metadata de las imagenes tienen que estar en **trian-bill-detection/data/custom/labels**.
Por cada imagen.jpg debe de existir un imagen.txt (metadata con el mismo nombre de la imagen)


Dentro de **train-bill-detection** se deben generar los archivos ```data/custom/valid.txt``` y ```data/custom/train.txt``` que contendrán la dirección donde se encuentran cada una de las imagenes. Estos  generarán automaticamente  con el siguiente comando (estando las imagenes ya dentro de ```data/custom/images```)
```
python split_train_val.py
```

 Los pesos pre-entrenados de la red neuronal se encuentran en la carpeta se deben descargar desde el siguiente link

```
https://drive.google.com/drive/folders/1IorMOfyKyj8zoiSE2W01gzAYgcXLeqL1?usp=sharing
```
 Se deben guardar dentro de train-bill-detection en una carpeta de nombre __weights__.

## Entrenar
Para poner a entrenar el modelo se debe ejecutar la siguiente linea, el parámetro batch_size por defecto se ejecutará con un valor de 2 pero se puede modificar para trabajar con mas batches si su dispositivo lo permite.

 ```
 python train.py --model_def config/yolov3-custom.cfg --data_config config/custom.data --pretrained_weights weights/darknet53.conv.74 --batch_size 2
 ```

 Esto irá guardando nuevos pesos con checkpoints enumerados en la carperta __checkpoints__ cada vez que complete una epoca de entrenamiento. Además se generará un archivo de texto __historial_precision.txt__ en donde se registrará la precisión que se obtuvo en ese checkpoint de entrenamiento, esto es para mejorar el resultado y poder notar en qué momento del entrenamiento se comenzó a producir overfitting.
