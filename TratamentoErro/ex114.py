import urllib.request

try:
    site = urllib.request.urlopen('https://www.linkedin.com/', timeout=10)
except urllib.erro.URLError:
    print(f'O site Linkedin não está acessivel no momento.')
else:
    print('Site acessível! Código de status:', site.status)
