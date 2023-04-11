# About

This is an API for instant dictionary where another application can get a definition for a pre defined word

## Working

It is a API built using justpy library and contains 2 endpoints
1. "/"
2. "/api"


### endpoint "/"
Serves the API documentation with URL and other endpoints with example

### endpoint "/api" 
Returns a JSON having the requested word and its definition.
The API call should me made as -> http://<hostname>/api?w=<Word>

## Credits
Based on the learnings from https://www.udemy.com/course/the-python-pro-course/

# Learnings
- Building API using JustPy library
- Writing API documentation
- Using the API with another application