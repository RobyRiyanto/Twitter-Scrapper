import tweepy
import pandas as pd

class Twitter:
    def __init__(self):
        pass

    def jokowiMarufSearch(self, consumer_key, consumer_secret, access_token, access_token_secret, jokowiMarufSearch_raw):
        # buat variabel untuk autentikasi dan akses token
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # Cari twit dengan kata kunci dan memfilter retweets
        search_words = "Jokowi Maruf"
        date_since = "2020-10-23"
        # date_until = "2020-10-23"
        new_search = search_words + " -filter:retweets"

        # tweets = tweepy.Cursor(api.search, q=new_search, lang="id", since=date_since, until=date_until, tweet_mode = 'extended').items(3000) # menggunakan until
        tweets = tweepy.Cursor(api.search, q=new_search, lang="id", since=date_since, tweet_mode = 'extended').items(3000)

        # convert to dataframe
        hasil = [[tweet.created_at, tweet.user.name, tweet.user.location, tweet.full_text, tweet.retweet_count, tweet.favorite_count] for tweet in tweets]
        df = pd.DataFrame(hasil, columns = ['created_at', 'screen_name', 'location', 'tweet', 'retweet_count', 'favorite_count'])
        print(df)

        # save to csv
        df.to_csv(jokowiMarufSearch_raw, index = False)
        print('data sudah tersimpan')

consumer_key = [YOUR KEY]
consumer_secret = [YOUR KEY]
access_token = [YOUR KEY]
access_token_secret = [YOUR KEY]

jokowiMarufSearch_raw = 'jokowiMaruf20201023_raw.csv' # cukup rubah tanggalnya, i.e 20201019 jika ambil tanggal 19 Okt 2020

app = Twitter()
app.jokowiMarufSearch(consumer_key, consumer_secret, access_token, access_token_secret, jokowiMarufSearch_raw)

