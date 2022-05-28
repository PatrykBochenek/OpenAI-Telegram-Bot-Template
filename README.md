# OpenAI-Telegram-Bot-Template

This is a simple template to create a telegram bot which utilises the OpenAI API to formulate responses to the user.

## 1.0 Prerequisites

Some prerequisites are required to use this template successfully:

  1.) An OpenAI API key. For this you need an OpenAI account with an attached payment method. 
   
  2.) Telegram bot & a bot authorisation token. How to create your bot and how to get its respective authorisation token is explained in section 2 below.
  
Both of these keys are then to be pasted into the constants.py file. 

```python
OPEN_AI_KEY = "ENTER YOUR OPEN AI API KEY HERE"
TELEGRAM_BOT_KEY = 'ENTER YOUR TELEGRAM BOTS KEY HERE'
```
## 1.1 Packages

Use the pip installer to install the [OpenAI package](https://openai.com/api/).

```bash
pip install openai
```

Use the pip installer to install the [Telegram Bot API](https://python-telegram-bot.org).

```bash
pip install python-telegram-bot
```


