import requests
import time

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



def cap():
    f = requests.Session()
    w = f.post(url_create, json=a).json()
    #{'errorId': 0, 'errorCode': '', 'errorDescription': '', 'taskId': 1404451391}
    taskId = w["taskId"]
    time.sleep(10)
    wasd = f.post(url, json={"clientKey":"b4a08a0ca48c10fc9ebb120f204dc782","taskId": taskId}).json()
    print(wasd)
    f = wasd["solution"]
    return f["gRecaptchaResponse"]

