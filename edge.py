import cv2
import numpy as np
import skimage.measure as measure

# 1. Load image
img = cv2.imread('/home/chiri/Documents/Image-Processing/paper.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Pre-process (blur)
blur = cv2.GaussianBlur(gray, (5,5), 0)

# 3. Edge detection
edges = cv2.Canny(blur, low_threshold, high_threshold)

# 4. Morphological ops to close holes etc
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# 5. Find contours (OpenCV) or regions (scikit-image)
contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 6. Choose the contour of interest (maybe largest area)
cnt = max(contours, key=lambda c: cv2.contourArea(c))

# 7. Compute area in pixels
area_px = cv2.contourArea(cnt)

# 8. If you have scale (pixels per cm), convert
pixels_per_cm = ...  # you figure out via calibration
area_cm2 = area_px / (pixels_per_cm**2)

print("Area in pixels:", area_px)
print("Area in cm²:", area_cm2)
