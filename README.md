# Temporal-median
In this repository ,we are using  "Temporal median filter" with opencv in cpp.

##The General steps of the thermal(or temporal median) median filter is :
###  1. Convert the background template to grayscale
###  2. Loop all the frames  of the video.then extract the current frame,and convert it to grayscale.
###  3. Calcule the absolute diffrence between the current frame and the background model.
###  4. Apply threshold to remove noise and binarize the output(only 0 and 1 or only 0 and 255)


-_CREATOR: mortza_-
