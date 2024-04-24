import requests


speaker_id = {'楠楠鹿':"1f653bed-c952-4534-af2d-e27ea2871988", '何同学':"9b39d819-c2f0-4bc6-a2da-bd75ffbad110",
              '白岩松':"844057ee-6b02-4da5-9145-0cd3cba5fc69", '鞠婧祎':"3f731111-0ab7-423c-afab-606b11e0fa23",
              '静静':"ebf9e565-19fa-4247-829f-44ef8c251a6f", '白洲梓':"c52b7b46-4e3e-4084-b35d-9b83c1f6e271",
              '范式':"93d0a185-f650-492e-8d77-7c1b4f516cb8", '蔡徐坤':"3e46c4d4-f4ed-44e1-b7c8-e5d4c4287f64",
              '马督工':"703cd0f9-24a4-41d7-8dac-708bdbc0fea2", '爱丽丝':"6e182506-44a3-4031-9674-86320d4d281c",
              '马老师':"bf2227ed-f2c4-4fb7-9c43-52ba5e75c270", 'hanser':"27f8b4d6-39a7-472e-b0bf-535b064e7454",
              '丁真':"0da57668-a4fe-47df-a0b9-b0ad1381bd51", '贾玲':"0bb12f68-8da5-4db2-89e7-d7f85ac9fe0f",
              '敖厂长':"bb048e6a-bda0-4c58-a3ca-a7d9c938f24f", '姜文':"5ca7efaa-ed0e-41a6-bec0-cbfb23ebda66"}
def call_gen_api(text:str, speaker:str = '静静',  mode:str="balance"):
    url = 'https://v1.reecho.cn/api/welcome/generate'
    json_data = {"voiceId": speaker_id[speaker], "text": text, "mode": mode}
    response = requests.post(url, json=json_data)
    json_raw = response.json()
    print(f"json_raw: {json_raw}")
    dl_url = json_raw['data']['url']
    return dl_url

def dl_mp3(dl_url:str, dl_name:str):
    import ssl, urllib.request
    ssl._create_default_https_context = ssl._create_unverified_context
    print(f"downloading {dl_name} from {dl_url}")
    urllib.request.urlretrieve(dl_url, dl_name)

text = "这么简单的问题怎么还没有解决。"
import random
import time
for speaker in speaker_id.keys():
    dl_url = call_gen_api(text=text, speaker=speaker)
    dl_name = f"{speaker}.mp3"
    dl_mp3(dl_url=dl_url, dl_name=dl_name)
    sleep_time = 5 + random.randrange(5)
    time.sleep(sleep_time)
