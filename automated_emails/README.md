# About
This is a application that sends Newsfeed via Email to the userbase.

## Working
This application is a repetitive task that runs in infinite while loop.
1. The userbase of the application is stored in xlsx file which contains email addresses and interests of the user.
2. The program uses request library to get news from newsapi.org the collected news are based on the user's interest.
3. The collected news from the API are emailed to respective users with the help of SMTP service.
4. The program is written in such a way that it sends automated emails at 1PM everyday to the users.

## Credits
Based on the learnings from https://www.udemy.com/course/the-python-pro-course/

# Learnings
- Automated Emails
- SMTP library
- Webscrapping
- Requests library
- yagmail Library

