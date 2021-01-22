from pytube import YouTube



VideoUrl = '           https://www.facebook.com/olhardigital/videos/2847883375500570/             '.strip()


output_path = 'C:\\Users\\IgorDC\\Desktop\\YouTubeVideoSaveLocation\\'


def DownloadYoutubeVideo(VideoUrl, output_path):

    YouTube(VideoUrl).streams.get_highest_resolution().download(output_path=output_path)

    print('Done')

DownloadYoutubeVideo(VideoUrl, output_path)