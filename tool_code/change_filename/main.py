import os

path = 'C:/Users/Administrator/Desktop/孙言昕/增强图/'
i = 0
for file in os.listdir(path):
    new_name = str(i) + '.bmp'
    os.rename(path + file,path + new_name)
    i+=1

