import os, natsort, moviepy.editor as mpy
av = input('请输入番号关键字：')
no = input('请输入合并的文件关键字：')
folders = os.listdir('./')
for folder in folders:
    if folder.find(str(av)) >= 0:
        current_folder = folder
        break

files = os.listdir('./'+ current_folder)
join_files = []
filename = ''
for f in files:
    if f.find(str(no)) >= 0:
        join_files.append(f)
        if filename == '':
            filename = f.split(' - ')[0]

join_files = natsort.natsorted(join_files)
clips = []
for video in join_files:
    print(video)
    clips.append(mpy.VideoFileClip('./'+ current_folder +'/'+ video))
finalclip = mpy.concatenate_videoclips(clips)
finalclip.write_videofile('./'+ current_folder +'/'+ filename +'.mp4')