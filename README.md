# SaasBot Assistant

<samp>Intelligent chatbot system replicating chatgpt to provide expert coding assistance. Application built using python Django, complete with user authentication, and deployed on EC2 instance. Fine tuned chat completiton API with system defined role.</samp>

## Features

- `OpenAI API` : Generated responses like ChatGPT large language model
- `Chatbot` : Chat model storing user messages on SQLite3 database
- `User-authentication` : User login and registration authentication with Django
- `AWS-EC2` : Website deployed live on AWS EC2 cloud services


## Tech Stack

- `Python Django` : High level Python web-framework for backend
- `sqlite3` : Lightweight, serverless database engine for user and post models
- `HTML, CSS` : Structuring content for responsive and user-friendly design
- `AWS EC2` : Cloud computing service for hosting application


## Explanation

1. <samp>User enters message in form field which is collected by an event listener</samp>
2. <samp>A JS scripts makes a POST request to the page's view function</samp>
3. <samp>The message is passed to the openai client which generates a response</samp>
4. <samp>Both the message and response are stored as a Chat object which is displayed on the UI</samp>


## Example Pages

<img src="https://github.com/SaminSarker05/SaasBot/blob/main/images/home.png" width=80%>
<img src="https://github.com/SaminSarker05/SaasBot/blob/main/images/login.png" width=80%>
<img src="https://github.com/SaminSarker05/SaasBot/blob/main/images/register.png" width=80%>
<img src="https://github.com/SaminSarker05/SaasBot/blob/main/images/example.png" width=80%>


## Getting Started

1. Clone the repository:
   ```bash
   git clone git@github.com:SaminSarker05/SaasBot.git
   ```
2. Change into Project Directory:
   ```bash
   cd SaasBot
   ```
3. Install Project Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Make .env file with OPENAI KEY called OPENAI:
   ```bash
   OPENAI = EXAMPLE
   ```
5. Change into Application Directory:
   ```bash
   cd bot
   ```
6. Start the Django Application:
   ```bash
   python3 manage.py runserver
   ```


## Future

- Use AWS cognito for user-authentication
- Organize chats into sessions that can be re-visited


