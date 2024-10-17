import json
from TrimoonCam2Telegram import *
from TrimoonCam2Telegram.telegram.TelegramCustom import *
class TrimoonTelegramPublisher(Chaturbate2Telegram):
    def __init__(self, woopyXXXAuthDict=None, woopyXXXAuthEnv='.env'):
        super().__init__(woopyXXXAuthDict, woopyXXXAuthEnv)  # Passa gli argomenti al costruttore della classe base
        self.woopyxxx_cams_base_url = "https://chaturbate.com/api/public/affiliates/onlinerooms/"

    def TelegramPublishBot(self, BotToken=None, ChatId=None, WebcamSite = None, WecamParam=None, MarkDown = None):

        Limit = WecamParam['limit'] if WecamParam is not None and 'limit' in WecamParam and WecamParam['limit'] else None
        ModelGender = WecamParam['modelgender'] if WecamParam is not None and 'limit' in WecamParam and WecamParam['modelgender'] else "f"

        if WebcamSite is None:
            CbResponse = Chaturbate2Telegram().chaturbate_online_rooms_raw(ModelGender=ModelGender, Limit=Limit)
            BongaResponse = BongaCams2Telegram().bongacams_online_rooms_raw(ModelGender=ModelGender, Limit=Limit)
            CamSodaResponse = CamSoda2Telegram().camsoda_online_rooms_raw(ModelGender=ModelGender, Limit=Limit)
            CamResponse = CbResponse + BongaResponse + CamSodaResponse
            random.shuffle(CamResponse)
        elif WebcamSite.lower() == "chaturbate":
            CamResponse = Chaturbate2Telegram().chaturbate_online_rooms_raw(ModelGender=ModelGender, Limit=Limit)
        elif WebcamSite.lower() == "bongacams":
            CamResponse = BongaCams2Telegram().bongacams_online_rooms_raw(ModelGender=ModelGender, Limit=Limit)
        elif WebcamSite.lower() == "camsoda":
            CamResponse = CamSoda2Telegram().camsoda_online_rooms_raw(ModelGender=ModelGender, Limit=Limit)
        else:
            CbResponse = Chaturbate2Telegram().chaturbate_online_rooms_raw(ModelGender=ModelGender, Limit=Limit)
            BongaResponse = BongaCams2Telegram().bongacams_online_rooms_raw(ModelGender=ModelGender, Limit=Limit)
            CamSodaResponse = CamSoda2Telegram().camsoda_online_rooms_raw(ModelGender=ModelGender, Limit=Limit)
            CamResponse = CbResponse + BongaResponse + CamSodaResponse
            random.shuffle(CamResponse)

        RandomModelIndex = CamResponse[random.randint(0, len(CamResponse) -1)]
        RoomUrl = RandomModelIndex['room_url']
        ImageUrl = RandomModelIndex['best_res_image']
        TelegramMessage = f"👠 Watch: \"*{RandomModelIndex['username']}*\" on [{RandomModelIndex['source'].title()}]({RandomModelIndex['source_link']})\n🔞 Anni: {RandomModelIndex['age']}\n🔥 Best cam Bot : [Freepornwebcam_bot](https://t.me/Freepornwebcam_bot)"
        MarkDownList = []
        if MarkDown is None:
            MarkDownList.append({'text': f'Watch 🔞 \"{RandomModelIndex['username']}\" 🔞 on *{RandomModelIndex['source'].title()}*', 'url': RoomUrl})
            MarkDownList.append({'text' : f"🎥 Free Porn Webcam XXX 🔞 Channel", 'url' : 'https://t.me/freepornwebcam'})
        else:
            MarkDownList.append({'text': f'Watch 🔞 \"{RandomModelIndex['username']}\" 🔞 on *{RandomModelIndex['source'].title()}*','url': RoomUrl})
            for TheButton in MarkDown:
                MarkDownList.append(TheButton)
            MarkDownList.append({'text': "🎥 Free Porn Webcam XXX 🔞 Channel", 'url': 'https://t.me/freepornwebcam'})

        ResponseTelegram = Cam2TelegramCustom().send_photo_message(TelegramBotToken=BotToken, TelegramChatId=ChatId, MessageContent=TelegramMessage, ImagePath=ImageUrl, MarkDown=MarkDownList)
        return ResponseTelegram


