# Temporal-median
In this repository ,we are using  "Temporal median filter" with opencv in cpp.

_The General steps of the thermal(or temporal median) median filter is :
 1. Convert the background template to grayscale
 2. Loop all the frames  of the video.then extract the current frame,and convert it to grayscale.
 3. Calcule the absolute diffrence between the current frame and the background model.
 4. Apply threshold to remove noise and binarize the output(only 0 and 1 or only 0 and 255)

_Documents that will help about bacground substracion:

    # https://docs.opencv.org/3.4/d1/d5c/classcv_1_1bgsegm_1_1BackgroundSubtractorGMG.html

    # https://docs.opencv.org/3.4/d6/da7/classcv_1_1bgsegm_1_1BackgroundSubtractorMOG.html

    # https://docs.opencv.org/3.4/d7/d7b/classcv_1_1BackgroundSubtractorMOG2.html

    # https://docs.opencv.org/3.4/db/d88/classcv_1_1BackgroundSubtractorKNN.html

    # https://docs.opencv.org/3.4/de/dca/classcv_1_1bgsegm_1_1BackgroundSubtractorCNT.html


 _Documents that will help,anyone*:
 
    # https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html
    
    # https://www.pyimagesearch.com/2021/01/19/opencv-bitwise-and-or-xor-and-not/



-_CREATOR: mortza_-
