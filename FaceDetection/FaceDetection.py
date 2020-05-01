# install OpenCV
# pip install opencv-python
# install numpy
# pip install numpy

# library
import cv2
import numpy as np

# Detecting obeject using casecades
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# casecades adalah sekumpulan file xml yang digunakan untuk deteksi objek

# mendeteksi objek menggunakn file cascade
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
# tangkap gambar menggunakan webcam pc yang didefinisikan pada variable camera
camera = cv2.VideoCapture(0);

# buat frame
while(True): 
# membaca gambar
 ret,img =camera.read();
#  tamabah grayscale untuk mengganti feed webcam
 gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 faces = faceDetect.detectMultiScale(gray,1.3,5);
#  dibuat ractangle dari frame.
#  dengan warna hijau
 for (x,y,w,h) in faces:
  cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),2)
#  "My Face" nama jendela dari webcame
 cv2.imshow("My Face",img);
 if(cv2.waitKey(1) ==ord('q')):
  break;
# rilis tangkapan
  camera.release()
cv2.destroyAllWindows()