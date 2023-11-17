#!/usr/bin/python

import os
import random
import sys
import time
from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class YouTubeUploader:
    def __init__(self, file, title, description, category, keywords, privacyStatus):
        self.file = file
        self.title = title
        self.description = description
        self.category = category
        self.keywords = keywords
        self.privacyStatus = privacyStatus
        self.YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
        self.YOUTUBE_API_SERVICE_NAME = "youtube"
        self.YOUTUBE_API_VERSION = "v3"

    def get_authenticated_service(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secrets.json", self.YOUTUBE_UPLOAD_SCOPE)
        credentials = flow.run_local_server(port=0)
        return build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION, credentials=credentials)

    def initialize_upload(self):
        youtube = self.get_authenticated_service()
        tags = None
        if self.keywords:
            tags = self.keywords.split(",")

        body = dict(
            snippet=dict(
                title=self.title,
                description=self.description,
                tags=tags,
                categoryId=self.category
            ),
            status=dict(
                privacyStatus=self.privacyStatus
            )
        )

        insert_request = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=MediaFileUpload(self.file, chunksize=-1, resumable=True)
        )

        self.resumable_upload(insert_request)

    def resumable_upload(self, insert_request):
        response = None
        error = None
        retry = 0
        while response is None:
            try:
                print("Uploading file...")
                status, response = insert_request.next_chunk()
                if response is not None:
                    if 'id' in response:
                        print("Video id '%s' was successfully uploaded." %
                              response['id'])
                    else:
                        exit("The upload failed with an unexpected response: %s" % response)
            except HttpError as e:
                if e.resp.status in [500, 502, 503, 504]:
                    error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
                else:
                    raise
            except [httplib2.HttpLib2Error, IOError] as e:
                error = "A retriable error occurred: %s" % e

            if error is not None:
                print(error)
                retry += 1
                if retry > 10:
                    exit("No longer attempting to retry.")

                max_sleep = 2 ** retry
                sleep_seconds = random.random() * max_sleep
                print("Sleeping %f seconds and then retrying..." % sleep_seconds)
                time.sleep(sleep_seconds)


# if __name__ == '__main__':
#     file = input("Enter the file path of the video: ")
#     title = input("Enter the title of the video: ")
#     description = input("Enter the description of the video: ")
#     category = input("Enter the category of the video: ")
#     keywords = input("Enter the keywords for the video (comma-separated): ")
#     privacyStatus = input("Enter the privacy status of the video (public, private, unlisted): ")

#     uploader = YouTubeUploader(file, title, description, category, keywords, privacyStatus)
#     uploader.initialize_upload()