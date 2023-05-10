import pandas as pd


def twitter_filter(df, search):
    coun = 0
    date_ls = []
    id_ls = []
    content_ls = []
    lan_ls = []
    name_ls = []
    retweet_ls = []
    cleaned_tweet_ls = []

    for i, row in df.iterrows():
        if search in row.cleaned_tweet:
            date_ls.append(row['date'])
            id_ls.append(row['id'])
            content_ls.append(row['content'])
            lan_ls.append(row['language'])
            name_ls.append(row['name'])
            retweet_ls.append(row['retweet'])
            cleaned_tweet_ls.append(row['cleaned_tweet'])

    new_dict = {
        "date": date_ls,
        "id": id_ls,
        "content": content_ls,
        "lan": lan_ls,
        "user_name": name_ls,
        "retweet": retweet_ls,
        "cleaned_tweeet": cleaned_tweet_ls,

    }
    new_df = pd.DataFrame(new_dict)
    return new_df


if __name__ == '__main__':
    df = pd.DataFrame(
        {
            "date": ["2019-01-01", "2019-01-02", "2019-01-03", "2019-01-04", "2019-01-05"],
            "id": [1, 2, 3, 4, 5],
            "content": ["a", "b", "c", "d", "e"],
            "language": ["en", "en", "en", "en", "en"],
            "name": ["Rabbitdogebsc", "gmtowner", "topcryptostats", "vGhostvRiderv", "gmtowner"],
            "retweet": [1, 2, 3, 4, 5],
            "cleaned_tweet": ["a", "b", "c", "d", "e"],
        }
    )
    res = twitter_filter(df, "")
    print(res)
