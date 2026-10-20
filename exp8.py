import cv2
from matplotlib import pyploy as pit
image=cv2.imread(r"lionel-messi-football-barcelona-hd-wallpaper-preview.jpg",flag)

if image is None:
	print("error,couldn't reaf image)
else:
	print("image loaded successfuly")


cv2.inwrite("lionel-messi-football-barcelona-hd-wallpaper-preview.jpg",image)
print("image saved image window",image):
cv2.waitkey(0)
cv2.destroyAllwindows()


