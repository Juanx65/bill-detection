
import keras
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time
import uuid

import tensorflow as tf

import tensorflow.keras.backend as k

def get_session():
    config = tf.compat.v1.ConfigProto()
    config.gpu_options.allow_growth = True
    return tf.compat.v1.Session(config=config)

tf.compat.v1.keras.backend.set_session(get_session)

<<<<<<< Updated upstream
model_path = 'inference_30.h5'   ## replace this with your model path
=======
model_path = 'models/inference_30.h5'   ## replace this with your model path
>>>>>>> Stashed changes
#model_path = '/mnt/c/Users/ricar/Desktop'
model = models.load_model(model_path, backbone_name='resnet50')

labels_to_names = {0: '1kbill', 1:'2kbill', 2:'5kbill', 3:'10kbill',4: '20kbill'}                    ## replace with your model labels and its index value

<<<<<<< Updated upstream
image_path = 'prueba.jpeg'## replace with input image path
=======
image_path = 'images/j10.jpg'## replace with input image path
>>>>>>> Stashed changes
#image_path = '/mnt/c/Users/ricar/Desktop/ale/juan_ssd.jpeg'  ## replace with input image path
#output_path = 'C:\\Users\\Samjith.CP\\Desktop\\detected_image.jpg'   ## replace with output image path

color_class =  {0 : [71,164,33], 1: [120,12,138], 2: [234,92,129], 3: [60,124,227],4:[250,119,43]}

def solapadas(b1,b2):
<<<<<<< Updated upstream
    if(abs(b1[0]-b2[0])<50 and abs(b1[1]-b2[1])<50):
=======
    if(abs(b1[0]-b2[0])/(b1[0]+0.01)<0.1 and abs(b1[1]-b2[1])/(b1[1]+0.01)<0.1):
>>>>>>> Stashed changes
        return(True)
    return(False)

SCORE = 0.75
def detection_on_image(image_path):

        image = cv2.imread(image_path)

        draw = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = preprocess_image(image)
        image, scale = resize_image(image)
        boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
        boxes /= scale
<<<<<<< Updated upstream
=======
        
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======
        
>>>>>>> Stashed changes
        for box, score, label in finales:

            color = color_class[label]
            b = box.astype(int)
            x1,y1,x2,y2 = b
            box_w = x2 - x1
            box_h = y2 - y1
 
            draw = cv2.rectangle(draw, (x1, y1 + box_h), (x2, y1), color, 5)
            draw_box(draw, b, color=color)
            cv2.putText(draw, labels_to_names[label] + "  "+  str(round(score,3)), (b[0],b[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1.8, color, 5)

        detected_img =cv2.cvtColor(draw, cv2.COLOR_RGB2BGR)

        image_name = "results_{}.jpg".format(uuid.uuid1())
        name = "results/"+ image_name
        cv2.imwrite(name, detected_img)

        #cv2.imshow('Detection',detected_img)
        cv2.waitKey(0)
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
detection_on_image(image_path)
