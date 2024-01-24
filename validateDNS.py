import socket

def validateDNS(email):
    domain = email.split('@')[1]

    try:
        socket.gethostbyname(domain)
        return True
    except (socket.gaierror, socket.timeout, socket.error):
        return False