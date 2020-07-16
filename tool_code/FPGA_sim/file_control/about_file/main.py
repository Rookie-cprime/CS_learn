import about_file as syx
import os
from PIL import Image,ImageDraw
import matplotlib.pyplot as plt
import cv2
import numpy as np


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
    cv2.imshow('thresh',thresh)
    return t






    
def main():
    image_name = '9.bmp' #可以更改
    txt_name   = '1.txt' #可以更改
    folder = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/input_pic/'
    outpath = 'B:/Github/CS_learn/tool_code/FPGA_sim/file_control/output_data/'
    t = pctofpga(folder,outpath,image_name,txt_name)
    

if __name__ == '__main__':
    main()




