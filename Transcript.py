# from YouTubeLinks import GetCompletedLives, get_channel_videos
from YouHeadlines import GetTitle
from Caption import GetCaption
from AudioToText import AudToText


def GetTranscript(video_url):
    if GetTitle(video_url): #Goevrnment News Classifier has to be addded here
        cap = GetCaption(video_url)
        if cap:
            return 1,cap
        else:
            return 2, AudToText(video_url)
        
# print(GetTranscript("https://www.youtube.com/watch?v=88SX_Ihx_d0"))
# print(GetTranscript("https://www.youtube.com/watch?v=Cx87U7TJH3c"))
