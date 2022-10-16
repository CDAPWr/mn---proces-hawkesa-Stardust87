
import pandas as pd
from tqdm import tqdm


records = []
with open("weibo/dataset.txt", "r") as f:
    
    for line in tqdm(f):
    
        line = line.strip()
        split = line.split("\t")
        message_id, root_user_id, publish_time, retweet_number, retweets = split
        if root_user_id == "-1":
            continue
        retweets = retweets.split(" ")[1:]
        assert all([retweet.split("/")[0] == root_user_id for retweet in retweets]), f"not a retweet to base tweet {message_id=}"
        retweets = ",".join([retweet.split(":")[-1] for retweet in retweets])
        record = {"message_id": message_id, "root_user_id": root_user_id, "publish_time": publish_time, "retweet_number": retweet_number, "retweets": retweets}
        records.append(record)

df = pd.DataFrame(records)
df.to_csv("weibo/weibo_dataset.csv", index=False)