
import pandas
from googleapiclient.discovery import build


comments = list()
api_obj = build('youtube', 'v3', developerKey='AIzaSyCHdfk0AxR8mVIwOe59-DyC6zUUeyn58_I')
response = api_obj.commentThreads().list(part='snippet,replies', videoId='NecSut7TDsM', maxResults=100).execute()
next_page_token = None
while True:
    response = api_obj.commentThreads().list(part='snippet,replies', videoId='NecSut7TDsM', maxResults=100, pageToken=next_page_token).execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([
            comment['textDisplay'],
            comment['authorDisplayName'],
            comment['publishedAt'],
            comment['likeCount']
        ])

        if 'replies' in item and item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                reply = reply_item['snippet']
                comments.append([
                    reply['textDisplay'],
                    reply['authorDisplayName'],
                    reply['publishedAt'],
                    reply['likeCount']
                ])

    if 'nextPageToken' in response:
        next_page_token = response['nextPageToken']
    else:
        break

df = pandas.DataFrame(comments)

df.to_csv('미국 AI가 만들면 별도 표시 자발 참여 2023.07.22뉴스투데이MBC.csv', header=['comment', 'author', 'date', 'num_likes'], index=1000)




