from videos import get_videos
from fetch_comments import get_comments
from config import Config


if __name__ == "__main__":
    # Get the aid and the number of comments associated with each video on homepage
    for item in Config.HOMEPAGES:
        video_list = get_videos(home_page=item[1], video_num=item[2])
        print(item[0], len(video_list))
        count = dict()
        crawled_num = 1
        for video in video_list:
            if crawled_num <= 39:
              crawled_num += 1
              continue
            
            # Fetch all comments using aid
            coms = get_comments(oid=video[0], com_num=video[1])

            # Count the number of emojis and store them in a dict
            all_coms = "".join(comment for comment in coms)

            for name, emoji in Config.EmojiCharac.items():
                if name in count:
                    count[name] += all_coms.count(emoji)
                else:
                    count[name] = all_coms.count(emoji)
            
            # for key in count:
            #     print("-"*40)
            #     print(key, ": ", count[key])
            print(crawled_num)
            crawled_num += 1
            for key in count:
                print(key, ": ", count[key])
        
        print("-"*20 + item[0] + "-"*20)
        for key in count:
            print(key, ": ", count[key])
