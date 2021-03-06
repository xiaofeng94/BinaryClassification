# import cv2

# fileName = 'D:/Baidu/BaiduDownload/20170712/2017-07-12-105036.mov'
# cap = cv2.VideoCapture(fileName)

# # weight = cap.get(3) #weight
# # height = cap.get(4) #height
# # fps = cap.get(5) #fps
# # frame_count = cap.get(7) #frame count

# # print('weight,height:' + str(weight) + ',' + str(height))
# # print('fps:' +  str(fps))
# # print('frame_count:' + str(frame_count))

# ret,frame1 = cap.read()
# win = cv2.namedWindow('frame 1', flags=0) 
# cv2.imshow('frame 1', frame1) 

# cap.set(1,12000)
# ret,frame200 = cap.read()
# win = cv2.namedWindow('frame 8000', flags=0) 
# cv2.imshow('frame 8000', frame200) 

# ret,frame200 = cap.read()
# win = cv2.namedWindow('frame 8000', flags=0) 
# cv2.imshow('frame 8000', frame200) 


# # ret,frame = cap.read()

# # win = cv2.namedWindow('frame win', flags=0) 
# # cv2.imshow('frame win', frame) 

# # image = cv2.resize(frame,(600,400))
# # win = cv2.namedWindow('image win', flags=0) 
# # cv2.imshow('image win', image) 

# cv2.waitKey(0)

# cap.release()  
# cv2.destroyAllWindows()

###################################################

# import os
# import os.path
# rootdir = 'D:/Baidu/BaiduDownload/20170712'                                   # 指明被遍历的文件夹

# for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#     for dirname in dirnames:                       #输出文件夹信息
#         print("parent is:" + parent)
#         print("dirname is:" + dirname)

#     for filename in filenames:                        #输出文件信息
#         print("parent is:" + parent)
#         print("filename is:" + filename)
#         print("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息


# from generator import *
# videoName = 'D:/Baidu/BaiduDownload/2017-07-13/2017-07-13 151123.mov' 
# saveRoot = 'D:/Baidu/BaiduDownload/20170712/data/2017-07-13-151123'
# filePrefix = ''
# generateData(videoName, saveRoot, filePrefix)

# from generator import *
# targetFileName = '2017-07-13-151123-test.txt'
# rootDir = saveRoot
# label = 1
# generateTxt(targetFileName, rootDir, label)

# ###########################

# from generator import *
# #get negtive samples
# videoName = 'D:/Baidu/BaiduDownload/20170712/2017-07-12-103818.mov'
# saveRoot = 'D:/Baidu/BaiduDownload/20170712/data/'
# filePrefix = 'negtive-test'
# generateData(videoName, saveRoot, filePrefix, 23)

# from generator import *
# targetFileName = 'negtive-test.txt'
# rootDir = 'D:/Baidu/BaiduDownload/20170712/data/negtive-test'
# label = 0
# generateTxt(targetFileName, rootDir, label)

# from generator import *
# targetFileName = 'positive-test.txt'
# rootDir = 'D:/Baidu/BaiduDownload/20170712/data/positive-test'
# label = 1
# generateTxt(targetFileName, rootDir, label) 

import numpy as np
import matplotlib.pyplot as plt

plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2
x = np.linspace(0, 3, 100)
for i in np.arange(5):
    plt.figure(1)  #❶ # 选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #❷ # 选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))
plt.show()

from generator import *
#get positive samples
videoName = 'D:/Baidu/BaiduDownload/2017-07-17/2017-07-17 074648.mov'
saveRoot = 'F:/DeepLearning/Caffe/caffe/examples/forklift_classification/data/2017-07-17-074648'
filePrefix = '2017-07-17-074648'
generateData(videoName, saveRoot, filePrefix, 15)