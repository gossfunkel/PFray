import socket

def server():
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
        print 'Recieved: ', data
        incomingData = cLient(data)
        print 'Recieved: ', incomingData
        client.send(incomingData)
        client.close() 

def cLient(message):
    host = '94.168.165.115'
    port = 1013
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(message)
    data = s.recv(size)
    s.close()
    return data 

server()
client()
