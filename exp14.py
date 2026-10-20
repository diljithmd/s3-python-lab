import cv2
#image=cv2.imread pyplot as plt
# Note: The line 'image = cv2.imread pyplot as plt' seems to be a mistake or leftover text.
# The actual image loading happens in the next line.
image = cv2.imread(r"dd.jpeg", 1)

if image is None:
    print("Error: could not read the image. check the file path")
else:
    print("image loaded successfully")
    cv2.imwrite("gecp.jpeg", image)
    print("image saved")
    cv2.imshow("OpenCV image window", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()