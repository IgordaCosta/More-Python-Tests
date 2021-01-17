from pydub import AudioSegment


def SplitMp3(Mp3File,Mp3Location,NumFilesToSplit):

    sound = AudioSegment.from_mp3(Mp3Location+'\\'+Mp3File)

    extensionUsed='.' + Mp3File.split('.')[-1]

    extensionUsedSize = len(extensionUsed)
    
    Mp3FileNameOnly = Mp3File[:-extensionUsedSize]


    

    # print('sound full size: ',len(sound))

    DividingStep = int(len(sound) / NumFilesToSplit)

    # print('DividingStep: ',DividingStep)

    # soundList=[]

    for i in range(NumFilesToSplit):

        startLocation=DividingStep*i

        StopLocation=DividingStep*(i+1)

        print('i: ',i)

        if i==NumFilesToSplit-1:

            soundListStep = sound[startLocation:]
            # print('last just runned')

        else:

            soundListStep = sound[startLocation:StopLocation]

        # soundList.append(soundListStep)

        # print('soundListStep size: ',len(soundList[i]))

        soundListStep.export(Mp3Location+'\\'+Mp3FileNameOnly+"_Part_"+str(i+1)+extensionUsed, format="mp3")




    # print('soundList: ',soundList)

    print("Done")



Mp3File='Reuniao2Ap.mp3'


Mp3Location=r'C:\Users\IgorDC\Desktop\Mp4ToMp3Location'


NumFilesToSplit=2



SplitMp3(Mp3File,Mp3Location,NumFilesToSplit)
