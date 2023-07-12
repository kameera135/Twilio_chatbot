![GitHub User's stars](https://img.shields.io/github/stars/RajKKapadia?style=for-the-badge)
![GitHub followers](https://img.shields.io/github/followers/RajKKapadia?style=for-the-badge)

# WhatsApp-OpenAI Connection
Hi everyone, this is a repository for my personal demo project on connecting Twilio and OpenAI to provide answers to all the user's questions using OpenAI GPT-3. This is written in `Python` and served with `Flask`. This bot can only handle:
* text messages


### What you will need
There are a couple of things that you need before you get started following this repository.
* OpenAI API key, since it is open to all, you can create an account [here](https://openai.com/) and access the key.
* You need a Twilio project, you can get `Account SID` and `Auth Token` for that project, we will need this to make requests. You can get it from [here](https://console.twilio.com/).
* API requesting applications like Postman, Insomnia, etc.
* NGROK for local testing.

### How to use it
To replicate the work of this repository and run it locally, you need to follow these steps:
* Create a `.env` file inside the root directory, and create these environmental variables:
    ```
    TWILIO_ACCOUNT_SID=YOUR ACCOUNT SID
    TWILIO_AUTH_TOKEN=YOUR AUTH TOKEN
    OPENAI_API_KEY=YOUR OPENAI API KEY
    FROM=TWILIO WHATSAPP NUMBER
    ```
This FROM variable in the .env file is the same for the Twilio WhatsApp Sandbox.
* Create a virtual environment and activate it before installing the packages
* install all the required dependencies from the `requirements.txt` file
```python
pip install -r requirements.txt
```
* run the server with either of the following commands
```python
python run.py
```
```python
gunicorn run:app
```
* start the NGROK engine on the same port as the Python application is running.
* provide the NGROk urlon `Twilio WhatsApp Sandbox` for all incoming requests.
* test the setup using your WhatsApp
