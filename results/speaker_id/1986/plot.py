import numpy as np
import matplotlib.pyplot as plt

def openreadtxt(file_name):
    data = []
    file = open(file_name,'r')  #打开文件
    file_data = file.readlines() #读取所有行
    for row in file_data:
        tmp_list = row.split(':') #按‘loss'切分每行的数据
        data.append(tmp_list) #将每行数据插入data中
    return data
  
  
if __name__=="__main__":
    data = openreadtxt('train_log.txt')
    train_loss=[]
    valid_loss=[]
    for idx,i in enumerate(data):
        if idx!=len(data):
            train=(((data[idx])[3]).split(' - '))[0]
            valid=(((data[idx])[-2]).split(','))[0]
            train=float(train)
            valid=float(valid)
            train_loss.append((train))
            valid_loss.append((valid))

    plt.figure()
    plt.plot(train_loss,marker='.', mec='r',label='train_loss')
    plt.plot(valid_loss,marker='*',label='valid_loss')
    plt.xlabel('epoch')
    plt.ylabel('value')
    plt.legend()
    plt.show()