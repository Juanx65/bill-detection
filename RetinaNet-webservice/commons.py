import keras
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
import matplotlib.pyplot as plt
import cv2
import os
import sys
import numpy as np
import time
import uuid

import tensorflow as tf

import tensorflow.keras.backend as k

def Convertir_RGB(img):
    # Convertir Blue, green, red a Red, green, blue
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b
    return img

def Convertir_BGR(img):
    # Convertir red, blue, green a Blue, green, red
    r = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 2].copy()
    img[:, :, 0] = b
    img[:, :, 1] = g
    img[:, :, 2] = r
    return img

def convertir_divisas(cant_total,div_in,div_out):
    dicc_divisas = {"CLP":{"USD": 0.0014, "EUR": 0.0011, "CNY": 0.0089},
                    "USD": { "CLP":735.20 , "EUR": 0.82, "CNY": 6.55 },
                    "EUR":{ "CLP": 893.51, "USD": 1.22, "CNY": 7.96},
                    "CNY":{"CLP": 112.26 , "USD":0.15 ,"EUR": 0.13}
                    }
    if div_in != div_out:
        cant_out = round(cant_total*dicc_divisas[div_in][div_out],4)
    else:
        cant_out = cant_total
    return cant_out

# funciones Retinanet

def get_session():
    config = tf.compat.v1.ConfigProto()
    config.gpu_options.allow_growth = True
    return tf.compat.v1.Session(config=config)

def solapadas(b1,b2):
    if(abs(b1[0]-b2[0])<50 and abs(b1[1]-b2[1])<50):
        return(True)
    return(False)


def detection_on_image(img):

        tf.compat.v1.keras.backend.set_session(get_session)

        SCORE = 0.7

        color_class =  {0 : [71,164,33], 1: [120,12,138], 2: [234,92,129], 3: [60,124,227],4:[250,119,43]}
        labels_to_names = {0: '1kbill', 1:'2kbill', 2:'5kbill', 3:'10kbill',4: '20kbill'}
        dicc_clases = {0: 1000, 1: 2000, 2: 5000, 3: 10000, 4: 20000}


        model_path = '/mnt/c/Users/juan_/Desktop/PDI_git/bill-detection/RetinaNet-webservice/models/inference_48.h5' #juan
        #model_path = "/mnt/c/Users/ricar/Desktop/PDI/bill-detection/RetinaNet-webservice/models/inference_37.h5"
        model = models.load_model(model_path, backbone_name='resnet50')

        dinero = list()
        #image = cv2.imread(image_path)
        image = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_UNCHANGED)
        draw = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = preprocess_image(image)
        image, scale = resize_image(image)#,768,1024) #resize_image(img, min_side=768, max_side=1024):
        boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
        boxes /= scale

        validos = []
        for box, score, label in zip(boxes[0], scores[0], labels[0]):
            if score < SCORE:
                break
            validos.append((box,score,label))
        finales = []
        comp = []
        for box1, score1, label1 in validos:
            agregar = True
            comp = [k for k in finales]
            for box2,score2,label2 in comp:
                if(solapadas(box1,box2)):
                    if(score2 >= score1):
                        agregar = False
                        break
                    else:
                        finales.remove((box2,score2,label2))
            if(agregar):
                finales.append((box1,score1,label1))

        for box, score, label in finales:

            color = color_class[label]
            b = box.astype(int)
            x1,y1,x2,y2 = b
            box_w = x2 - x1
            box_h = y2 - y1

            if box_h*box_w > 4100:
                draw = cv2.rectangle(draw, (x1, y1 + box_h), (x2, y1), color, 5)
                draw_box(draw, b, color=color)
                cv2.putText(draw, labels_to_names[label] + "  "+  str(round(score,3)), (b[0],b[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1.8, color, 5)
                dinero.append(dicc_clases[label])
                print(labels_to_names[label],score)
                detected_img =cv2.cvtColor(draw, cv2.COLOR_RGB2BGR)

        image_name = "results_{}.jpg".format(uuid.uuid1())
        name = "static/"+ image_name
        cv2.imwrite(name,detected_img )
        #cv2.imshow('Detection',detected_img)
        #cv2.waitKey(0)
        cant_total =  sum(dinero)

        return image_name,cant_total


#detection_on_image(image_path)
