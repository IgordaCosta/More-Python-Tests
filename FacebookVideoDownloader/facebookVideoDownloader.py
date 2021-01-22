from datetime import datetime
from tqdm import tqdm
import requests
import re
import os

import getFacebookVideoposter

def main(url,saveLocaction,list,HD,IfNotDowloadOtherQuality,html):
    try:
        if len(list) == 2:
            if 0 in list and 1 in list:
            #     _input_1 = str(input("\nPress 'A' to download the video in HD quality.\nPress 'B' to download the video in SD quality.\n: ")).upper()
                if HD:
                    download_video(url,"HD",saveLocaction,html)

                else:
                    download_video(url,"SD",saveLocaction,html)

        if len(list) == 2:
            if 1 in list and 2 in list:
            #     _input_2 = str(input("\nOops! The video is not available in HD quality. Would you like to download it? ('Y' or 'N'): ")).upper()
                if IfNotDowloadOtherQuality:
                    download_video(url,"SD",saveLocaction,html)
                else:
                    exit()

        if len(list) == 2:
            if 0 in list and 3 in list:
                #_input_2 = str(input("\nOops! The video is not available in SD quality. Would you like to download it? ('Y' or 'N'): \n")).upper()
                if IfNotDowloadOtherQuality:
                    download_video(url,"HD",saveLocaction,html)
                else:
                    exit()
    except(KeyboardInterrupt):
        print("\nProgramme Interrupted")


def download_video(url,quality,saveLocaction,html):
    """Download the video in HD or SD quality"""
    print(f"\nDownloading the video in {quality} quality... \n")
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    VideoPoster = getFacebookVideoposter.getFacebookVideoposter(url)
    filename = VideoPoster+"_"+datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    if saveLocaction == '':
        saveLocactionF= saveLocaction

    else:
        saveLocactionF= saveLocaction+'\\'

    with open(saveLocactionF + filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    print("\nVideo downloaded successfully.")

def facebookVideoDownloader(url,saveLocaction='',HD=True,IfNotDowloadOtherQuality=True):
    # try:
    #while True:
        #url = input("\nEnter the URL of Facebook video: ")

        url = url.strip()
        x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)
        
        html=''

        if x:
            html = requests.get(url).content.decode('utf-8')
        else:
            print("\nNot related with Facebook domain.")
            
        if html == '':
            pass
        else:

            _qualityhd = re.search('hd_src:"https', html)
            _qualitysd = re.search('sd_src:"https', html)
            _hd = re.search('hd_src:null', html)
            _sd = re.search('sd_src:null', html)

            list = []
            _thelist = [_qualityhd, _qualitysd, _hd, _sd]
            for id,val in enumerate(_thelist):
                if val != None:
                    list.append(id)

            main(url,saveLocaction,list,HD,IfNotDowloadOtherQuality,html)
        # again = input("\nWanna download another video? (Y or N): ").upper()
        # if again == str("Y"):
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     continue
        # else:
        #     break

    # except KeyboardInterrupt:
    #     print("\nProgramme Interrupted")


url='        https://www.facebook.com/olhardigital/videos/2847883375500570/       '

saveLocaction=r'C:\Users\IgorDC\Desktop\FacebookVideoSaveLocation'


facebookVideoDownloader(url,saveLocaction)
