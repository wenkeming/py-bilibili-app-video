# JiJiDown 下载后重命名
import json, requests, os, shutil

fold = input('请输入文件夹关键字：')

def find_folder():
    folders = os.listdir('./')
    for folder in folders:
        if folder.find(fold) > -1:
            curr_folder = folder
            break
    run(curr_folder)
def run(folder):
    print(folder)
    files = os.listdir(folder)
    av = ''
    for f in files:
        if f.find('mp4') > -1:
            filename1 = f.split('(Av')
            filename2 = f.split('.')
            page = 'P'+ filename2[0]
            ex = filename2[-1]
            filename3 = filename1[0].split('.')
            filename4 = filename1[0].replace(filename3[0] + '.', '', 1)
            if av == '':
                av = filename1[1].split(',')[0]
            filename = page + ' ' + filename4 + '.' + ex
            print('重命名：'+ f +' --> '+ filename)
            os.rename(folder + '/' + f, folder + '/' + filename)
    print('重命名：'+ folder)
    os.rename(folder, av + ' ' + folder)

def init():
    find_folder()

init()