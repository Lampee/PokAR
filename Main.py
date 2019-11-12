import numpy as np
import cv2

cap = cv2.VideoCapture(0)


def rescale_frame(frame,percent=75):
    scale_percent = 75
    width = int(frame.shape[1] * scale_percent/100)
    height = int(frame.shape[0] * scale_percent/100)
    dim = (width, height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

while True:
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    frame_blur = cv2.medianBlur(frame_gray,5)

    frame_HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    white = np.array([127,127,127])
    black = np.array([255,255,155])

    frame_thres = cv2.inRange(frame_gray, 127, 255)
   

    
    


   
    cv2.imshow('frame', frame)
    cv2.imshow('frame_thres', frame_thres)
    

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()