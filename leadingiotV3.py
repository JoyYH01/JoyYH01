import os
try:
    import requests
except:
    os.system("pip install requests")
try:
    import user_agent
except:
    os.system("pip install user_agent")
    
import requests,random,threading
from user_agent import generate_user_agent, generate_navigator
from pprint import pprint



code = "LIO9ES"
id = "45694"


def pro():
    purl=["https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all","https://rootjazz.com/proxies/proxies.txt"]
    url1=random.choice(purl)
    pr = requests.get(url1).text
    list =pr.split()
    session = requests.Session()
    proxie= random.choice(list)
    
    
    session.proxies = {
   'http': f'http://{proxie}',
   'https': f'http://{proxie}',
   }
    try:
        r=session.post("https://www.leadingiot.com/pages/login/reg/",timeout=7)
    except:
        print("\n False")
        
    else:
        for x in range(1):
            u=generate_user_agent(os=('android'))
            headers = {
            'authority': 'api.leadingiot.com',
            'accept': '*/*',
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://www.leadingiot.com',
            'referer': 'https://www.leadingiot.com/',
            'token': '',
            'user-agent': u,
            }
            list=["12","11","10"]
            n=random.randint(00000000,99999999)
            n3=random.choice(list)
            n2=random.randint(000,999)
            json_data = {
            'username': f'{n3}{n}',
            'password': '123321',
            'pay_pass': '153153',
            're_pass': '123321',
            'code': '',
            'invite_code': code,
            'country_code': '+20',
            'driver': 'android',
            'device': f'SM-M{n2}BR',
            'utype': 2,
            'openid': '',
            'nickname': '',
            'sex': '',
            'province': '',
            'city': '',
            'headimgurl': '',
            'unionid': '',
            'is_app': 1,
            'undefined': '153153',
            'share_data': '',
            'wx_openid': '',
            'deviceId': f'167538332810{n}',
            }
            response = session.post('https://api.leadingiot.com/reg', headers=headers, json=json_data,timeout=7).json()
            
            #print(response)
#            print()
            
            try:
                token=(response['token'])
            
            except:
                print("\n False1")
            
            else:
                user=(f'{n3}{n}')
                user=str(user)
                uu=(user+"\n")
                print(uu)
                
                json_data = {
                'username': f'{n3}{n}',
                'password': '123321',
                'device': f'SM-M{n2}BR',
                'driver': 'android',
                'deviceId': f'167538332810{n}',
                'userAgent': f'H{n2}',
                'google_code': '',
                }
                response = session.post('https://api.leadingiot.com/login', headers=headers, json=json_data,timeout=7).json()
                token=(response['token'])
                
                #print(response)
#                print()

                headers = {
                'authority': 'api.leadingiot.com',
                'accept': '*/*',
                'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json',
                'origin': 'https://www.leadingiot.com',
                'referer': 'https://www.leadingiot.com/',
                'token': token,
                'user-agent': u,
                }
                
                json_data = {
                'item_id': id,
                }
                response = session.post('https://api.leadingiot.com/done_haggle_user_robot', headers=headers, json=json_data,timeout=7)
                #print(response.text)
#                print()
                json_data = {
                'item_id': '1',
                'pay_pass': '',
                }
                response = session.post('https://api.leadingiot.com/buy_user_robot', headers=headers, json=json_data,timeout=7)
                #print(response.text)
#                print()
                json_data = {
                'page': 1,
                }
                response = session.post('https://api.leadingiot.com/load_user_robots', headers=headers, json=json_data,timeout=7).json()
                
                #print(response)
#                print()
                idt=(response['data'][0]['id'])
                #print(idt)
#                print()
                response = session.get('https://api.leadingiot.com/load_other_link', headers=headers,timeout=7)
                #print(response.text)
#                print()
                
                json_data = {
                'page': 1,
                }
                
                response = session.post('https://api.leadingiot.com/load_team_robots', headers=headers, json=json_data,timeout=7)

                #print(response.text)
#                print()
                
                json_data = {
                'item_id': idt,
                }
                response = session.post('https://api.leadingiot.com/active_user_robot', headers=headers, json=json_data,timeout=7).json()
                #print(response)
#                print()
                print(f"\n                    [ Done Create Account ]\n")
                with open('acc.txt','a') as u:
                    u.write(uu)


for x in range(9999):
    try:
        pro()
    except:
        y=6
        #print("\n Wrong\n")
    else:
        y=0
        #print("\n Done\n")
        
