import json
import os, json
import numpy as np



path_to_json = '/Users/babalia/Desktop/DTW/Gesture_data/drill/drill_e_02.mp4'
f = os.listdir(path_to_json)
f.sort()
print(f)
json_files = [pos_json1 for pos_json1 in f if pos_json1.endswith('.json')]
print(json_files)
for x, js in enumerate(json_files):

    with open(os.path.join(path_to_json, js)) as json_file:
        data = json.load(json_file)
    print(type(data))
    a = data["people"][0]["pose_keypoints_2d"]
    hand_left = data["people"][0]["hand_left_keypoints_2d"]
    hand_right = data["people"][0]["hand_right_keypoints_2d"]
    a.extend(hand_left)
    a.extend(hand_right)
    #print(type(a), np.shape(a))
    b = [0.0]*67*2  # 116 is the number of total number of points
    # print(np.size(b))
    k = 2         # k is the probability value index
    j = 0
    l = 0
    m = 1
    for i in range(len(a)):
        if ( i != k ): # this is not to write the probability
            b[j] = a[i]
            j = j+1
        else:
            k = k+3

    file = open('/Users/babalia/Desktop/DTW/Gesture_data/drill_txt/drill_2/%i.txt' %x,'w')
    while (l < len(b)):
        file.write(str(b[l]))
        l = l+2
        file.write(" " + str(b[m]) +"\n")
        m = m+2

    file.close()