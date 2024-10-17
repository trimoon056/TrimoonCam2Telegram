from TrimoonCam2Telegram.telegram.TelegramPublisher import *
TelegramBotToken = ""
TelegramChatID = ""
MarkDownTest = [
    {'text' : f'🔞 Adult Dating 🔞', 'url' : ''},
    {'text' : f'🚹 Gay Dating 🔞', 'url' : ''}
]
Results = TrimoonTelegramPublisher().TelegramPublishBot(BotToken=TelegramBotToken, ChatId=TelegramChatID, MarkDown=MarkDownTest)
print(Results)
