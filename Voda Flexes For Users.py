import requests,os
print ("\n Dev: https://YassaHany\n\n Dev Channel: https://YassaTeam\n")
print("="*50)
n = input("\n Enter the Family number: ")
p = input(" Enter the Family password: ")
    



headers1 = {
    'Accept': 'application/json, text/plain, */*',
    'x-dynatrace': 'MT_3_8_3300078660_17-0_a556db1b-4506-43f3-854a-1d2527767923_0_8377_318',
    'x-agent-operatingsystem': '1630483957',
    'clientId': 'AnaVodafoneAndroid',
    'x-agent-device': 'RMX1911',
    'Host': 'mobile.vodafone.com.eg',
    'User-Agent': 'okhttp/4.9.1',
}
da= {
    'username': n,
    'password': p,
    'grant_type': 'password',
    'client_secret': 'a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3',
    'client_id': 'my-vodafone-app',
}
b = requests.post('https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token', headers=headers1, data=da)

try:
    access_token = b.json()['access_token']
except:
    print("\n Erorr Number Or Password In Family Owner")
    exit()
else:
    print("\n Done Login In Family Owner")

print("\n [0] For Send Invitation\n [1] For Cancel Invitation\n")
c = input(" Enter Your Choice: ")
if c == "0":
    type = "SendInvitation"
    mn = input("\n Enter the member number: ")
    mp = input(" Enter the member password: ")
    percentage = input(" Enter the percentage for the member: ")
elif c == "1":
    type = "CancelInvitation"
    mn = input("\n Enter the member number: ")
    mp = "Yassa Ya 3lam"
    percentage = "1"
else:
    print(" Flase Choice")
    exit()
    
url1 = 'https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup'

headers2 = {
'Authorization':f"Bearer {access_token}",
'api-version': 'v2',
'x-agent-operatingsystem': '1601266300',
'clientId': 'AnaVodafoneAndroid',
'x-agent-device': 'b1231',
'x-agent-version': '2022.2.1.1',
'x-agent-build': '502',
'Accept': 'application/json',
'msisdn': n,
'Accept-Language': 'en',
'Content-Type': 'application/json; charset=UTF-8',
'Content-Length': '532',
'Host': 'mobile.vodafone.com.eg',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/4.9.1'}

data2 ={"category":[{"listHierarchyId":"PackageID","value":"523"},{"listHierarchyId":"TemplateID","value":"47"},{"listHierarchyId":"TierID","value":"523"},{"listHierarchyId":"familybehavior","value":"percentage"}],"name":"FlexFamily","parts":{"characteristicsValue":{"characteristicsValue":[{"characteristicName":"quotaDist1","type":"percentage","value": percentage}]},"member":[{"id":[{"schemeName":"MSISDN","value":n}],"type":"Owner"},{"id":[{"schemeName":"MSISDN","value":mn}],"type":"Member"}]},"type":type}

re1 = requests.post(url1, headers=headers2, json=data2).text
print()
if "{}" in re1:
    print(f" Done {type}")
elif "maximum" in re1:
    print(" Cancel Invitation Before And Try Again")
    exit()
elif "Customer not eligible-Family member" in re1:
    print(" Cancel Invitation Before And Try Again")
    exit()

else:##
    print(" Erorr Try Again")
    exit()


if type == "CancelInvitation":
    exit()
else:
    Yassa="Yassa"

da2= {
    'username': mn,
    'password': mp,
    'grant_type': 'password',
    'client_secret': 'a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3',
    'client_id': 'my-vodafone-app',
}
b2 = requests.post('https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token', headers=headers1, data=da2)

try:
    access_token2 = b2.json()['access_token']
except:
    print("\n Erorr Number Or Password In Family Member")
    exit()
else:
    print("\n Done Login In Family Member\n")
    
    
url2="https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"




hd={
    
    "Host": "mobile.vodafone.com.eg",
    "x-dynatrace":"MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
    "msisdn": mn,
    "api-version":"v2",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "Authorization": f"Bearer {access_token2}",
    "x-agent-device":"RMX1911",
    "Accept": "application/json",
    "x-agent-version":"2022.2.1.2",
    "x-agent-build":"503",
    "Accept-Language":"ar",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"302",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
}

json={"category": [{"listHierarchyId": "TemplateID", "value": "47"}], "name": "FlexFamily", "parts": {"member": [{"id": [{"schemeName": "MSISDN", "value": "2"+n}], "type": "Owner"}, {"id": [{"schemeName": "MSISDN", "value": mn}], "type": "Member"}]}, "type": "AcceptInvitation"}
    
    
re2=requests.patch(url2, headers=hd, json=json).text


if "{}" in re2:
    print(f" Done Accept Invitation\n")
    data2 ={"category":[{"listHierarchyId":"PackageID","value":"523"},{"listHierarchyId":"TemplateID","value":"47"},{"listHierarchyId":"TierID","value":"523"},{"listHierarchyId":"familybehavior","value":"percentage"}],"name":"FlexFamily","parts":{"characteristicsValue":{"characteristicsValue":[{"characteristicName":"quotaDist1","type":"percentage","value": percentage}]},"member":[{"id":[{"schemeName":"MSISDN","value":n}],"type":"Owner"},{"id":[{"schemeName":"MSISDN","value":mn}],"type":"Member"}]},"type":"CancelInvitation"}
    re1 = requests.post(url1, headers=headers2, json=data2).text
    if "{}" in re1:
        print(" Done Cancel Invitation\n")
    elif "maximum" in re1:
        print(" Cancel Invitation Before And Try Again")
        exit()
    elif "Customer not eligible-Family member" in re1:
        print(" Cancel Invitation Before And Try Again")
        exit()
    else:
        print(" Erorr Try Again")
        exit()
        
elif "No" in re2:
    print(" Send Invitation Before And Try Again")
    exit()
else:##
    print(" Erorr Try Again")
    exit()