from videos import get_videos
from fetch_comments import get_comments
from config import Config


if __name__ == "__main__":
    for item in Config.HOMEPAGES:
        # Get the aid and the number of comments associated with each video on homepage
        video_list = get_videos(home_page=item[1], video_num=item[2])

        for video in video_list:
            # Fetch all comments using aid
            coms = get_comments(oid=video[0], com_num=video[1])
            
            # Count the number of emojis and store them in a dict