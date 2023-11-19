from socket import *

sender = socket()

try:
    sender.bind(('localhost', 9999))

    sender.listen()

    receiver_socket, address = sender.accept()

    print("Connection established from address ", address)

    while True:
        message = input("Enter message to send or 'close' to close connection: ")
        if(message == "close"):
            break
        receiver_socket.send(bytes(message, "utf-8"))

    receiver_socket.close()
    sender.close()
    print("Connection closed successfully!")

except Exception as error:
    print("Error occured: ", error)