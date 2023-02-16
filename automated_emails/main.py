import yagmail
import pandas as pd
from news import NewsFeed
from datetime import datetime, timedelta
import time


def send_email():
    today = datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'], from_date=yesterday, to_date=today)
    email = yagmail.SMTP(user="csit6910@gmail.com", password="akprfwuujtzcgqju")
    email.send(
        to=row['email'],
        subject=f"Your {row['interest']} news for today!",
        contents=f"Hi {row['name']}\nSee whats on about {row['interest']} today \n {news_feed.get()}.",
    )


while True:
    if datetime.now().hour == 13 and datetime.now().minute == 00:
        df = pd.read_excel('files/people.xlsx')

        for index, row in df.iterrows():
            send_email()

        time.sleep(60)