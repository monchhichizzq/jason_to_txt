
print("welcome to python-opencv")
#读取一张图片
import cv2
import numpy as np

#读取图片
# image = cv2.imread("frame_depth_001.png")
#窗口显示
#
#灰度图
img = cv2.imread('/Users/babalia/Desktop/json parsing/frame_depth_008.png')
# #或者以下方式：0表示灰度图
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

shape = img_grey.shape
px = img_grey[1000, 200]
print('gray', img_grey,shape)


np.savetxt("a.txt",img_grey) #缺省按照'%.18e'格式保存数据，以空格分隔
np.loadtxt("a.txt")



