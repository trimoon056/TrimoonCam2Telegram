from TrimoonCam2Telegram.cam2telegram_config import *
class CamSoda2Telegram(Cam2Telegram):
    def __init__(self, woopyXXXAuthDict=None, woopyXXXAuthEnv='.env'):
        super().__init__(woopyXXXAuthDict, woopyXXXAuthEnv)  # Passa gli argomenti al costruttore della classe base
        self.woopyxxx_cams_base_url = "https://feed.camsoda.com/api/v1/"

    def camsoda_online_rooms(self, AffiliateTracking = None, ModelGender = None, Limit=None):
        woopyxxx_cams_CamSodaApiEndpoint = "browse/online_embed"
        woopyxxx_cams_apiUrlConstructor = f"{self.woopyxxx_cams_base_url}{woopyxxx_cams_CamSodaApiEndpoint}"
        Cam2TelegramAffTrack = self.woopyxxx_chaturbate_aff_campaign_id if AffiliateTracking is None else AffiliateTracking
        Cam2TelegramLimitResponse = 10 if Limit is None else int(Limit)
        Cam2TelegramHeaders = {
            'id': Cam2TelegramAffTrack,
            'length': Cam2TelegramLimitResponse,
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
            camsodaResponse = requests.get(woopyxxx_cams_apiUrlConstructor, params=Cam2TelegramHeaders)

            if camsodaResponse.status_code == 200:
                #print(camsodaResponse.url)
                # Estrai il contenuto JSON dalla risposta
                json_data = camsodaResponse.json()
                return json_data['results']
            else:
                print("Errore nella richiesta:", camsodaResponse.status_code)
                return None
        except Exception as e:
            print("Errore durante la richiesta:", e)
            return e

    def camsoda_online_rooms_raw(self, AffiliateTracking = None, ModelGender = None, Limit=None):
        CamJsonData = self.camsoda_online_rooms(AffiliateTracking = AffiliateTracking, ModelGender = ModelGender, Limit=Limit)
        WoopyXXX_CamsResponseManipulator = []
        for Cam in CamJsonData:
            WoopyXXXCamNormalizer = {}
            WoopyXXXCamNormalizer['source'] = 'camsoda'
            WoopyXXXCamNormalizer['source_link'] = 'https://www.camsoda.com/?id=seoserviceit&type=PPS'
            WoopyXXXCamNormalizer['username'] = Cam['name']
            WoopyXXXCamNormalizer['slug'] = Cam['username']
            WoopyXXXCamNormalizer['model_id'] = Cam['user_id']
            WoopyXXXCamNormalizer['gender'] = Cam.get('gender', '')
            WoopyXXXCamNormalizer['age'] = Cam.get('age', None)
            WoopyXXXCamNormalizer['country'] = Cam.get('country', None)
            WoopyXXXCamNormalizer['language'] = Cam.get('language', None)
            WoopyXXXCamNormalizer['profile_url'] = Cam.get('link', None)
            WoopyXXXCamNormalizer['profile_image'] = Cam.get('thumb', '')
            WoopyXXXCamNormalizer['best_res_image'] = Cam.get('thumb', '')
            WoopyXXXCamNormalizer['best_res_video'] = Cam.get('vthumb', '')
            WoopyXXXCamNormalizer['room_url'] = Cam['link']
            WoopyXXXCamNormalizer['room_iframe'] = Cam['link_iframe']
            WoopyXXXCamNormalizer['new_performer'] = Cam['is_new']
            WoopyXXXCamNormalizer['hd'] = Cam.get('is_hd', True)
            WoopyXXXCamNormalizer['viewers'] = Cam.get('viewers', None)
            WoopyXXXCamNormalizer['stream_time'] = Cam.get('seconds_online', random.randint(10,39472))
            WoopyXXXCamNormalizer['tags'] = Cam.get('tags', '')
            WoopyXXX_CamsResponseManipulator.append(WoopyXXXCamNormalizer)

        return WoopyXXX_CamsResponseManipulator