import requests
from urllib import request
import os,shutil,time,random

number=1
url=f'https://blackpearl.tortuga.wtf/content/stream/serials/charmed.s01e01.1plus1.mvo_4335/hls/480/segment{number}.ts'

stream=url.split('/')[6]
#print(stream)
def download_files(number=1):
    while number<2:#think what to do with state--- state or
        url = f'https://blackpearl.tortuga.wtf/content/stream/serials/charmed.s01e01.1plus1.mvo_4335/hls/480/segment{number}.ts'
        request.urlretrieve(url, f'{number}.ts')
        print(number)
        time.sleep(random.randrange(1, 3))
        number += 1
        #return number
def create_folder():
    if not os.path.isdir(f"{stream}"):
        os.mkdir(f"{stream}")# create folder with name...
    os.chdir(f'{stream}')#change directory
    #print(os.getcwd())
    download_files()# download in this directory
    create_bat()
    call_bat()
    move_from()
    delete()
def create_bat():
    with open(f'bat.bat', 'w') as f:
        f.write(f'copy /b *.ts {stream}.ts') #create bat file for unite ts files
def move_from():
    print(os.getcwd())
    #os.chdir(f'{stream}')
    if not os.path.exists(f'D:/pythonProject1/video\{stream}.ts'):
        shutil.move(f'{stream}.ts','D:/pythonProject1/video')
    else:
        os.remove(f'D:/pythonProject1/video\{stream}.ts')
        shutil.move(f'{stream}.ts', 'D:/pythonProject1/video')
def call_bat():
    # bat file for unite ts files
    os.system(f'start bat.bat')
def delete():
    os.system(f'del {stream}/*.ts')
    os.remove(f'bat.bat')
create_folder()