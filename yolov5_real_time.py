from importlib.resources import path
from time import time
import torch 
from matplotlib import pyplot as plt

import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5','custom',path='buraya best.pt modelinizin dosya yolunu yapıştırın',force_reload=True)
#aşağıdaki gibi olacak 
#model = torch.hub.load('ultralytics/yolov5','custom',path='C:\\Users\\Lenovo\\Desktop\\wetransfer_otonom2023_test_kodlari_2023-01-26_1342\\OTONOM2023_TEST_KODLARI\\goruntuisleme\\best.pt',force_reload=True)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    start = time()
    ret, frame = cap.read()
    result = model(frame)
    cv2.imshow('Screen',np.squeeze(result.render()))
    if cv2.waitKey(10) & 0xff == ord('x'):
        break
    if cv2.getWindowProperty("Screen",cv2.WND_PROP_VISIBLE) < 1:
        break
    
    end = time()
    fps = 1/(end - start)
    print(fps)
cap.release() 
cv2.destroyAllWindows()

