from toolz import pipe, compose
from toolz.functoolz import compose_left
import twitter
from multiprocessing import Pool

Twitter = twitter.Api(consumer_key="lgdsqRUZQd0uU0ka76Rthk7FZ",
                      consumer_secret="SfX5QgkveTJdUKrjIlteROk64CDqkkWul9XZckKZ1HvXYLySan",
                      access_token_key="1408828154928582661-2qs7Trc01Wd3lR4IaRfQrCJSI7dx4L",
                      access_token_secret="Iao92WvRqJQsZNhqVGjhco0goybl8rPbKO5b8KNv440eZ")
# Bearer Token: AAAAAAAAAAAAAAAAAAAAAEs9VAEAAAAAAbb0sk6Nd5r6ZEqfbmjBbtfFn5o%3DafyUeb7uHbsl5lsfdJnB1kRff16pdNYBRrS8ChiOlnlWNNbmXG

# Tweet level functions
def get_tweet_from_id(tweet_id, api=Twitter):
    return api.GetStatus(tweet_id, trim_user=True)

def tweet_to_text(tweet):
    return tweet.text

def tokenize_text(text):
    return text.split()

def score_text(tokens):
    lexicon = {"the":1, "to":1, "and":1,
             "in":1, "have":1, "it":1,
             "be":-1, "of":-1, "a":-1,
             "that":-1, "i":-1, "for":-1}
    return sum(map(lambda x: lexicon.get(x, 0), tokens))

def score_tweet(tweet_id):
    return pipe(tweet_id,
                get_tweet_from_id, tweet_to_text,
                tokenize_text, score_text)
    

users_tweets = [
[1056365937547534341, 1056310126255034368, 1055985345341251584,
 1056585873989394432, 1056585871623966720],
[1055986452612419584, 1056318330037002240, 1055957256162942977,
 1056585921154420736, 1056585896898805766]
]


# User level functions
def score_user(tweets):
    N = len(tweets)
    total = sum(map(score_tweet, tweets))
    return total/N

def categorize_user(user_score):
    if user_score > 0:
        return {"score":user_score,
                "gender": "Male"}
    return {"score":user_score,
            "gender":"Female"}

pipeline = compose_left(score_user, categorize_user)


if __name__ == '__main__':
    with Pool(processes=2) as P:
        print(P.map(pipeline, users_tweets))





