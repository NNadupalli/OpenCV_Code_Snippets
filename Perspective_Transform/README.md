# Perspective Transform Description:

This porject is based on "https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/"

## How the code works:

- Convert an image to grayscale
- Finds the edges of the grayscale image using Canny Edge Detector
- Find the approximate contour of the object of interest (grocery receipt in my example) 
- Apply perspective transform of the 4 corners of the receipt obtained by detecting contours.


## Using OpenCV 3.4.4 and python 3.6



