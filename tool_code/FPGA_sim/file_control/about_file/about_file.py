import numpy as np
import os
import random
import sys
from math import *
from PIL import Image,ImageDraw


def txt2matrix(filename='',width = 0,height = 0):
    """
    Input:filename is the input txt filepath
          width and height is the picture width and height
    Return:a list of picture data match the col and row
    """
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
    """
    Return:a list of txt data(one line)
    """
    f = open(filename)
    pic = np.zeros((1,width),dtype = np.int)
    col_cnt = 0
    for line in f.readlines():
        line = line.strip()
        pic[0][col_cnt] = int(line)
        col_cnt+=1
    return pic

def gray_fpga(filename = '',pic = [[]],width = 0,height = 0):
    """
    Input: filename
    Input: picture data
    Input: width = pic_width
    Input: Height = pic_height
    Return:generate the fpga sim picture data
    """
    f = open(filename,'w')
    for i in range(height):
        for j in range(width):
            f.write(str(bin(pic[i][j]))[2:])
            f.write('\n')
    return  width*height

def binary(filename = '',pic = [[]],width = 0,height = 0):
    """
    Return:generate the fpga sim picture data
    Input: pic = binary_picture
    Input: finename = data store address
    """
    f = open(filename,'w')
    for i in range(height):
        for j in range(width):
            if(pic[i][j]>0):
                f.write(str(1))
                f.write('\n')
            else:
                f.write(str(0))
                f.write('\n')
    return  width*height

def draw_pic(label_list = [],colors = {},pic = [[]],path = ''):
    """
    Input: path = result stored address
    Input: pic = labeled binary picture
    Input: label_list = the label appeared in the color
    Return: return a visual conmonent picture that different label compared different color
    """
    height,width = np.shape(pic)
    output_img = Image.new('RGB',(width,height))
    handle = output_img.load()
    for val in label_list[0]:
        if val not in colors and val != 0:
            colors[val] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    for i in range(height):        
        for j in range(width):
            handle[j,i] = colors.get(pic[i][j],(0,0,0))
    output_img.save(path)
    output_img.show()
    return True

def nrgb(r = 0,g = 0,b = 0):
    sum = 0
    sum = int(r)+int(g)+int(b)
    if sum == 0:
        return (0,0,0)
    else:
        return(r*256//sum,g*256//sum,b*256//sum)

def coe(path = ''):
    f = open(path+'outdata.coe','w')
    f.write('memory_initialization_radix = 2;\n')
    f.write('memory_initialization_vector =\n')
    for i in range(65536):
        if(i == 0):
            f.write('00000000000000000000')
            f.write('\n')
        elif(i == 65535):
            a = log10(i)
            f.write(fpga_log10(c = a)+';')         
        else:
            a = log10(i)
            f.write(fpga_log10(c = a)+',')
            f.write('\n')

def coe2(path = ''):
    f = open(path+'outdata2.coe','w')
    f.write('memory_initialization_radix = 2;\n')
    f.write('memory_initialization_vector =\n')
    for i in range(int(1048576/8)):
        if(i == 1048576//8 - 1):
            f.write('1111111111111111;')
            f.write('\n')      
        else:
            a =8*i/131072
            a = 10**(a)
            if a <= 65535:
                f.write(fpga_exp10(c = a)+',')
                f.write('\n')
            else:
                f.write('1111111111111111,')
                f.write('\n')      




        
def fpga_log10(c = 0,b_num = 20):
    c = c*131072
    c = int(c)
    c = bin(c)
    c = c[2:]
    result = ''
    num = b_num - len(c)
    for i in range(num):
        c = '0' + c
    result = result + c
    return result

def fpga_exp10(c = 0,b_num = 16):
        c = int(c)
        c= bin(c)
        c = c[2:]
        result = ''
        num = b_num - len(c)
        for i in range(num):
            c = '0' + c
        result = result + c
        return result
        





#def fpga_log10(c = 0.0,b_num = 16):
#    a = int(c)
#    b = c-a
#    result = ''
#    c = bin(a)
#    if(len(c)==3):
#        result = result + '00'+ c[2:3]
#    elif(len(c) == 4):
#        result = result + '0'+ c[2:4]
#    elif(len(c) == 5):
#        result = result + c[2:5]
#    else:
#        print('somethin wrong')
#    for i in range(b_num):
#        b *= 2
#        result = result + str(int(b))
#        b = b - int(b)
#    return result

