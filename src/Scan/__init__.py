                                            
import sys
import socket
import Manager as manager


def scan(path, ip, port):
    try:
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.05)
        code = client.connect_ex((ip, port))
        if code == 0:
            manager.writeTXT(path, port)
    except Exception as e:
        print("Error, something is wrong", e)