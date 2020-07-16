import numpy as np
import os

def txt2matrix(filename='',width = 0,height = 0):
    f = open(filename)
    row_cnt = 0
    col_cnt = 0
    pic = np.zeros((height,width),dtype = np.int)
    for line in f.readlines():
        line = line.strip()
        pic[row_cnt][col_cnt] = int(line)
        col_cnt+=1
        if col_cnt>=width:
            col_cnt = 0
            row_cnt+=1
    return pic

def txt2array(filename = '',width = 0):
    f = open(filename)
    pic = np.zeros((1,width),dtype = np.int)
    col_cnt = 0
    for line in f.readlines():
        line = line.strip()
        pic[col_cnt] = int(line)
        col_cnt+=1
    return pic

def gray_fpga(filename = '',pic = [[]],width = 0,height = 0):
    f = open(filename,'w')
    for i in range(height):
        for j in range(width):
            f.write(str(pic[i][j]))
            f.write('\n')
    return  width*height


        



