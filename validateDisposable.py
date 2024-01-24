def disposableDomains(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def validateDisposable(email, disposable_domains):
    domain = email.split('@')[1]

    for disposable_domain in disposable_domains:
        if domain.endswith(disposable_domain):
            return False

    return True