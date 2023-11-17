# YouTubeFileStorage

## Introduction
YouTube platform offers users the ability to upload an unlimited amount of videos, hence an unlimited amount of media can be stored on the platform, theoretically. The aim of the project is to encode files into videos and upload them onto YouTube as a form of "cloud storage". The way this was achieved was by mapping characters onto specific colours, then conjoining the frames to create a video. For the purposes of reducing memory usage, each frame is made up of 10 coloured strips/ 10 characters, however, this can still be further reduced.

## Implementation
- Python: the core programming language used in this project
- Fernet (Cryptography Library): implemented to encrypt the files, esnuring security
- MoviePy: utilised for video editing and composition
- OpenCV: used for video processing and image detection, enhancing the project's ability to interact with the video files
- Google API: integrated to allow videos to be uploaded directly to YouTube
- PyTube: used for video downloading, allowing for the retireval of videos from YouTube

## Prerequesites
1. Ensure python is installed: ```python --version```
2. Clone this repository: ```git clone https://github.com/angh-el/YouTubeFileStorage```
3. Install the external libraries: ```pip install cryptography``` ```pip install opencv-python``` ```pip install pytube```
4. Setting up the Google API: [link to video tutorial](https://www.youtube.com/watch?v=eq-mjehACe4&ab_channel=SoftwareSage)


  ## Usage
1. Run the program:  ``` python Main.py  ```
     ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/344d5c23-b7eb-473c-bb12-803f59ea02d3)
2. Selecting 'U' for upload:

    Enter the name of the file
  ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/b42cfdb6-721c-4294-9d93-5811a5881392)

    Example file that is used in this example:
   ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/d6d00cb6-fb8b-4671-8d35-f5e378360eeb)

    Converting the file into a video
  ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/0a1b2087-c23c-4e98-ac56-3f884354ec9c)

    Video conversion finished and saved as sample_video.mp4
  ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/61b56d2f-0bb5-42c6-8e22-0bb73b344f62)

    Frame taken from sample_video.mp4
   ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/17e9e442-ef0a-4b9e-bb09-cefe135a0637)

    Enter the final details for uploading the video on YouTube and follow the on-screen instructions in the new opened tab
   ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/61338264-4c30-4d62-a91b-8c1a63a79e64)
    * for the category of the video please refer to: [YouTube Categories Explained](https://www.linkedin.com/pulse/ultimate-guide-youtube-categories-which-one-right-you-basavaraj-v-#:~:text=Music%20%2D%20This%20category%20features%20music,popular%20gamers%20and%20gaming%20enthusiasts.)
    * it is also recommened to set the privacy status as unlisted so that it can only be accessed if through its unique link

3. Selecting 'R' for reteiving the file:

    Enter the YouTube link
   ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/fafd084f-3bf8-4143-aa01-c0292efde292)

    A status message will be printed
   ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/7ba1dc1c-9c98-4eb4-a121-711a82a86e3c)

    Two new files will be created as result of this. One for the downloaded video and one of the decoded file
   ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/80d3f5ac-039d-4f27-9c78-c3aadc255eb3)
  ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/21b41e8d-1696-48a5-9654-431d374f11ee)

    The new decoded file
   ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/19644b0c-333b-4afd-aadb-f283e38ccae8)

    Before and after succesful conversion from text to video and back to text
   ![image](https://github.com/angh-el/YouTubeFileStorage/assets/123000792/0633578a-14a3-4116-b486-33f8cdbc5052)


## Reflections
- The main goal of the project was to convert contents of a file into a video, then decode it back into file format, which was succesfully achieved
- During the testing stage, it was concluded that this method of storing files is relatively inefficient due to Google API restrictions, time taken to encode and decode the file, and the size of the videos
- Further Improvements to the model could be to support different file formats other than .txt

    

