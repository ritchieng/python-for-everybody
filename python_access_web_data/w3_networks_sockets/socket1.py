import socket

# CREATE ENDPOINT
# socket - library
# socket - method within library
# (socket.AF_INET, socket.SOCK_STREAM) --> make internet socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# PUSH ENDPOINT THROUGH WEB
# Establish connection between me and host with port 80
# Want the other end to be www.py4inf.com
# Most like the open() call to read a file
mysock.connect(('www.pythonlearn.com', 80))
# www.py4inf.com --> host
# 80 --> port

# SEND REQUEST
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

# LOOP TO READ
while True:
    # Call to receive
    data = mysock.recv(512)
    # When last data, break the loop
    if len(data) < 1:
        break
    # Get data
    print data
# Close the socket
mysock.close()







