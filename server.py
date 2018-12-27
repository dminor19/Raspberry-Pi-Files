from socket import *

host = "10.0.0.49"

print host

port = 7777

s = socket(AF_INET, SOCK_STREAM)

print "Socket Made"

s.bind((host,port))

print "Socket Bound"

s.listen(5)

print "Listening for connections..."

q,addr = s.accept()

data = raw_input("Enter data to be sent: ")

q.send(data)  
