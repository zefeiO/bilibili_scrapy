import requests
import math

def get_comments(oid, com_num):
    api_model = "https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&next={}&type=1&oid={}&mode=3&plat=1"
    req_num = math.ceil(com_num/20)

    messages = list()
    for next in range(req_num):
        comment_api = api_model.format(next, oid)
        res = requests.get(comment_api)
        data = res.json()
        replies = data.get("data").get("replies")
        for reply in replies:
            messages.append(reply.get("content").get("message"))
            for rep_of_rep in reply.get("replies"):
                messages.append(rep_of_rep.get("content").get("message"))

    return messages