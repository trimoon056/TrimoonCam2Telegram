import os
import socket
import requests
import random
from dotenv import load_dotenv
import json
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from pathlib import Path
from typing import List, Dict, Union
class Cam2Telegram:
    def __init__(self, woopyXXXAuthDict=None, woopyXXXAuthEnv='.env'):
        if woopyXXXAuthDict:
            self._update_auth_from_dict(woopyXXXAuthDict)
        else:
            load_dotenv(woopyXXXAuthEnv)
            self._load_env_variables()

    def _load_env_variables(self):
        self.woopyxxx_chaturbate_aff_campaign_id = os.environ.get("WOOPYXXX_CHATURBATE_AFF_ID", "f83lA")
        self.woopyxxx_bongacams_aff_id = os.environ.get("WOOPYXXX_BONGACAMS_AFF_ID", "310564")
        self.woopyxxx_camsoda_aff_id = os.environ.get("WOOPYXXX_CAMSODA_AFF_ID", "seoserviceit")
        self.woopyxxx_cam4_aff_id = os.environ.get("WOOPYXXX_CAM4_AFF_ID", "4277")

    def _update_auth_from_dict(self, woopyCamsAuthDict):
        self.woopyxxx_chaturbate_aff_campaign_id = woopyCamsAuthDict.get("woopyxxx_chaturbate_aff_campaign_id", "f83lA")
        self.woopyxxx_bongacams_aff_id = woopyCamsAuthDict.get("woopyxxx_bongacams_aff_id", "310564")
        self.woopyxxx_camsoda_aff_id = woopyCamsAuthDict.get("woopyxxx_camsoda_aff_id", "seoserviceit")
        self.woopyxxx_cam4_aff_id = woopyCamsAuthDict.get("woopyxxx_cam4_aff_id", "4277")

    def cam2telegram_GetMyIP(self, GetLanIp=True, GetCountryIp=None):
        if GetLanIp is False:
            try:
                # Effettua una richiesta HTTP a un servizio esterno per ottenere l'IP pubblico
                response = requests.get('https://api.ipify.org?format=json')
                # Estrai l'IP pubblico dalla risposta JSON
                ip_address = response.json()['ip']
                return ip_address
            except Exception as e:
                print("Errore durante il recupero dell'indirizzo IP pubblico:", e)
                return e
        else:
            try:
                # Ottieni l'hostname del computer
                hostname = socket.gethostname()
                # Ottieni l'indirizzo IP associato all'hostname
                ip_address = socket.gethostbyname(hostname)
                return ip_address
            except Exception as e:
                print("Errore durante il recupero dell'indirizzo IP:", e)
                return e