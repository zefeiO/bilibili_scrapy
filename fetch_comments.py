import requests
import math
import time

def get_comments(oid, com_num):
    api_model = "https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&next={}&type=1&oid={}&mode=3&plat=1"
    req_num = math.ceil(com_num/20)

    messages = list()
    for next in range(req_num):
        comment_api = api_model.format(next, oid)
        res = None
        # repeat the request when it has been blocked
        while True:
            try:
                res = requests.get(comment_api)
            except:
                time.sleep(60)
                continue

            if res.status_code != 200:
                time.sleep(60)
                continue
            else:
                break
        
        data = res.json()
        replies = data.get("data").get("replies")
        if replies == None:
            return messages
        for reply in replies:
            messages.append(reply.get("content").get("message"))
            if reply.get("replies") != None:
                for rep_of_rep in reply.get("replies"):
                    messages.append(rep_of_rep.get("content").get("message"))
        time.sleep(0.1)

    return messages