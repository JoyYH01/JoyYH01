try:
    import requests
except:
    os.system("pip install requests")
try:
    import user_agent
except:
    os.system("pip install user_agent")
    
import requests,random,time
import os
from user_agent import generate_user_agent, generate_navigator
from pprint import pprint

print('\033[1;30m='*60)
print('\033[1;33m Dev: \033[1;32mhttps://t.me/YassaHany')
print('\033[1;30m='*60)
print('\033[1;33m Dev Channel: \033[1;32mhttps://t.me/YassaTeam')
print('\033[1;30m='*60)

ti = 11
code=input(str("\033[1;32m Enter Your Code: "))
print('\033[1;30m='*60)

def pro():
    ms = random.randint(0000,9999)
    purl=[f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout={ms}&country=all&ssl=no&anonymity=anonymous",f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout={ms}&country=all&ssl=no&anonymity=elite"]
    url1=random.choice(purl)
    pr = requests.get(url1).text
    list =pr.split()
    session = requests.Session()
    proxie= random.choice(list)
    
    session.proxies = {
   'http': f'http://{proxie}',
   'https': f'http://{proxie}',
   }
    cookies = {
    'Language': 'en-us',
    'PHPSESSID': '1ba2a9e3ece1456777acea6f8521a00f',
    }
    u=generate_user_agent(os=('android'))
    headers = {
    'authority': 'm.riotblockchain.live',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer null',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'Language=en-us; PHPSESSID=1ba2a9e3ece1456777acea6f8521a00f',
    'language': 'en',
    'origin': 'https://m.riotblockchain.live',
    'referer': 'https://m.riotblockchain.live/ar/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': u
    }
    cookies3 = {
    'Language': 'en-us',
    'PHPSESSID': '1ba2a9e3ece1456777acea6f8521a00f',
    }
    cookies2 = {
    'Language': 'en-us',
    'PHPSESSID': '1ba2a9e3ece1456777acea6f8521a00f',
    }
    json_data2 = {
    'id': 13,
    'coupon_id': '',
    }
    try:
        r=session.get("https://m.riotblockchain.live",timeout=ti)
    except:
        print("\033[1;31m False IP, Waiting...")
        
    else:
        print("\033[1;32m Done")
        
        for x in range(1):
            n=random.randint(11111111,99999999)
    
            users=requests.get("https://raw.githubusercontent.com/JoyYH01/JoyYH01/main/users.txt").text
            users=users.split()
            user=random.choice(users)
            user=str(user)
       
            json_data = {
            'username': f'{user}',
            'mobile': f'12{n}',
            'email': f'{user}@gmail.com',
            'password': 'Yassa123',
            'sms': '000000',
            'verify': f'{code}',
            'prefix': '20',
            'type': 1,
            }
            session.proxies = {
            'http': f'http://{proxie}',
            'https': f'http://{proxie}',
            }
            response = session.post('https://m.riotblockchain.live/v1/login/register', cookies=cookies, headers=headers, json=json_data,timeout=ti)
            print(response.text)
            co = (response.json()['msg'])
            if co=="Restricted Registration":
                print()
                time.sleep(2)
   
            elif co == "register successful":
                print()
                json_data3 = {
                'username': f'{user}@gmail.com',
                'password': 'Yassa123',
                }
                response3 = session.post('https://m.riotblockchain.live/v1/login/index', cookies=cookies3, headers=headers, json=json_data3,timeout=ti)
                print(response3.text)
                print()
                token= (response3.json()["data"])
                u=generate_user_agent(os=('android'))
                headers2 = {
                'authority': 'm.riotblockchain.live',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': f'Bearer {token}',
                'content-type': 'application/json;charset=UTF-8',
                'language': 'en',
                'origin': 'https://m.riotblockchain.live',
                'referer': 'https://m.riotblockchain.live/ar/',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'user-agent': u
                }
                time.sleep(2)
                response2 = session.post('https://m.riotblockchain.live/v1/order/create', cookies=cookies2, headers=headers2, json=json_data2,timeout=ti)
                print(response2.text)
                print()
                time.sleep(2)
    
            else:
                time.sleep(2)
                
for x in range(999):
    try:
        pro()
    except:
        y="Yassa"
    else:
        y="Hany"

       
