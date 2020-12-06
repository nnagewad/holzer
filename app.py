import tweepy
import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.API_KEY, twitter_credentials.API_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

locations = api.trends_available()
country_list = []
city_list = []

for location in locations:
    city_name = location['name']
    country_name = location['country']
    city_list.append(city_name)
    country_list.append(country_name)

country_list = list(dict.fromkeys(country_list))
city_list = set(city_list) - set(country_list)
city_list = list(city_list)

country_list.remove('')
city_list.remove('Worldwide')

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',cityList=city_list,countryList=country_list)

if __name__ == "__main__":
    app.run(debug=True)