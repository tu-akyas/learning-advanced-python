# About
This is a webapp developed using FLASK to calculate the calorie intake needed for the user
based on their age, weight, height and temperature of the location.

## Working
This application has 2 Web Pages.
1. Home Page that have simple text and a link to bill page. This could be further improved by Styling with CSS and with more informations.
2. A form page which takes the input from the user of their age, weight, height, country and city.
3. On clicking the calculate button it will display the calculated result.

- When the user inputs necessary info, the temperature of the user location is obtained by webscraping.
- The website from where the data is scrapped is "https://www.timeanddate.com/weather"
- Formula used for calculting calorie is "BMR = 10 x weight + 6.5 x height - 5 x age - 10 x temperature"

## Credits
Based on the learnings from https://www.udemy.com/course/the-python-pro-course/


# Learnings
- Web development
- FLASK Framework
- Frontend with HTML and CSS
- Webscrapping
- Requests library
- selectorlib library
