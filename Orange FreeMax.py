import os
try:
    import requests
except:
    os.system("pip install requests")
import requests


pnum=input(" Enter Family Number: ")
ppass=input(" Enter Family Passowrd: ")
mn = input(" Enter Your Number: ")

ur1 = 'https://services.orange.eg/SignIn.svc/SignInUser'

headers ={'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 6 Pro MIUI/V10.3.6.0.PEKMIXM)',
                  'Host': 'services.orange.eg',
                  'Accept-Encoding': 'gzip'}

data1 = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (pnum,ppass)
req1=requests.post(ur1,headers=headers,data=data1)
#---------------------------------------------------------------
if(not req1.json()["SignInUserResult"]["ErrorCode"]==0):
	if("ip" in req1.text):
		print("="*60)
		print(" Error Number or Password\n")
		print("="*60)
		exit()
	else:
		print("="*60)
		print(" Error Number or Password\n")
		print("="*60)
		exit()
else:
	print("="*60)
	print("\n                 Successfully logged in\n")
	userid=req1.json()["SignInUserResult"]["UserData"]["UserID"]
	pass
print("="*60)
print()
#---------------------------------------------------------------


print("\n [0] For Add \n [1] For Delete\n")
c = input(" Enter Your Choice: ")
if c == "0":
    
    url = "https://backend.orange.eg/api/HybridFamily/ManageSharing"
    json ={"ActionType":"2","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"FamilyMemberDial":mn,"lang":"ar","Sharing":[{"SharedAmount":"1","SharingType":5}],"dial":pnum,"IsEasyLogin":False,"password":ppass}
    
elif c == "1":
    
    url = "https://backend.orange.eg/api/HybridFamily/ManageFamily"
    json = {"ActionType":"3","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"FamilyMemberDial":mn,"FamilyOwnerDial":pnum,"lang":"ar","dial":pnum,"IsEasyLogin":False,"password":ppass}
    
else:
    print(" Flase Choice")
    exit()


	
re=requests.get("https://testing339.000webhostapp.com/Yassa-Pro.php").json()
ctv = (re["ctv"])
htv = (re["htv"])
	
a = {"_ctv": ctv,
"_htv": htv,
"isEasyLogin": "false",
"UserId": userid,
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "190",
"Host": "backend.orange.eg",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.12.1"}
	
	



b = requests.post(url,headers=a,json=json).text
print (b)
