import re

def extract_domain(email):
    match = re.search(r"@([\w.]+)", email)
    return match.group(1) if match else None

def filterAndKeep(emails, domains):
    return [email for email in emails if extract_domain(email) in domains]