from pytube import YouTube

import os
import glob

from moviepy.editor import *

# import pprint



AudioUrl = '            https://www.youtube.com/watch?v=rtOvBOTyX00              '.strip()


output_path = 'C:\\Users\\IgorDC\\Desktop\\YouTubeAudioSaveLocation\\'




def DownloadYoutubeAudio(AudioUrl,output_path):

    YouTube(AudioUrl).streams.filter(subtype ='mp4').get_highest_resolution().download(output_path=output_path)

   
    # pprint.pprint(list(YouTube(AudioUrl).streams))


    os.chdir(output_path)

    newest = max(glob.iglob('*'), key=os.path.getctime)

    print(newest)

    newestList=newest.split('.')

    OriExtension=newestList[-1]

    print(OriExtension)


    if OriExtension == 'mp3':

        print('file already mp3')



    else:

        extensionSpace=len(OriExtension)+1

        filenameNoextension = newest[:-extensionSpace]

        print(filenameNoextension)
            
        newestMp3=filenameNoextension+'.mp3'

        print(newestMp3)


        mp4_file = output_path + newest
        mp3_file = output_path + newestMp3

        
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()


        os.remove(mp4_file) 







DownloadYoutubeAudio(AudioUrl,output_path)