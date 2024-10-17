from TrimoonCam2Telegram.cam2telegram_config import *

class Cam2TelegramCustom(Cam2Telegram):
    def __init__(self):
        pass

    def send_photo_message(self, TelegramBotToken = None, TelegramChatId = None, ImagePath = None, MessageContent = None, MarkDown = None):
        Cam2TelegramBotInit = telebot.TeleBot(TelegramBotToken)

        if MarkDown is not None and isinstance(MarkDown, list):
            Woopymarkdown = self.parse_markdown(TelegramButtons=MarkDown)
            TelegramMessageSenderResponse = Cam2TelegramBotInit.send_photo(TelegramChatId, ImagePath, caption=MessageContent, reply_markup=Woopymarkdown, parse_mode='MARKDOWN')
        else:
            TelegramMessageSenderResponse = Cam2TelegramBotInit.send_photo(TelegramChatId, ImagePath, caption=MessageContent, parse_mode="MARKDOWN")

        return TelegramMessageSenderResponse

    def parse_markdown(self, TelegramButtons=List[Dict[str, str]]):
        markup = InlineKeyboardMarkup()
        for button in TelegramButtons:
            markup.add(InlineKeyboardButton(
                text=self._clean_markdown_for_button(button['text']),
                url=button['url']
            ))
        return markup

    def _clean_markdown_for_button(self, text: str) -> str:
        """Rimuove i caratteri di formattazione Markdown non supportati nei bottoni."""
        # I bottoni supportano solo grassetto e corsivo
        text = text.replace('`', '')  # Rimuove il formato codice
        text = text.replace('~', '')  # Rimuove il formato barrato
        text = r"\." if "." in text else text
        return text
