import credentials
import tweepy

# Autenticación e ingreso
auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


# Probando la conexión
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
    # print(f'{tweet.user.screen_name}:\ntweet.text\n{"*"*60}')


# Obtener los tweets de un topic
id = None
count = 0
while count <= 3000:
    tweets = api.search(q='one piece', lang='es', tweet_mode='extended', max_id=id)
    for tweet in tweets:
        if tweet.full_text.startswith('RT'):
            count += 1
            continue
        f = open('./onepiece.txt', 'a', encoding='utf-8')
        f.write(tweet.full_text + '\n')
        f.close
        count += 1
    id = tweet.id
    print(count)