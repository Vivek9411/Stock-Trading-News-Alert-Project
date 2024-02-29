import requests
import datetime
from twilio.rest import Client
yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
day_before = str(datetime.date.today() - datetime.timedelta(days=2))
# print(yesterday)
# print(day_before)
print(yesterday)
print(day_before)
STOCK = "RELIANCE.BSE"
COMPANY_NAME = "RELIANCE"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
API_KEY = api_key
API = "https://www.alphavantage.co/query"
parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}
response = requests.get(url=API, params=parameter)
response.raise_for_status()

data = response.json()['Time Series (Daily)']
print(data)
yesterday_closing = float(data[yesterday]['4. close'])
before_yesterday_opening = float(data[day_before]["1. open"])

# better way of getting hold of yesterdata and day before yestedays data is

data1 = [value for (key, value) in data.items()]

yesterday_closing = float(data1[0]["4. close"])
before_yesterday_opening = float(data1[1]["4. close"])
print(yesterday_closing)
print((before_yesterday_opening))



# print(yesterday_closing)
# print(before_yesterday_opening) 
percent = (abs(yesterday_closing-before_yesterday_opening)/before_yesterday_opening)*100


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
Api_KEY2 = '7162308c8429437bacd0f9c4ea19b4b5'
url = "https://newsapi.org/v2/everything"
response1 = requests.get(url="https://newsapi.org/v2/everything?q=RELIANCE&apiKey=7162308c8429437bacd0f9c4ea19b4b5")
news_data = response1.json()['articles'][:3]
final_news = []
for item in news_data:
    temp ={
        "title": item["title"],
        "description": item['description']
    }
    final_news.append(temp)


# sending message with the help of twilio first create an account
# provide these details from twilio
to = ""  # number to which you want to send the notification
from_ = ''
account_sid = ''  #  you will get from twilio
auth_token = '' #  you will get from twilio


if percent >= 0:
    for news in final_news:
        a = news["title"]
        b = news["description"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_=from_,
            to=to,

            body=f"headline:{a} \n\n\n Brief:{b}"
        )






