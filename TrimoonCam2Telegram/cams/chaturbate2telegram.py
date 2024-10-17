from TrimoonCam2Telegram.cam2telegram_config import *
class Chaturbate2Telegram(Cam2Telegram):
    def __init__(self, woopyXXXAuthDict=None, woopyXXXAuthEnv='.env'):
        super().__init__(woopyXXXAuthDict, woopyXXXAuthEnv)  # Passa gli argomenti al costruttore della classe base
        self.woopyxxx_cams_base_url = "https://chaturbate.com/api/public/affiliates/onlinerooms/"

    def chaturbate_online_rooms(self, AffiliateTracking = None, ModelGender = None, Limit=None):

        Cam2TelegramAffTrack = self.woopyxxx_chaturbate_aff_campaign_id if AffiliateTracking is None else AffiliateTracking
        Cam2TelegramLimitResponse = 10 if Limit is None else int(Limit)
        Cam2TelegramHeaders = {
            'wm' : Cam2TelegramAffTrack,
            'limit' : Cam2TelegramLimitResponse,
            'client_ip': self.cam2telegram_GetMyIP(GetLanIp=False),
        }
        ALLOWED_GENDERS = ["m", "f", "t", "c"]
        gender_value = ModelGender
        if gender_value:
            if isinstance(gender_value, str):
                if gender_value in ALLOWED_GENDERS:
                    Cam2TelegramHeaders['gender'] = gender_value
                else:
                    pass
            elif isinstance(gender_value, (list, tuple)):
                Cam2TelegramHeaders['gender'] = list(gender_value)

        try:
            woopyxxx_camsResponse = requests.get(self.woopyxxx_cams_base_url, params=Cam2TelegramHeaders)

            if woopyxxx_camsResponse.status_code == 200:
                # print(woopyxxx_camsResponse.url)
                # Estrai il contenuto JSON dalla risposta
                json_data = woopyxxx_camsResponse.json()
                return json_data['results']
            else:
                print("Errore nella richiesta:", woopyxxx_camsResponse.status_code)

                return None
        except Exception as e:
            print("Errore durante la richiesta:", e)
            return e

    def chaturbate_online_rooms_raw(self, AffiliateTracking = None, ModelGender = None, Limit=None):

        CamJsonData = self.chaturbate_online_rooms(AffiliateTracking = AffiliateTracking, ModelGender = ModelGender, Limit=Limit)

        WoopyXXX_CamsResponseManipulator = []
        for Cam in CamJsonData:
            WoopyXXXCamNormalizer = {}
            WoopyXXXCamNormalizer['source'] = 'chaturbate'
            WoopyXXXCamNormalizer['source_link'] = 'https://chaturbate.com/in/?tour=grq0&campaign=f83lA&track=default'
            WoopyXXXCamNormalizer['username'] = Cam['username']
            WoopyXXXCamNormalizer['slug'] = Cam['slug']
            WoopyXXXCamNormalizer['model_id'] = Cam['slug']
            WoopyXXXCamNormalizer['gender'] = Cam['gender']
            WoopyXXXCamNormalizer['age'] = Cam.get('age', None)
            WoopyXXXCamNormalizer['country'] = Cam.get('country', None)
            WoopyXXXCamNormalizer['language'] = Cam.get('spoken_languages', None)
            WoopyXXXCamNormalizer['profile_image'] = Cam['image_url']
            WoopyXXXCamNormalizer['profile_url'] = Cam['chat_room_url_revshare']
            WoopyXXXCamNormalizer['best_res_image'] = Cam['image_url']
            WoopyXXXCamNormalizer['best_res_video'] = ""
            WoopyXXXCamNormalizer['room_url'] = Cam['chat_room_url_revshare']
            WoopyXXXCamNormalizer['new_performer'] = Cam['is_new']
            WoopyXXXCamNormalizer['hd'] = Cam['is_hd']
            WoopyXXXCamNormalizer['viewers'] = Cam.get('num_users', None)
            WoopyXXXCamNormalizer['stream_time'] = Cam.get('seconds_online', None)
            WoopyXXXCamNormalizer['tags'] = Cam.get('tags', '')
            WoopyXXX_CamsResponseManipulator.append(WoopyXXXCamNormalizer)

        return WoopyXXX_CamsResponseManipulator