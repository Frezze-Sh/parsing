# import requests
# from selenium import webdriver
# def fetch (url,params):
#     headers = params["headers"]
#     body = params["body"]
#     method = params["method"]
#     if method == "POST":
#         return requests.post(url, headers=headers, data=body)
#     if method == "GET":
#         return requests.get(url, headers=headers)
#
# amulets = fetch("https://auto.ru/-/ajax/desktop-search/listing/", {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#     "content-type": "application/json",
#     "priority": "u=1, i",
#     "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Opera GX\";v=\"122\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "same-origin",
#     "sec-fetch-site": "same-origin",
#     "x-client-app-version": "462.0.18065713",
#     "x-client-date": "1763821280706",
#     "x-csrf-token": "ade8b387848643be81b48eb820915184ea7d0d6e44f63c9b",
#     "x-page-request-id": "46f87e11e3585439d3e4edecd8bc070a",
#     "x-requested-with": "XMLHttpRequest",
#     "x-retpath-y": "https://auto.ru/cars/chery/amulet/all/?query=chery+amulet&from=searchline",
#     "cookie": "suid=d8021a6fc81270f988ac1accd4104af6.e951eb905a849e3ec176efe8397b988a; _csrf_token=ade8b387848643be81b48eb820915184ea7d0d6e44f63c9b; autoruuid=g69219e36289orh2ad8ev8jq9f44arop.a40bd1898ac37c0ad529e60f5ab9ed34; Session_id=3:1763810876.5.0.1716322107055:3bAaVQ:2.1.2:1|1982976151.0.2.3:1716322107|61:11420453.263959.VsuD4N2LLyVIulUcjc05L3vxBOQ; sessar=1.1396519.CiA8AQhPeJW6vwqFCI8uUV0gkoDOqXbQqZSD2LV-jQlMXQ.PxRIH2U3A63P6AKgJ4_NROkcTMdHaWK-gffk3NBIauo; yandex_login=Frezze-Sh; ys=udn.cDpGcmV6emUtU2g%3D#c_chck.1962770998; i=+t2Dk/FCoji3ESpIcFodkyJ/LZxC0ZYm0Nhbdyzwu8Z2m86x7ugtSXGrxuR/oZ5hkUnYaW5B1yVwv4EiOS58t8fweZM=; yandexuid=4250315921672005611; mda2_beacon=1763810876355; sso_status=sso.passport.yandex.ru:synchronized; autoru_sid=128447557%7C1763810879693.259200.jxs9Kg2-GbmbOoOY-iZ1mg.4o4SvTP9uDFfxvLPvV87-Zp5OTJx3uKtBu3OCbGLMFM; SLO_G_WPT_TO=ru; SLO_GWPT_Show_Hide_tmp=1; SLO_wptGlobTipTmp=1; _ym_uid=1763810886545506301; yaPassportTryAutologin=1; _ym_isad=2; crookie=ov4i6+c2b8tvqCOwdGev7MkJstQ4V74onJ/f0emHluJNPlbeWfA4b7SFEm/KN+0VEu3rt6pPvsdj/BzQp64SZY6+FO8=; cmtchd=MTc2MzgxMDg4Nzc0Mg==; fp=bd38946d9f5a2b1c2bfdb50f00f9a7a4%7C1763810887962; los=1; bltsr=1; coockoos=7; geo_onboarding_shown=true; autoru-visits-count=1; gdpr=0; from=direct; popups-union-promo-mag-shown-count=1; _ym_d=1763821261; _yasc=lXnwnCvs+n5gKZpLvRq86d68LavugjDd9l3wyWlbWc9sfw3XAiTnjsIM0REyJHCZZmHr; autoru_crashreport={%22route_name%22:%22listing%22%2C%22app_id%22:%22af-desktop-search%22%2C%22time_spent%22:%221%22%2C%22chat_indicator_unread%22:false}; count-visits=7; from_lifetime=1763821267048; layout-config={\"screen_height\":1080,\"screen_width\":1920,\"win_width\":996,\"win_height\":956}",
#     "Referer": "https://auto.ru/cars/chery/amulet/all/?query=chery+amulet&from=searchline"
#   },
#   "body": "{\"with_discount\":true,\"catalog_filter\":[{\"mark\":\"CHERY\",\"model\":\"AMULET\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\",\"geo_id\":[]}",
#   "method": "POST"
# })
#
# offers = amulets.json()["offers"]
#
# for offer in offers:
#     print(offer["price_info"]["RUR"])
#     print(offer["seller"]["location"])


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Постоянный путь к драйверу
DRIVER_PATH = r"C:\Users\orazl\.wdm\drivers\chromedriver\win64\142.0.7444.175\chromedriver-win32\chromedriver.exe"


# Создаем сервис и браузер
service = Service(DRIVER_PATH)
browser = webdriver.Chrome(service=service)

# Использование
browser.get("https://hh.ru/?customDomain=1")
print("Работает!")
time.sleep(10)
# browser.quit()