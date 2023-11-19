from socket import *

receiver = socket()

try:
    receiver.connect(('localhost', 9999))

    while True:
        message = receiver.recv(1024).decode()
        if not message:
            break
        print(message)

    receiver.close()
    print("Connection closed successfully!")
    
except Exception as error:
    print("Error occured: ", error)
