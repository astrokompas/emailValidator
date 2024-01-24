import socket

def validateMX(email, ports):
    domain = email.split('@')[1]

    for port in ports:
        try:
            mx_records = sorted(socket.getaddrinfo(domain, port, socket.AF_INET, socket.SOCK_STREAM))

            if mx_records:
                return True

        except (socket.gaierror, socket.timeout, socket.error):
            pass

    return False