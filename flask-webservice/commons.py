#alguna wea 13/12/20
from __future__ import division
from models import *
from utils.utils import *
from utils.datasets import *
import os
import sys
import argparse
import io

import uuid

import torchvision.transforms as transforms
import numpy as np

import cv2
from PIL import Image
import torch
from torch.autograd import Variable

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

def get_detection(img):

    dinero = list()
    dicc_clases = {"1kbill" : 1000, "2kbill": 2000, "5kbill": 5000, "10kbill": 10000, "20kbill": 20000}

    model_def="config/yolov3-custom.cfg"
    class_path="data/custom/classes.names"
    weights_path="checkpoints/yolov3_ckpt_97.pth"
    conf_thres=0.8
    nms_thres=0.4
    batch_size=1
    n_cpu=0
    img_size=416
    checkpoint_model="checkpoints/yolov3_ckpt_97.pth"

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("cuda" if torch.cuda.is_available() else "cpu")
    model = Darknet(model_def, img_size=img_size).to(device)
    model.load_state_dict(torch.load(weights_path))

    model.eval()
    classes = load_classes(class_path)
    classes.append('5kbill')
    #print(classes)
    Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

    frame = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_UNCHANGED)

    colors = np.random.randint(0, 255, size=(len(classes), 3), dtype="uint8")
    #frame = cv2.resize(frame, (1280, 960), interpolation=cv2.INTER_CUBIC)
    #LA imagen viene en Blue, Green, Red y la convertimos a RGB que es la entrada que requiere el modelo
    RGBimg=Convertir_RGB(frame)
    imgTensor = transforms.ToTensor()(frame)
    imgTensor, _ = pad_to_square(imgTensor, 0)
    imgTensor = resize(imgTensor, 416)
    imgTensor = imgTensor.unsqueeze(0)
    imgTensor = Variable(imgTensor.type(Tensor))


    with torch.no_grad():
        detections = model(imgTensor)
        detections = non_max_suppression(detections, conf_thres, nms_thres)


    for detection in detections:
        if detection is not None:
            detection = rescale_boxes(detection, img_size, RGBimg.shape[:2])
            for x1, y1, x2, y2, conf, cls_conf, cls_pred in detection:
                box_w = x2 - x1
                box_h = y2 - y1
                dinero.append(classes[int(cls_pred)])
                color = [int(c) for c in colors[int(cls_pred)]]
                print("Se detectó {} en X1: {}, Y1: {}, X2: {}, Y2: {}".format(classes[int(cls_pred)], x1, y1, x2, y2))
                frame = cv2.rectangle(frame, (x1, y1 + box_h), (x2, y1), color, 5)
                cv2.putText(frame, classes[int(cls_pred)], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 5)# Nombre de la clase detectada
                cv2.putText(frame, str("%.2f" % float(conf)), (x2, y2 - box_h), cv2.FONT_HERSHEY_SIMPLEX, 0.5,color, 5) # Certeza de prediccion de la clase
    #
    #Convertimos de vuelta a BGR para que cv2 pueda desplegarlo en los colores correctos

    cant_total = 0
    for billete in dinero:
        cant_total += dicc_clases[billete]

    frame = Convertir_BGR(frame)
    image_name = "result_{}.jpg".format(uuid.uuid1())
    name = "static/"+image_name
    cv2.imwrite(name,frame)

    return image_name,cant_total
