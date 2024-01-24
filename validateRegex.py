import re

def validateRegex(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    match = re.match(regex, email)
    
    if match:
        return True
    else:
        return False