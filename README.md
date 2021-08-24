# Nordigen Telegram bot

Telegram bot that retrieves your bank account balance from your bank using Nordigen’s free account information API. You can get your bank account balance by using command `/balance` or by recording a voice message.

## Introduction

Nordigen Telegram bot is a hobby project built by Nordigen’s team to showcase the features of our API. This bot is meant for developers who want to experiment with open banking APIs and want to add more functionality to their bank accounts.

To create and configure it, please follow the following steps:

* Register on [ob.nordigen.com](https://ob.nordigen.com/) and connect your bank via API as detailed in our [Quickstart Guide](https://nordigen.com/en/account_information_documenation/integration/quickstart_guide_postman/). To save time, we recommend using our [swagger file](https://ob.nordigen.com/api/swagger.json) in Postman.

* Create a new personal Telegram Bot by starting a chat with `@BotFather` on Telegram, clicking Start and choosing the bot’s name and username. Once it is created, BotFather will provide you with a token that you will need in later steps

* Install the bot’s logic and configure it as described in the steps below.

---
## Requirements

* Python >= 3.7
* [Nordigen](https://ob.nordigen.com/) token
* Telegram API key, you can get one simply with [@BotFather](https://core.telegram.org/bots#botfather) with simple commands right after creating your bot.

---

## Instalation

1. Clone repository

`git clone https://github.com/victory-sokolov/nordigen-telegram-bot`

2. Install python dependencies using `poetry` or `pip`

`pip install -r requirements.txt` or `poetry install`

3. In order to use audio recognition, you have to install `FFmpeg` which is used to convert `.og` Telegram audio file to `.wav` to use it with `speech_recognition` package.
   
### Linux

For Debian based distribution 

`sudo apt install ffmpeg`

### macOS

Install `ffmpeg` using homebrew

`brew install ffmpeg`

### Windows

In order to use `ffmpeg` in Windows, you cna download `.exe` file from official site https://ffmpeg.org/download.html

or using [Chocolatey](https://chocolatey.org/) package manager

`choco install ffmpeg`

---

## Usage Example

1. Add your Telegram and Nordigen credentials to `.env.local` file.
`USER_ID` can be retrieved from `ob.nordigen.com` url when clicking on `transacitons`, `details` or `balances`

```
TELEGRAM_API_KEY=<TELEGRAM_API_KEY>
NORDIGEN_TOKEN=<NORDIGEN_TOKEN>
NORDIGEN_ACCOUNT_ID=<NORDIGEN_ACCOUNT_ID>
```

2. Run the script `python main.py`

---

## Available commands

* `/start` - start the bot and get instruction info
* `/help` - list available commands
* `/about` - short info about Nordigen
* `/balance` - get your balance
