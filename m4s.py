# m4s重命名
import os

def runner():
    folders = os.listdir('./')
    for folder in folders:
        print('重命名'+ folder)
        if os.path.exists(folder + '/64/audio.m4s'):
            os.rename(folder + '/64/audio.m4s', folder + '/64/audio.m4a')
        if os.path.exists(folder + '/64/video.m4s'):
            os.rename(folder + '/64/video.m4s', folder + '/64/video.m4v')
runner()