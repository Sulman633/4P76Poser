import urllib.request
import cv2
import sys
import numpy as np


def getImage():
    url = 'http://192.168.0.3:8080/shot.jpg'
    try:
        with urllib.request.urlopen(url) as response:
            imgResp = response.read()
    except:
        print("Please start server up for IP Webcam.")
    imgNp = np.array(bytearray(imgResp), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    
    cv2.imwrite(sys.path[0] + '\..\images\LiveTest\cap.jpg', img)
getImage()    






