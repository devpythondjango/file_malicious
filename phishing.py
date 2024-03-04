import re

def is_phishing(url):
    # Проверка наличия подозрительных ключевых слов в URL-адресе
    suspicious_keywords = ['secure', 'account', 'login', 'verify', 'update', 'bank', 'paypal']
    for keyword in suspicious_keywords:
        if keyword in url:
            return True

    # Проверка длины URL-адреса
    if len(url) < 10:
        return True

    # Проверка домена на наличие цифр или длинных поддоменов
    domain = re.findall(r"://([^/]+)/?", url)[0]
    if re.search(r'\d', domain) or len(domain.split('.')) > 3:
        return True

    return False

if __name__ == "__main__":
    test_urls = [
        "https://example.com",
        "https://secure-login.com",
        "https://suspicious-site.com",
        "https://paypal-update.verify.com",
        "https://123.456.789.123/login",
        "https://login.samtuit.uz",
        "https://samtuit.uz",
        "https://kun.uz"
    ]

    for url in test_urls:
        if is_phishing(url):
            print(f"URL {url} fishing bo'lishi mumkin")
        else:
            print(f"URL {url} fishing emas")

