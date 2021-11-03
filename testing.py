import httpx, json, base64, random, threading
from time import time
import requests
import websocket
import undetected_chromedriver as uc
from urllib import parse
from json import dumps
import string
from test import cap

# Discord invite link
# Just replace with None if you don't want to join a server upon creation
#invite = "xxxxxx" # Only the string after /
invite = "6CTyYHJ2"

# Delay to wait after creating an account
delay = 10

# Enable email verification
# This also needs an extra captchakey for verification part
emailver = True

# Rotating proxy or does it use a list of proxies
rotating = True

# Debug mode, gives all information about what the gen is doing
debug = True

# Random usernames from a text file
usernames = []
with open('discord_usernames.txt', 'r', encoding='UTF-8') as discordnames:
    for x in discordnames:
        usernames.append(x)


sitekey = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
host = "discord.com"
discordratelimit = []


data = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./;<=>?@[\]^_`{|}~'''
dataE = '''abcdefghijklmnopqrstuvwxyz0123456789'''

uc.TARGET_VERSION = 91
options = uc.ChromeOptions()
options.headless=True
options.add_argument("--no-sandbox")
driver = uc.Chrome(options=options)
driver.execute_script("null")
hsw = open("hsw.js", "r").read()
def getcaptchakey(numbert, proxy):
    headersCONFIG = {
        "Host": "hcaptcha.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json; charset=utf-8",
        "Cache-Control": "no-cache",
        "Origin": "https://newassets.hcaptcha.com",
        "Connection": "keep-alive",
        "Referer": "https://newassets.hcaptcha.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers"
    }
    try:
        config = httpx.get("https://hcaptcha.com/checksiteconfig?host=discord.com&sitekey=f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34&sc=1&swa=1", headers=headersCONFIG, timeout=None, proxies=proxy)
        c = config.json()
        c["c"]["type"] = "hsw"
        c = dumps(c["c"])
        req = config.json()["c"]["req"]
    except:
        return False
    n = driver.execute_script(hsw + f"return hsw('{req}');")
    json = {
        "v": "7b183e4",
        "sitekey": "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34",
        "host": "discord.com",
        "hl": "en",
        "motionData": '{"v":1,"topLevel":{"st":1632506059500,"sc":{"availWidth":1366,"availHeight":734,"width":1366,"height":768,"colorDepth":24,"pixelDepth":24,"top":0,"left":0,"availTop":0,"availLeft":0,"mozOrientation":"landscape-primary","onmozorientationchange":null},"nv":{"permissions":{},"doNotTrack":"unspecified","maxTouchPoints":0,"mediaCapabilities":{},"oscpu":"Linux x86_64","vendor":"","vendorSub":"","productSub":"20100101","cookieEnabled":true,"buildID":"20181001000000","mediaDevices":{},"credentials":{},"clipboard":{},"mediaSession":{},"webdriver":false,"hardwareConcurrency":4,"geolocation":{},"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (X11)","platform":"Linux x86_64","userAgent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","product":"Gecko","language":"en-US","languages":["en-US","en"],"onLine":true,"storage":{},"plugins":[]},"dr":"","inv":false,"exec":false,"wn":[[1354,590,1,1632506059651]],"wn-mp":0,"xy":[[0,0,1,1632506059652]],"xy-mp":0,"mm":[[540,474,1632506059653],[541,473,1632506059702]],"mm-mp":49},"session":[],"widgetList":["075smy0yd1tm"],"widgetId":"075smy0yd1tm","href":"https://discord.com/","prev":{"escaped":false,"passed":false,"expiredChallenge":false,"expiredResponse":false}}',
        "n": n,
        "c": c
    }
    data = parse.urlencode(json)
    headersCAPTCHA = {
        "Host": "hcaptcha.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        #"Accept-Encoding": "gzip, deflate, br",
        "Content-type": "application/x-www-form-urlencoded",
        "Content-Length": str(len(data)),
        "Origin": "https://newassets.hcaptcha.com",
        "Connection": "keep-alive",
        "Referer": "https://newassets.hcaptcha.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Ch-Ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers"
    }
    try:
        cookies = {"hc_accessibility": "0A/jgkF8hJmTiHAKKtEDHfrxCwOBEhfwSzM9u8A87vRY2UOuHu7Xm/iR71bappwF+VhBZe2W8FaVzpioleqz9hOQlFbmKvSg1xAFsmh3VcWyJu4OjxJ6j39Qd0czB+e3b329f9iKVsgvaIfVTKp8sUdWy3Uqf9X7oR60+JtFYsZ3Kqtz9/UHS0S1l2cMBVMOUu2paokIWfsRRNPU++wJ12w1sfPohySN14OQ/3EDIc2Su9LS9UF/EVrlriRx3IMeb64fzHsEXKV5qBZsuTi6WvTfqamrhu+b8SDnFD0iMLxYl4QV+Zst5lXn+OTNkselStdfj2eGeELazDMkNUFgh7EnrAI5X+baMqhcbPDTvXA9MjXqAjaLYmuOBLpinHili0baKmUrW31wgq6rChpX7bDbIiUXx35JRkAyEA==rM0T7f/v8SQEfUiM"}
        captcha = httpx.post("https://hcaptcha.com/getcaptcha?s=f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34", cookies=cookies, headers=headersCAPTCHA, data=data, proxies=proxy, timeout=None)
        return captcha.json()["generated_pass_UUID"]
    except:
        return False

def ensurecaptchakey(numbert, proxy=None):
    dprint(numbert, "Getting captcha key...")
    while True:
        w = httpx.get("http://127.0.0.1:5000/")
        captchakey = w.text
        if captchakey != False:
            break
    return(captchakey)

def dprint(numbert, string):
    if debug == True:
        print(f"Thread {str(numbert)}: {string}")

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
    
number = 0
def accountgen(proxydiscord):
    global number
    number += 1
    numbert = number

    # Handling proxy
    
    origproxydiscord = proxydiscord
    username = random.choice(usernames)
    if proxydiscord == "None":
        proxydiscord = None
    else:
        proxydiscord = "http://"+proxydiscord
    url = "https://api.capmonster.cloud/getTaskResult"
    url_create = "https://api.capmonster.cloud/createTask"

    a = {
    "clientKey":"b4a08a0ca48c10fc9ebb120f204dc782",
    "task":
    {
        "type":"HCaptchaTaskProxyless",
        "websiteURL":"https://discord.com/register",
        "websiteKey":"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
    }
}
    while True:
        f = requests.Session()
        w = f.post(url_create, json=a).json()
        #{'errorId': 0, 'errorCode': '', 'errorDescription': '', 'taskId': 1404451391}
        taskId = w["taskId"]
        
        wasd = f.post(url, json={"clientKey":"b4a08a0ca48c10fc9ebb120f204dc782","taskId": taskId}).json()
        print(wasd)
        f = wasd["solution"]
        if f == None:
            print("None")
            pass
        else:
            break
    captchakey= f["gRecaptchaResponse"]
    

    with httpx.Client(timeout=None, proxies=proxydiscord) as client:

            #Getting of email
            email = "John"+random_char(6)+"@praisegang.com"

            dcfduid = "1bf20330382a11ec88f103abce84432e"
            sdcfduid = "1bf20331382a11ec88f103abce84432e11ca7fbb6efa3fa9b8e174b4af3570abc5105c4de373119ed863feb9964d5285"
            print(dcfduid)
            '''
            #Convert __sdcfduid to __dcfduid (Shouldn't use unless needed)
            dcfduid = sdcfduid[:7]+"0"+sdcfduid[8:32]
            '''

            # Get the fingerprint

            headersMAIN = {
            	"Host": "discord.com",
            	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
            	"Accept": "*/*",
            	"Accept-Language": "en-US",
            	#"Accept-Encoding": "gzip, deflate, br",
            	"X-Super-Properties": "eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2OjkxLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTEuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkxLjAiLCJvc192ZXJzaW9uIjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3MDk3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
            	"X-Context-Properties": "eyJsb2NhdGlvbiI6IkFjY2VwdCBJbnZpdGUgUGFnZSJ9",
            	"Authorization": "undefined",
            	"X-Debug-Options": "bugReporterEnabled",
            	"Connection": "keep-alive",
            	"Referer": "https://discord.com/register",
            	"Sec-Fetch-Dest": "empty",
            	"Sec-Fetch-Mode": "cors",
            	"Sec-Fetch-Site": "same-origin",
            	"TE": "trailers"
            }
            dprint(numbert, "Getting the fingerprint...")
            fingerprint = requests.get("https://discord.com/api/v9/experiments", headers=headersMAIN).json()["fingerprint"]
            print(fingerprint)
            headersMAIN.pop("X-Context-Properties")
            headersMAIN["X-Fingerprint"] = fingerprint
            password = "DetectiveVoke1!ontop"

            register = {"fingerprint":fingerprint,"email":email,"password":password,"username":username,"invite":invite,"consent":True,"gift_code_sku_id":None,"captcha_key":captchakey}

            # Registration headers

            headersREGISTER = {
                    "Host": "discord.com",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
                    "Accept": "*/*",
                    "Accept-Language": "en-US",
                    #"Accept-Encoding": "gzip, deflate, br",
                    "Content-Type": "application/json",
                    "Authorization": "undefined",
                    "X-Super-Properties": "eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2OjkxLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTEuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkxLjAiLCJvc192ZXJzaW9uIjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3MDk3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
                    "X-Fingerprint": fingerprint,
                    "Cookie": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}",
                    "X-Debug-Options": "bugReporterEnabled",
                    "Origin": "https://discord.com",
                    "Connection": "keep-alive",
                    "Referer": "https://discord.com/register",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "TE": "trailers"
            }

            # Register an account
            dprint(numbert, "Registering account...")
            registration = httpx.post("https://discord.com/api/v8/auth/register", headers=headersREGISTER, json=register, proxies=proxydiscord, timeout=None).json()
            registrationjson = registration
            print(registrationjson)
            try:
                token = registrationjson["token"]
                dprint(numbert, "Registration successful Token: "+token)
                ws = websocket.WebSocket()
                ws.connect("wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream")
                
                auth = {
                    "op":2,
                    "d": {
                    "token": token,
                    "capabilities": 61,
                    "properties": {"os":"Windows","browser":"Chrome","device":"","system_locale":"en-GB","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36","browser_version":"90.0.4430.212","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":"85108","client_event_source":"null"}, 
                    "presence": {
                        "status":"online",
                        "since":0,
                        "activities":[],
                        "afk":False
                    },
                    "compress":False,
                    "client_state":{
                        "guild_hashes":{},
                        "highest_last_message_id":"0",
                        "read_state_version":0,
                        "user_guild_settings_version":-1
                    }
                    }
                }

                ws.send(json.dumps(auth))
                ws.recv()
                ws.close()
            except Exception as e:
                print(e)
                dprint(numbert, "Registration unsuccessful. Error:")
                print("RESPONSE CODE:", str(registration.status_code)+"\nRESPONSE CONTENT: ",registration.content.decode('utf-8'))
                exit()

            headersMAIN["Authorization"] = token
            headersMAIN["Content-Type"] = "application/json"
            headersMAIN["Origin"] = "https://discord.com"


            print(f"fully done with one acc yk g")
            with open("tokens.txt","a+") as f:
                f.write(f"\n{token}")
            with open("tokensp.txt","a+") as f:
                f.write(f"\n{token}:{email}:{password}")


# Parsing proxies
proxiesdiscord = ["142.202.220.242:1899:kederli8uGY:TR4js9b8kvF6x1p3_country-UK"]

try:
    threads = int(input("Number of threads to use: "))
    #threads = 125
    origthreads = threads
except:
    print("Please input a valid number")
    exit()
while True:
    for i in range(threads-(threading.active_count()-1)):
        threading.Thread(target=accountgen, args=(proxiesdiscord[0],)).start()