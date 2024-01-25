import socket

def validateDNS(email):
    if '@' not in email:
        return False
    
    domain = email.split('@')[1]

    try:
        socket.gethostbyname(domain)
        return True
    except (socket.gaierror, socket.timeout, socket.error):
        return False