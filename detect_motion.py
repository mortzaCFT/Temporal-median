# Motion detection with thermal median filter.
# This script will use this method, to see what objects is moving(detect motion).

#The General steps of the thermal(or temporal median) median filter is :
#  1. Convert the background template to grayscale
#  2. Loop all the frames  of the video.then extract the current frame,and convert it to grayscale.
#  3. Calcule the absolute diffrence between the current frame and the background model.
#  4. Apply threshold to remove noise and binarize the output(only 0 and 1 or only 0 and 255)

# This script can used by everyone.Feel free to any changes.
import numpy as np
import cv2
import sys

TEXT_COLOR = (0, 255, 0)
TRACKER_COLOR = (255, 0, 0)
FONT = cv2.FONT_HERSHEY_SIMPLEX
VIDEO_SOURCE = cv2.VideoCapture(0) 

BGS_TYPES = ["GMG", "MOG", "MOG2", "KNN", "CNT"]
BGS_TYPE = BGS_TYPES[2]

def getKernel(KERNEL_TYPE):
    if KERNEL_TYPE == "dilation":
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    if KERNEL_TYPE == "opening":
        return np.ones((3, 3), np.uint8)
    if KERNEL_TYPE == "closing":
        return np.ones((3, 3), np.uint8)

def getFilter(img, filter):
    if filter == 'closing':
        return cv2.morphologyEx(img, cv2.MORPH_CLOSE, getKernel("closing"), iterations=2)
    if filter == 'opening':
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, getKernel("opening"), iterations=2)
    if filter == 'dilation':
        return cv2.dilate(img, getKernel("dilation"), iterations=2)
    if filter == 'combine':
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, getKernel("closing"), iterations=2)
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, getKernel("opening"), iterations=2)
        dilation = cv2.dilate(opening, getKernel("dilation"), iterations=2)
        return dilation

#Background substraction: 
#Is any technique that allows the foreground of the image extracted for futhrer processing.
def getBGSubtractor(BGS_TYPE):
    if BGS_TYPE == "GMG":
        return cv2.bgsegm.createBackgroundSubtractorGMG()
    if BGS_TYPE == "MOG":
        return cv2.bgsegm.createBackgroundSubtractorMOG()
    if BGS_TYPE == "MOG2":
        return cv2.createBackgroundSubtractorMOG2()
    if BGS_TYPE == "KNN":
        return cv2.createBackgroundSubtractorKNN()
    if BGS_TYPE == "CNT":
        return cv2.bgsegm.createBackgroundSubtractorCNT()
    print("Invalid detector")
    sys.exit(1)

cap = cv2.VideoCapture(VIDEO_SOURCE)
bg_subtractor = getBGSubtractor(BGS_TYPE)
minArea = 250

def main():
    while True:
        ok, frame = cap.read()
      #IF SOURCE was video.use this:
       # if not ok:
        #    print("Finished processing the video")
         #   break

        frame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)

        bg_mask = bg_subtractor.apply(frame)
        bg_mask = getFilter(bg_mask, 'combine')
        bg_mask = cv2.medianBlur(bg_mask, 5)

        contours, _ = cv2.findContours(bg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area >= minArea:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (10, 30), (250, 55), (255, 0, 0), -1)
                cv2.putText(frame, 'Motion detected!', (10, 50), FONT, 0.8, TEXT_COLOR, 2, cv2.LINE_AA)

                for alpha in np.arange(0.8, 1.1, 0.9)[::-1]:
                    frame_copy = frame.copy()
                    output = frame.copy()
                    cv2.drawContours(frame_copy, [cnt], -1, TRACKER_COLOR, -1)
                    frame = cv2.addWeighted(frame_copy, alpha, output, 1 - alpha, 0, output)

        result = cv2.bitwise_and(frame, frame, mask=bg_mask)
        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', result)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

if __name__ == '__main__':
 main()
  
