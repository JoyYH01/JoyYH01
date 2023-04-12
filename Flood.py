import requests,threading,time
url = input ("\033[1;32m Enter Domain WebSite : ")
print ("\033[1;31m="*60)
nu = int(input("\033[1;32m Enter Number Of Threads : "))
def th():
    re=requests.get(url)
    print(re)

for x in range(nu):
    threading.Thread(target=th).start()
