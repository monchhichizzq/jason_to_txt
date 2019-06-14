import os,os.path,shutil
import numpy as np
import sys
import math
import time


# 打开文件
path_joints = "/Users/babalia/Desktop/json/txt/"
path_depth = "/Users/babalia/Desktop/json/depth_txt"
list_joints = os.listdir(path_joints)
list_depth = os.listdir(path_depth)

list_joints.sort()
list_depth.sort()

print(list_joints)
print(list_depth)

for x, frame in enumerate(list_joints):

    with open(os.path.join(path_joints, frame)) as file:
        a = np.loadtxt(file)


