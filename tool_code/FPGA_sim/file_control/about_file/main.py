import about_file as syx
import os
from PIL import Image,ImageDraw
import matplotlib.pyplot as plt
import cv2
import numpy as np
import random

#直方图
def pctofpga(folder,outpath,image_name,txt_name):
    """
    Input:folder is the origin file
          outpath is the output file
          image_name is the image we prepare
          txt_name is out fpga file's name
    Return:True when output picture and txt has been generated
    """
    imagepath = folder+image_name
    outpath0 = outpath+'1.jpg'
    outpath1 = outpath+txt_name
    outpath2 = outpath+image_name
    image = cv2.imread(imagepath)
    gray_img = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    height,width = np.shape(gray_img)
    plt.hist(np.ravel(gray_img),256,[0,256])
    plt.savefig(outpath0)
    plt.show()
    syx.gray_fpga(outpath1,gray_img,width,height)
    t,thresh = cv2.threshold(gray_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)
    print(t)
    return t
#直方图
def fpgatopc(folder,outpath,result_name,output_name):
    txtpath = folder+result_name
    outpath0= outpath+output_name
    y = syx.txt2array(txtpath,256)
    x = [i for i in range(256)]
    plt.bar(x=x,height=y[0],align='edge',color='wheat',width=1)
    plt.savefig(outpath0)
    plt.show()
#生成二值化的FPGA模拟txt
def pcbintofpga(folder,outpath,image_name,txt_name):
    imagepath = folder+image_name
    outpath_0 = outpath+txt_name
    image = cv2.imread(imagepath)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    height,width = np.shape(image)
    syx.binary(outpath_0,image,width,height)

#Nrgb
def nrgb_generate(folder,outpath,image_name):
    picturepath = folder + image_name
    r = outpath + 'r.txt'
    g = outpath + 'g.txt'
    b = outpath + 'b.txt'
    nrgb = outpath + 'nrgb.txt'
    f = open(nrgb,'w')
    image = cv2.imread(picturepath)
    blue,green,red = cv2.split(image)
    height,width,unit = np.shape(image)
    syx.gray_fpga(r,red,height,width)
    syx.gray_fpga(g,green,height,width)
    syx.gray_fpga(b,blue,height,width)
    for i in range(height):
        for j in range(width):
            nr,ng,nb = 0,0,0
            (nr,ng,nb) = syx.nrgb(image[i][j][2],image[i][j][1],image[i][j][0])
            f.write('the nr = %d,the ng = %d,the nb = %d\n'%(nr,ng,nb))
    return None











    
def main():
    """
    Return: the gray picture data txt for fpga to simulation
    Return: the result of gray hist of pc
    """
    image_name = 'mvnr.png' #可以更改
    txt_name   = '1.txt' #可以更改
    folder = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/input_pic/'
    outpath = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/output_data/'
    t = pctofpga(folder,outpath,image_name,txt_name)

def main_0():
    """
    Using fpga simulation data to generate the gray hist
    """
    folder = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/output_result/'
    outpath = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/output_result/'
    result_name = 'result.txt'
    output_name = 'result.jpg'
    fpgatopc(folder,outpath,result_name,output_name)

def main_1():
    """
    Using the fpga labeled result to generate a labeled picture
    """
    outpath = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/pic.jpg'
    inputpath = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/input_pic/result.txt'
    labelpath = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/input_pic/label.txt'
    pic = syx.txt2matrix(inputpath,512,512)
    label = syx.txt2array(labelpath,7)
    syx.draw_pic(label,{},pic,outpath)

def main_2():
    """
    Input a binary picture then generate a txt for fpga to simulate
    """
    image_name = '9.bmp' #可以更改
    txt_name   = 'rgb1.txt' #可以更改
    folder = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/input_pic/'
    outpath = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/output_data/'
    t = pcbintofpga(folder,outpath,image_name,txt_name)

def main_3():
    """
    a normal rgb picture convert to nrgb
    """
    folder = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/pc_nrgb/pic/'
    outpath = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/pc_nrgb/result/'
    nrgb_generate(folder,outpath,'test.jpg')

    

if __name__ == '__main__':
    main_3()




