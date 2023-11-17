from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, link):
        self.link = link

    def download(self):
        youtubeObject = YouTube(self.link)
        youtubeStream = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeStream.download()
        except:
            print("An error has occurred")
        else:
            print("Download is completed successfully")

    def get_video_title(self):
        try:
            youtube_object = YouTube(self.link)
            title = youtube_object.title
            return title
        except Exception as e:
            print(f"An error occurred: {e}")
            return None



# if __name__ == '__main__':
#     link = input("Enter the YouTube video URL: ")
#     downloader = YouTubeDownloader(link)
#     downloader.download()
