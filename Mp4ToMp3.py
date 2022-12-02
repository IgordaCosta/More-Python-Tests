from pytube import YouTube

import os
import glob

from moviepy.editor import *

# import pprint



Mp4File ='File2Convert.mp4'


pathUsed = r'C:\Users\Tigereye\Desktop\Mp4ToMp3Location'+ '\\'




def Mp4ToMp3(Mp4File, pathUsed):

    # YouTube(AudioUrl).streams.filter(subtype ='mp4').get_highest_resolution().download(output_path=output_path)

   
    # pprint.pprint(list(YouTube(AudioUrl).streams))


    os.chdir(pathUsed)

    # newest = max(glob.iglob('*'), key=os.path.getctime)

    # print(newest)

    newestList=Mp4File.split('.')

    OriExtension=newestList[-1]

    print(OriExtension)


    if OriExtension == 'mp3':

        print('file already mp3')



    else:

        extensionSpace=len(OriExtension)+1

        filenameNoextension = Mp4File[:-extensionSpace]

        print(filenameNoextension)
            
        newestMp3=filenameNoextension+'.mp3'

        print(newestMp3)


        mp4_file = pathUsed + Mp4File
        mp3_file = pathUsed + newestMp3

        
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()


        # os.remove(mp4_file) 

        print("Done")






Mp4ToMp3(Mp4File,pathUsed)