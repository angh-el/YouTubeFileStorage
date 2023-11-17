from cryptography.fernet import Fernet
from Encrypt import Encrypt
from Decrypt import Decrypt
from VideoConverter import VideoConverter
from YouTubeUploader import YouTubeUploader
from YouTubeDownloader import YouTubeDownloader
from VideoReverter import VideoReverter

class Main:

    def run(self):
        action = input("Do you want to upload a file (U), retrieve a file (R) or exit (X)?  ").upper()

        if action == 'U':
            path = input("Enter the path to the .txt file: ")
            encryptor = Encrypt(path)
            encrypted_contents = encryptor.get_file_contents()

            #video conversion
            input_string = encrypted_contents
            output_file = "sample_video.mp4"
            converter = VideoConverter(input_string, output_file)
            converter.create_colored_frames()

            #uplad to youtube
            file_name = "sample_video.mp4"
            title = input("Enter the title of the video: ")
            description = input("Enter the description of the video: ")
            category = input("Enter the category of the video: ")
            keywords = input("Enter the keywords for the video (comma-separated): ")
            privacyStatus = input("Enter the privacy status of the video (public, private, unlisted): ")

            uploader = YouTubeUploader(file_name, title, description, category, keywords, privacyStatus)
            uploader.initialize_upload()
                

        elif action == 'R':
            link = input("Enter the link of the video to retrieve: ")
            downloader = YouTubeDownloader(link)
            downloader.download()
            
            title = downloader.get_video_title()+".mp4"
            video_reverter = VideoReverter(title)
            video_reverter.detect_colors_in_video()


            

        elif action == 'X':
            return

        else:
            print("Invalid choice. Please select 'U' to upload or 'R' to retrieve a file.")
            self.run()

    





if __name__ == '__main__':
    # file_path = 'Test.txt'
    # file_path = 'Hello.txt'
    main = Main()
    main.run()

