from random import random, choice
import markovify
from datetime import datetime
import re

real_tweets = []
tweet_text = []

rts = []
favs = []
times = []

# parse
tweets = []
fin = [(re.sub(r'[a-z]*[:.]+\S+', '', i.split(",")[1]), i.split(",")[3], i.split(",")[4], i.split(",")[2]) for i in open("data/data.csv", "r", encoding="utf8").read().split("\n")]

for i in fin:
    tweet_text.append(i[0])
    rts.append(i[1])
    favs.append(i[2])
    times.append(i[3])
    real_tweets.append(i)

joined = "\n".join(tweet_text)
markov = markovify.NewlineText(joined)

def make_tweet():
    tweet = {
        "text": None,
        "retweets": None,
        "favorites": None,
        "is_real": None,
        "date": None
    }
    if(random() > 0.7):

        real = choice(real_tweets)
        tweet["text"] = real[0].replace("&amp", "&")
        tweet["retweets"] = real[1]
        tweet["favorites"] = real[2]
        tweet["is_real"] = True
        date = real[3]
        tweet["date"] = datetime.strftime(datetime.strptime(date, '%m-%d-%Y %H:%M:%S'),'%#I:%M %p - %d %b %Y')
    else:
        generated = markov.make_short_sentence(int(50 + random()*150))
        tweet["text"] = generated.replace("&amp;", "&")
        tweet["retweets"] = choice(rts)
        tweet["favorites"] = choice(rts)
        tweet["is_real"] = False
        date = choice(times)
        tweet["date"] = datetime.strftime(datetime.strptime(date, '%m-%d-%Y %H:%M:%S'), '%#I:%M %p - %d %b %Y')

    return tweet
# parse = re.sub(r'[a-z]*[:.]+\S+', '', i.split(",")[1], flags=re.MULTILINE)
# parse = parse.lower()
# parse = parse.replace(".", " . ")
# parse = parse.replace(",", " , ")
# parse = parse.replace("!", " ! ")
# parse = parse.replace("-", " - ")
# parse = parse.replace("?", " ? ")
# parse = ' '.join(parse.split())
# words = parse.split(" ")
# for j in range(len(words)):
#     all_words.add(words[j])
#     if words[j] not in word_dict:
#         word_dict[words[j]] = []
#     if j == len(words) - 1:
#         word_dict[words[j]].append(None)
#     else:
#         word_dict[words[j]].append(words[j+1])
# tweets.append(i.split(",")[1])

# all_words = list(all_words)
#
# fake_tweet = ""
# cur = choice(all_words)
# fake_tweet += cur
#
# while(True):
#     cur = choice(word_dict[cur])
#     if cur is None:
#         break
#     fake_tweet += " " + cur


# print(fake_tweet)