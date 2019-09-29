import numpy as np
import cv2

# Reading the input image
image = cv2.imread("Indian_grocers.jpg")
aspect_ratio = (image.shape[0]) / (image.shape[1])
width = int((image.shape[0]) * (20 / 100) * aspect_ratio)
height = int((image.shape[1]) * (20 / 100) * aspect_ratio)
img_Copy = cv2.resize(image, (width, height))
img_dup = img_Copy.copy()

# Converting the input image to grayscale
gray = cv2.cvtColor(img_Copy, cv2.COLOR_BGR2GRAY)

# Applying Gaussian Blur on the grayscale image
smooth_img = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny edge detection
edged = cv2.Canny(smooth_img, 75, 255)
cv2.imshow('Canny', edged)

# Contours of the edged detected image and drawing the contours
(_, contours, _) = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break

cv2.drawContours(img_dup, [screenCnt], -1, (255, 0, 0), 2)
cv2.imshow('draw contours', img_dup)

# Perspective transform
sq_screenCnt = np.squeeze(screenCnt)
src_pts = sq_screenCnt.astype(np.float32)
dst_pts = np.float32([[0,0],[0, 600],[400, 600],[400,0]])

Matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
Warped = cv2.warpPerspective(img_dup, Matrix, (400,600))

cv2.imshow("warped", Warped)
cv2.imwrite("Transformed.jpg", Warped)
#cv2.waitKey(0)