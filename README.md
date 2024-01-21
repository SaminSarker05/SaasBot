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

1. User enters message in form field which is collected by an event listener
2. A JS scripts makes a POST request to the page's view function
3. The message is passed to the openai client which generates a response
4. Both the message and response are stored as a Chat object which is displayed on the UI


## Example Pages

<img src="https://github.com/SaminSarker05/SaasBot/blob/main/images/home.png" width=80%>
<img src="https://github.com/SaminSarker05/SaasBot/blob/main/images/login.png" width=80%>
<img src="https://github.com/SaminSarker05/SaasBot/blob/main/images/register.png" width=80%>
<img src="https://github.com/SaminSarker05/SaasBot/blob/main/images/example.png" width=80%>


## Getting Started

1. Clone the repository:
   ```bash
   git clone git@github.com:SaminSarker05/EtherBlock.git
   ```
2. Change into Project Directory:
   ```bash
   cd EtherBlock
   ```
3. Install Project Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask Application:
   ```bash
   python3 app.py
   ```


## Future

- Use AWS cognito for user-authentication
- Organize chats into sessions that can be re-visited


