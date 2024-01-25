import re

def extract_domain(email):
    match = re.search(r"@([\w.]+)", email)
    return match.group(1) if match else None

def filterAndDelete(emails, domains):
    return [email for email in emails if extract_domain(email) not in domains]

