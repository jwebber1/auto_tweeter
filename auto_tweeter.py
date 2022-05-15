import tweepy
import datetime
import config
import quotes

client = tweepy.Client(
  consumer_key = config.API_KEY,
  consumer_secret = config.API_SECRET_KEY,
  access_token = config.ACCESS_TOKEN,
  access_token_secret = config.ACCESS_TOKEN_SECRET,
)

start_day = datetime.date(2022, 5, 13)
today = datetime.date.today()
delta_days = today - start_day

todays_dict = quotes.QUOTES[delta_days.days%len(quotes.QUOTES)]
todays_text = f'Good morning!\n\n{todays_dict["text"]}\n'

if todays_dict["author"] != None or todays_dict["author"] != "":
  todays_text += f'- {todays_dict["author"]}\n'
todays_text += f'\nSpecial thanks to SergeyWebPro for compiling the quotes\nhttps://forum.freecodecamp.org/t/free-api-inspirational-quotes-json-with-code-examples/311373'

response = client.create_tweet(text=todays_text)
