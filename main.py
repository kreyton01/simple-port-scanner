from socket import *

def conScan(trgtHost, trgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((trgtHost, trgtPort))
        print('[+]%d/tcp open'% trgtPort)
        connskt.close()

    except:
        print('[-]%d/tcp closed'% trgtPort)

def portScan (trgtHost, trgtPorts):
    try:
        trgtIP = gethostbyname(trgtHost)
    except:
        print('[-] Cannot resolve %d '% trgtHost)
        return
    try:
        trgtName = gethostbyaddr(trgtIP)
        print('\n[+] Scan result of %s ' % trgtName[0])
    except:
        print('\n[+] Scan result of: %s ' % trgtIP)
    setdefaulttimeout(1)
    for trgtPort in trgtPorts:
        print('Scanning Port: %d ' % trgtPort)
        conScan(trgtHost, int(trgtPort))


# portscan('address', [ports to scan])
if __name__ == '__main__':
    portScan('google.com', [80,22])
