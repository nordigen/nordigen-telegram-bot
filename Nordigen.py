import requests
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
import speech_recognition as sr
import ffmpeg

class NordigenTelegramBot:

    def __init__(self, telegram_token: str, nordigen_token: str, user_id: str) -> None:
        self.__telegram_token = telegram_token
        self.__nordigen_token = nordigen_token
        self.__user_id = user_id

    def _get_balances(self):
        r = requests.get(f'https://ob.nordigen.com/api/accounts/{self.__user_id}/balances/', headers={'Authorization': f'Token {self.__nordigen_token}'})

        if r.status_code == 200:
            data = r.json()['balances'][0]['balanceAmount']
            balance = data['amount']
            currency = data['currency']
            return [balance, currency]

        return r.status_code

    def _start_command(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(
            "Welcome To Nordigen Bot! 🚀"
            "\nTo get started please insert your token and user id into .env file."
            "\nGet token and user id form our portal ➡ https://ob.nordigen.com/tokens/"
        )

    def _balance_command(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(f"💰 Your Revolut balance is...")
        balance, currency = self._get_balances()
        update.message.reply_text(f"{balance} {currency}")
        

    def _help_command(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text("Available commands: /start, /help, /balance, /about")

    def _handle_audio(self, update: Update, context: CallbackContext) -> None:
        chat_id = update.effective_message.chat.id
        file_name = '%s_%s%s.wav' % (chat_id, update.message.from_user.id, update.message.message_id)
        message = update.effective_message
        message.voice.get_file().download(file_name)
        transcript = self._audio_to_text(file_name)

        if 'balance' in transcript:
            self._balance_command(update, context)
            return

        update.message.reply_text("Didn't catch you. Please try again!")

    def _audio_to_text(self, file_name: str) -> str:
        stream = ffmpeg.input(file_name)
        stream = ffmpeg.output(stream, 'out.wav')
        ffmpeg.run(stream, quiet=True)

        r = sr.Recognizer()
        with sr.AudioFile('out.wav') as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            os.remove(f'./{file_name}')
            os.remove('./out.wav')
            return text

    def _about_command(self, update: Update, context: CallbackContext):

        update.message.reply_text(
            "Nordigen is an authorised Account Information Service Provider."
            "\nWe provide free access to bank data and premium data insights."
            "\nFouned in 2016."
            "\nMore information https://nordigen.com/en/"
        )

    def _handle_messages(self, update: Update, context: CallbackContext):
        # Get user text
        text = str(update.message.text)
        update.message.reply_text("Sorry at the moment i only can tell you youre balance account")

    def _error(self, update: Update, context):
        print(f"Update {update} caused error {context.error}")

    def start_bot(self) -> None:
        updater = Updater(self.__telegram_token, use_context=True)

        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", self._start_command))
        dp.add_handler(CommandHandler("help", self._help_command))
        dp.add_handler(CommandHandler("balance", self._balance_command))
        dp.add_handler(CommandHandler("about", self._about_command))
        dp.add_handler(MessageHandler(Filters.text, self._handle_messages))
        dp.add_handler(MessageHandler(Filters.voice, self._handle_audio))
        dp.add_error_handler(self._error)

        updater.start_polling(0)
        updater.idle()