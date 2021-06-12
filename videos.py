import requests
import re
import math

def get_videos(home_page: str, video_num: int):
    # home_page: "https://space.bilibili.com/<mid:int>/video"
    mid = re.search(r"space.bilibili.com/(\d+)/video", home_page).group(1)

    page_num = math.ceil(video_num/30)
    api_model = "https://api.bilibili.com/x/space/arc/search?mid={}&ps=30&tid=0&pn={}&keyword=&order=pubdate&jsonp=jsonp"

    result = list()
    for pn in range(1, page_num+1):
        video_api = api_model.format(mid, pn)
        res = requests.get(video_api)
        data = res.json()
        vlist = data.get("data").get("list").get("vlist")
        for video in vlist:
            aid = video.get("aid")
            com_num = video.get("comment")
            result.append((aid, com_num))
    
    return result
