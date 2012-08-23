import socket
import os

greenlist = {}
online = []

def startup():
    global name
    servisnew = 0
    try:
        meta = open("metadata.fue", "r")
    except IOError as e:
        print "NEW SERVER"
        servisnew = 1
        name = raw_input("Please enter a name for the server: \n")
        meta = open("metadata.fue", "w")
        meta.writelines(name + "\n")
        meta.writelines(str(os.times()) + "\n")
        meta.writelines(os.name + "\n")
        meta.writelines("/////////////")
        meta.close()
    if servisnew == 0:
        meta = open("metadata.fue", "r+")
        oldmetaV = meta.readline()
        endname = oldmetaV.find("\n")
        name = oldmetaV[0:endname]
        meta.writelines("\n" + str(os.times()) + "\n")
        meta.writelines(os.name + "\n")
        meta.writelines("/////////////")
    try:
        log = open("log.fue", "r")
    except IOError as e:
        log = open("log.fue", "w")
        log.close()
        isnew = 1

def logIn(client, address, data):
    logentry = ("LOGI: " + str(client) + ' ' + str(address) + ' ' + data)
    print logentry
    log = open("log.fue", "r+")
    log.writelines(logentry)
    greenlist[address] = username
    logV = log.read()
    endUsnm = data.find(' ')
    username = data[:endUsnm]
    startpass = endUsnm + 1
    endpass = data.find(' ', startpass)
    password = data[startpass:endpass]
    online.append(username)
    if data[-1] == 0:
        if logV.find(username) != -1:
            x1 = logV.find(username)
            x2 = logV.find(' ', x1)
            y1 = x2 + 1
            y2 = logV.find(' ', y1)
            pasw = logV[y1:y2]
            if pasw == password:
                return 1
            else:
                log.writelines("DENY: INCORRECT PASSWORD")
                print "DENIED: " + str(address) + ": INCORRECT PASSWORD"
                return 0            
        else:
            log.writelines("DENY: NEW")
            print ("DENIED: " + str(address) + ": NEW")
            return 0
    else:
        log.writelines("NEWUSER: " + username + ' ' + password + ' ' + str(address) + ' | ')
        print "NEWUSER: " + username + ' ' + password + ' ' + str(address)
        return 1
    log.close()

def logOut(address, data)
    try:
        del greenlist[address]
    except NameError:
        print "not logged in"
        return "0 not logged in"

def main():
    global name
    host = ''
    port = 1013
    pool_size = 5
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(pool_size)
    while 1:
        client, address = s.accept()
        print ("Client is: " + str(client))
        print ("Address is: " + str(address))
        data = client.recv(size)
        if data:
            print data
            if data.find('LOGI') == 0:
                print ("login application from " + str(address))
                dAta = data[5:]
                entrysuccess = logIn(client, address, dAta)
                if entrysuccess == 1:
                    client.send("1 " + name)
                    print "Client " + str(address) + " logged in successfully."
                else:
                    client.send("0")
                    print "Error logging in: client denied."
            if data[0:3] == 'LOGO':
                logOut(address, data)
                client.send("Logged out successfully.")
            if data[0:3] == 'MOVE':
                return 0
        else:
            client.send("Illegal action: empty packet")
        client.close() 

startup()
main()
