import re

patron = r'^((https|http):\/\/)?(www\.)?[\da-z\.-]+\.[a-z\.]{2,6}[\/\w\.\-]*(\/|\?)?([\w\-]+=[\w\-]+&?)*$'

urls = [
    'https://www.facebook.com/',
    'http://www.facebook.com/',
    'exe://www.facebook.com/',
    'www.facebook.com.ar',
    'facebook.com',
    'https://www.youtube.com.ar/watch?v=dQw4w9WgXcQ'
]

for url in urls:
    if re.match(patron, url):
        print(f'{url} es una URL válida')
    else:
        print(f'{url} no es una URL válida')
