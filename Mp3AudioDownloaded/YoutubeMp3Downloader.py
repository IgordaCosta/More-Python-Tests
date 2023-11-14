from pytube import YouTube

# Provide the URL of the YouTube video you want to download
video_url = 'https://www.youtube.com/watch?v=NFq2agaONzA'

# Specify the output directory and filename (change as needed)
output_directory = r'F:\Apps3\More-Python-Tests\Mp3AudioDownloaded'
output_filename = 'output.wav'

def download_mp3(video_url, output_directory, output_filename):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path=output_directory, filename=output_filename)

if __name__ == "__main__":
    download_mp3(video_url, output_directory, output_filename)