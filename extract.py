import json
import os, json
import numpy as np

# 读取文件路径
path_depth = "/Users/babalia/Desktop/json/depth_txt"
# 返回指定的文件夹包含的文件或文件夹的名字的列表
list_depth = os.listdir(path_depth)
# 给文件排序
list_depth.sort()
print(list_depth)

# 读取文件路径
path_to_json = '/Users/babalia/openpose/output_color/'
# 返回指定的文件夹包含的文件或文件夹的名字的列表
f = os.listdir(path_to_json)
# 给文件排序
f.sort()
print(f)
# 只读取json文件并存入列表
json_files = [pos_json1 for pos_json1 in f if pos_json1.endswith('.json')]
print(json_files)

# 文件序号， 文件名， 枚举列表中的文件
for index_depth, num in enumerate(list_depth):
    # 打开文件（文件夹路径加文件名）
    with open(os.path.join(path_depth, num)) as f:
        # 读取txt文件数据存入矩阵
        matrix_depth = np.loadtxt(f)
        # print(matrix_depth.shape)

# index 是 json_files的序列， js是他的名称
        # 文件序号， 文件名， 枚举列表中的文件
        for index, js in enumerate(json_files):
            # 打开文件（文件夹路径加文件名）
            with open(os.path.join(path_to_json, js)) as json_file:
                    # 读取json文件数据存入矩阵
                    data = json.load(json_file)
                    # 读取json文件中"pose_keypoints_2d"后的2d坐标
                    a = data["people"][0]["pose_keypoints_2d"]
                    hand_left = data["people"][0]["hand_left_keypoints_2d"]
                    hand_right = data["people"][0]["hand_right_keypoints_2d"]
                    # 在数列延展加入左手和右手坐标
                    a.extend(hand_left)
                    a.extend(hand_right)
                    # print(type(a), np.shape(a))
                    # 创建一个零数列
                    skeleton = [0.0] * 67 * 2  # 116 is the number of total number of points
                    # print(np.size(b))
                    k = 2  # k is the probability value index
                    j = 0
                    l = 0
                    m = 1
                    for i in range(len(a)):
                        if (i != k):  # this is not to write the probability
                            skeleton[j] = a[i]
                            j = j + 1
                        else:
                            k = k + 3
                    # 创建一个零数列
                    skeleton_depth = [0.0] * 67
                    # 在depth矩阵中找到joints对应的深度值
                    for i in range(len(skeleton_depth)):
                        for j in range(len(skeleton)):
                            if j%2 == 0:
                                # print(j)
                                # print(skeleton[j+1])
                                # print(skeleton[j])
                                skeleton_depth[i] = matrix_depth[int(skeleton[j+1]),int(skeleton[j])]

                    # print(skeleton_depth)
    # Save txt files
    file = open('/Users/babalia/Desktop/json/depth_extract/%i.txt' % index_depth, 'w')
    file.write(str(skeleton_depth))

    # file.close()