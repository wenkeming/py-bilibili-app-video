import json, requests, os, shutil

def replace_spcial_word(word):
    special_words = ['?', '*', '"', '<', '>', '|']
    transfer_words = ['？', '', '', '《', '》', '']
    res = word
    for i in range(0, len(special_words)):
        res = res.replace(special_words[i], transfer_words[i])
    return res

def readpage(av):
    headers = {
        'Cookie': '_uuid=B57B2293-E01D-C0F1-D97E-928B5BC2260950356infoc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Host': 'www.bilibili.com'
    }
    html = requests.get('https://www.bilibili.com/video/av'+ av, headers=headers).text
    txt = html.split('window.__INITIAL_STATE__=')[1]
    txt = txt.split(';(function(){')[0]
    infos = json.loads(txt)['videoData']
    title = replace_spcial_word(infos['title'])
    pages = infos['pages']
    items = []
    index = 1
    for page in pages:
        items.append('P'+ str(index) +' '+ replace_spcial_word(page['part']))
        index += 1
    
    return [title, items]

def runner():
    av = input('请输入番号：')
    hd = input('请输入清晰度：')
    bit = input('请输入视频质量：')

    infos = readpage(str(av))

    folder = './'+ av + '/'
    index = 1

    for txt in infos[1]:
        path = folder + str(index) +'/lua.flv'+ hd +'.bili2api.'+ bit +'/'
        files = os.listdir(path)
        isOneFile = len(files) <= 3
        file_index = 1
        for f in files:
            if os.path.splitext(f)[-1] == '.blv':
                if isOneFile:
                    print('重命名：'+ txt)
                    os.rename(path + f, path + txt +'.mp4')
                    print('移动文件：'+ txt)
                    shutil.move(path + txt +'.mp4', folder + txt +'.mp4')
                    pass
                else:
                    print('重命名：'+ txt + str(file_index))
                    os.rename(path + f, path + txt +' - '+ str(file_index) +'.mp4')
                    print('移动文件：'+ txt + str(file_index))
                    shutil.move(path + txt +' - '+ str(file_index) +'.mp4', folder + txt +' - '+ str(file_index) +'.mp4')
                    file_index += 1
                    pass
                pass
        index += 1
    
    folders = os.listdir(folder)
    for folder_item in folders:
        if os.path.isdir(folder + folder_item):
            print('删除文件夹：'+ folder + folder_item)
            shutil.rmtree(folder + folder_item)

    print('重命名：'+ av + ' '+ infos[0])
    os.rename(folder, './'+ av +' '+ infos[0])

runner()