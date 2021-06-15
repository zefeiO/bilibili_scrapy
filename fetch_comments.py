import requests
import math
import time
from config import Config

def next_proxy(i, proxies_json):
    i = (i + 1) % 30
    return i, {
        "http": "http://" + proxies_json[i].get("Ip") + ":" + str(proxies_json[i].get("Port")),
        "https": "https://" + proxies_json[i].get("Ip") + ":" + str(proxies_json[i].get("Port"))
    }

def get_comments(oid, com_num):
    api_model = "https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&next={}&type=1&oid={}&mode=3&plat=1"
    req_num = math.ceil(com_num/20)

    proxies_json = requests.get("http://gec.ip3366.net/api/?key=20210615180511308&getnum=30&anonymoustype=3&filter=1&area=1&formats=2&proxytype=01").json()
    i = -1
    messages = list()
    for next in range(req_num):
        comment_api = api_model.format(next, oid)
        proxies = next_proxy(i, proxies_json)

        # filter out the usable proxy servers
        t1 = time.time()
        while True:
            try:
                res = requests.get(comment_api, proxies=proxies)
            except:
                i, proxies = next_proxy(i, proxies_json)
                print("NO!!{}".format(i))
            else:
                break
        print("First while loop: " + str(time.time() - t1))
            
        # change the proxy when request has been blocked by bilibili
        t2 = time.time()
        while res.status_code != 200:
            i, proxies = next_proxy(i, proxies_json)
            try:
                res = requests.get(comment_api, proxies=proxies)
            except:
                print("NO!!{}".format(i))
                continue
        print("Second while loop: " + str(time.time() - t2))
            
        
        # # repeat the request when it has been blocked
        # while res.status_code != 200:
        #     time.sleep(60)
        #     res = requests.get(comment_api)
        
        t3 = time.time()
        data = res.json()
        replies = data.get("data").get("replies")
        if replies == None:
            return messages
        for reply in replies:
            messages.append(reply.get("content").get("message"))
            if reply.get("replies") != None:
                for rep_of_rep in reply.get("replies"):
                    messages.append(rep_of_rep.get("content").get("message"))
        # time.sleep(0.1)
        print("Third loop: " + str(time.time() - t3))

    return messages