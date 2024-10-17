from TrimoonCam2Telegram.cam2telegram_config import *

class BongaCams2Telegram(Cam2Telegram):
    def __init__(self, woopyXXXAuthDict=None, woopyXXXAuthEnv='.env'):
        super().__init__(woopyXXXAuthDict, woopyXXXAuthEnv)  # Passa gli argomenti al costruttore della classe base
        self.woopyxxx_cams_base_url = "https://bngprm.com/api/v2/"

    def bongacams_online_rooms(self, AffiliateTracking = None, ModelGender = None, Limit=None):
        Cam2TelegramAffTrack = self.woopyxxx_bongacams_aff_id if AffiliateTracking is None else AffiliateTracking
        Cam2TelegramLimitResponse = 10 if Limit is None else int(Limit)
        Cam2TelegramHeaders = {
            'c': Cam2TelegramAffTrack,
            'limit': Cam2TelegramLimitResponse,
            'client_ip': self.cam2telegram_GetMyIP(GetLanIp=False),
        }
        try:
            bongaResponse = requests.get(f"{self.woopyxxx_cams_base_url}models-online", params=Cam2TelegramHeaders)
            if bongaResponse.status_code == 200:
                # Estrai il contenuto JSON dalla risposta
                json_data = bongaResponse.json()['models']

                return json_data


            else:
                print("Errore nella richiesta:", bongaResponse.status_code)

                return None
        except Exception as e:
            print("Errore durante la richiesta:", e)
            return e

    def bongacams_online_rooms_raw(self, AffiliateTracking = None, ModelGender = None, Limit=None):

        CamJsonData = self.bongacams_online_rooms(AffiliateTracking = AffiliateTracking, ModelGender = ModelGender, Limit=Limit)

        WoopyXXX_CamsResponseManipulator = []
        for Cam in CamJsonData:
            WoopyXXXCamNormalizer = {}
            WoopyXXXCamNormalizer['source'] = 'bongacams'
            WoopyXXXCamNormalizer['source_link'] = 'https://bongacams8.com/track?v=2&c=310564'
            WoopyXXXCamNormalizer['username'] = Cam['username']
            WoopyXXXCamNormalizer['slug'] = Cam['username']
            WoopyXXXCamNormalizer['model_id'] = Cam['username']
            WoopyXXXCamNormalizer['gender'] = Cam['gender']
            WoopyXXXCamNormalizer['age'] = Cam.get('age', None)
            WoopyXXXCamNormalizer['country'] = Cam.get('homecountry', None)
            WoopyXXXCamNormalizer['language'] = Cam.get('primary_language', None)
            WoopyXXXCamNormalizer['profile_url'] = Cam.get('profile_page_url', None)
            WoopyXXXCamNormalizer['profile_image'] = Cam['profile_images']['thumbnail_image_big']
            WoopyXXXCamNormalizer['best_res_image'] = Cam['live_images']['thumbnail_image_big']
            WoopyXXXCamNormalizer['best_res_video'] = Cam.get('stream_feed_url', '')
            WoopyXXXCamNormalizer['room_url'] = Cam['chat_url']
            WoopyXXXCamNormalizer['new_performer'] = False
            WoopyXXXCamNormalizer['hd'] = Cam['is_hd']
            WoopyXXXCamNormalizer['viewers'] = Cam.get('members_count', None)
            WoopyXXXCamNormalizer['stream_time'] = Cam.get('online_time', None)
            GetCamTags = list(Cam.get('tags').values())
            WoopyXXXCamNormalizer['tags'] = GetCamTags
            WoopyXXX_CamsResponseManipulator.append(WoopyXXXCamNormalizer)

        return WoopyXXX_CamsResponseManipulator