# __App movil con reconocimiento de billetes!__

###  Referencias:

Implementación SmartWebView
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

Podemos implementar el uso de esta aplicación tanto para el servidor de RetinaNet como para el de YOLOv3.
