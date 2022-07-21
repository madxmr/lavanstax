from distutils.log import error

from traceback import print_tb
from .language import LANG, COUNTRY, LANGUAGE, TZ
from rich.prompt import Prompt, Confirm
from asyncio import get_event_loop
from lavan_installer import *
from time import time
from . import console
from git import Repo
import requests
import heroku3
import base64
import random
import os

LANG = LANG['MAIN']
Client = None

def connect (api):
    heroku_conn = heroku3.from_key(api)
    try:
        heroku_conn.apps()
    except:
        hata(LANG['INVALID_KEY'])
        exit(1)
    return heroku_conn

def createApp (connect):
    appname = "lavanstax" + str(time() * 1000)[-4:].replace(".", "") + str(random.randint(0,500))
    try:
        connect.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        hata(LANG['MOST_APP'])
        exit(1)
    return appname

def hgit (connect, repo, appname):
    global api
    app = connect.apps()[appname]
    giturl = app.git_url.replace(
            "https://", "https://api:" + api + "@")

    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        hata(LANG['ERROR'] + str(e))

    bilgi(LANG['POSTGRE'])
    app.install_addon(plan_id_or_name='062a1cc7-f79f-404c-9f91-135f70175577', config={})
    basarili(LANG['SUCCESS_POSTGRE'])
    return app


if __name__ == "__main__":
    logo(LANGUAGE)
    loop = get_event_loop()
    api = soru(LANG['HEROKU_KEY'])
    bilgi(LANG['HEROKU_KEY_LOGIN'])
    heroku = connect(api)
    basarili(LANG['LOGGED'])

   
    #username = soru(LANG['USERNAME'])
    #if username.startswith('@'):
     #   hata('@ kullanmadan giriniz')
      #  exit()
    # password = soru(LANG['PASSWORD'])
   
    #try:
     # instacli(username, password)
    #except ClientLoginError:
     #   hata('Kullanıcı adı veya şifre yanlış')
      #  exit()

 # İnstagram #
    try:
       os.system('node str.js')
       basarili(LANG['LOGGED'])
    except:
       hata("Bir hata oluştu!")
       exit()
    

    
       

    baslangic = time()


    # Heroku #
    bilgi(LANG['CREATING_APP'])
    appname = createApp(heroku)
    basarili(LANG['SUCCESS_APP'])
    onemli(LANG['DOWNLOADING'])

    
    enc = 'aHR0cHM6Ly9naXRodWIuY29tL0JlcjR0YmV5L0xhdmFuc3RheA=='
    enc1 = enc.encode('ascii')
    lavan = base64.b64decode(enc1)
    lavander = lavan.decode('ascii')

    if os.path.isdir("./Lavanstax/"):
        rm_r("./Lavanstax/")
    repo = Repo.clone_from(lavander,"./Lavanstax/", branch="master")
    onemli(LANG['DEPLOYING'])
    app = hgit(heroku, repo, appname)
    config = app.config()

    onemli(LANG['WRITING_CONFIG'])
    username = os.environ.get('username')
    password = os.environ.get('password')
    config['USERNAME'] = username
    config['PASSWORD'] = password
    config['PREFIX'] = "."
    config['LANG'] = LANGUAGE
    config['HEROKU_API_KEY'] = api
    config['HEROKU_APPNAME'] = appname
    config['COUNTRY'] = COUNTRY
    config['AFK_MESSAGE'] = "Hayat çok kısa, yapacak çok şey var...\nOnlardan birini yapıyorum.. Sahibim şuanda #AFK"
    config['SEND_READ'] = 'false'
    config['PENDING_REQUEST'] = 'false'
    config['FOLLOW_SEND'] = 'true'
    



   
 

    basarili(LANG['SUCCESS_CONFIG'])
    bilgi(LANG['OPENING_DYNO'])

    try:
        app.process_formation()["worker"].scale(1)
    except:
        hata(LANG['ERROR_DYNO'])
        exit(1)

    basarili(LANG['OPENED_DYNO'])
    basarili(LANG['SUCCESS_DEPLOY'])
    tamamlandi(time() - baslangic)
    

    


basarili(LANG['SEEYOU'])
